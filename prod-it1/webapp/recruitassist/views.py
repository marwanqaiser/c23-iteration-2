from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from .models import Providers

def index(request):
   return render(request, 'recuritassist/Homepage-IE.html')

def seek(request):

    return render(request, 'recuritassist/SeekSuburb-index.html')

def service(request):

    return render(request, 'recuritassist/ShowService.html')


def home(request):
    return render(request, 'recuritassist/Homepage-IE.html')

def about_us (request):
    return render(request, 'recuritassist/about_us.html')

def listprovider(request):
    service = {'msg': None}
    context={}
    print(request.POST)

  ##  if request.POST.get('english') == None and request.POST.get('interview') == None and \
    ##        request.POST.get('commuincation') == None and  request.POST.get('technical') == None:
     ##   context['msg'] = "Please select at least one skill.....redirecting!"
      ##  return render(request,'recuritassist/failure.html', {'obj':context})
    if (request.POST.get('english') == "on" or request.POST.get('interview') == "on" or \
            request.POST.get('commuincation') == "on") and  request.POST.get('technical') == None:
        service['msg']="Accredited Training"
    elif request.POST.get('technical') == "on" and request.POST.get('english') == None and request.POST.get('interview') == None and \
            request.POST.get('commuincation') == None :
       service['msg']="Employer-required Training"
    elif (request.POST.get('english') == "on" or request.POST.get('interview') == "on" or \
        request.POST.get('commuincation') == "on") and request.POST.get('technical') == "on":

       service['msg']= "Employer-required Training and Accredited Training"
    else:
        service= ""

    if 'suburb' in request.POST:
        suburb=request.POST.get('suburb')

        objall=Providers.objects.all()
        list_of_obj= []
        total= objall.count()
        i=1

        while(i<= total):
            if suburb.upper() == objall.get(ID=i).SITE_SUBURB:
                o1=objall.get(ID=i)
                str1=o1.URL
                index=str1.find('http')
                if index != 0 and len(str1)>1:
                    o1.URL= "http://"+ str1
                    print(o1.URL)
                else:
                    print(o1.URL)
               # print ( o1.SITE_NAME + o1.ADDRESS + o1.CONTACT + o1.URL + o1.EMAIL_ADDRESS  )
                list_of_obj.append(o1)

            i+=1
    else:
        service['msg'] = "Something went wrong"
        return HttpResponse('/')

    print(service)

    i=0
    pos=0
    print(list_of_obj)
    final =[]
    for obj in list_of_obj:

        print(obj.ADDRESS)
        i+=1

        for c in range(i,len(list_of_obj)-1):
            if obj.ADDRESS == list_of_obj[c].ADDRESS:

                final.append(pos)

        pos+=1
    s=set(final)
    final=list(s)

    for i in range(len(final)):
        del list_of_obj[final[0]]
        del final[0]
        final = [item-1 if item > 0 else item for item in final]


    if len(list_of_obj) == 0:
        context['msg'] = "Please enter the correct suburb.....redirecting!"
        return render(request,'recuritassist/failure.html', {'obj':context})
    else:
        return render(request,'recuritassist/new_result.html',{'obj':list_of_obj, 'service':service})
