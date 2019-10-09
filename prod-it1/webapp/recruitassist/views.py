from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import Providers
import requests
import json,os
from django.conf import settings
import re


def password(request):
   return render(request, 'recuritassist/password.html')

def index(request):
   return render(request, 'recuritassist/Homepage_final_version.html')

def seek(request):

    return render(request, 'recuritassist/SeekSuburb-index.html')

def service(request):

    return render(request, 'recuritassist/ShowService.html')


def home(request):
    return render(request, 'recuritassist/Homepage-IE.html')

def about_us (request):
    return render(request, 'recuritassist/about_us.html')

def quiz(request):
    return render(request, 'recuritassist/quiz.html')   # this returns the  quiz.html page back to the website

def Homepage_fianl_version(request):
    return render(request, 'recuritassist/Homepage_final_version.html')   # this returns the  quiz.html page back to the website

def Homepage_job(request):
    return render(request, 'recuritassist/Homepage_job.html')   # this returns the  quiz.html page back to the website

def Homepage_skill(request):
    return render(request, 'recuritassist/Homepage_skill.html')   # this returns the  quiz.html page back to the website

def job_advert(title,location):
    all_jobs=[]
    dict_of_jobs={}
    print(title)
    file_path = os.path.join(settings.BASE_DIR, 'recruitassist/api_data.txt')
    with open(file_path, 'r', encoding='utf-8') as filehandle:
        for line in filehandle:
            # remove linebreak which is the last character of the string
            j = line[:-1]
            # add item to the list
            all_jobs.append(j)
    job_name=title.strip(' ')
    t=job_name.split(' ')
    print(t)
    print(location)


    for job in all_jobs:
        jd=job.split(',')
        vacanay=jd[2]
        vacanay=vacanay.upper()

        for vac in t:
            p = re.compile(r'\b'+vac.upper()+'\\b')

            if  p.search(vacanay) and (jd[1]==location and jd[0]!= 'Unknown' and jd[0]!='Property Jobs' and jd[0]!='Hospitality & Catering Jobs' and
                                      jd[0]!='Customer Services Jobs' and jd[0]!='Part time Jobs') :

                dict_of_jobs[jd[len(jd)-1]]= jd[2]+','+jd[4]+','+ jd[1]+','+ jd[5]

    print("final",dict_of_jobs)
    return (dict_of_jobs)

def access_jobs(suburb):
    all_jobs=[]
    dict_of_jobs={}
    file_path = os.path.join(settings.BASE_DIR, 'recruitassist/api_data.txt')
    with open(file_path, 'r', encoding='utf-8') as filehandle:
        for line in filehandle:
            # remove linebreak which is the last character of the string
            j = line[:-1]
            # add item to the list
            all_jobs.append(j)


    count=0
    for job in all_jobs:
        jd=job.split(',')
        if jd[1]== suburb and (jd[0]!= 'Unknown' and jd[0]!='Property Jobs' and jd[0]!='Hospitality & Catering Jobs'
                               and jd[0]!='Part time Jobs') :
            if jd[0] not  in dict_of_jobs:
                dict_of_jobs[jd[0]]=1
            else:
                dict_of_jobs[jd[0]]+=1

    return (dict_of_jobs)

def top_suburbs(job_name,flag):
    all_jobs=[]
    dict_of_jobs={}
    file_path = os.path.join(settings.BASE_DIR, 'recruitassist/api_data.txt')
    with open(file_path, 'r',encoding='utf-8') as filehandle:
        for line in filehandle:
            # remove linebreak which is the last character of the string
            j = line[:-1]
            # add item to the list
            all_jobs.append(j)
    job_name=job_name.strip(' ')
    t=job_name.split(' ')
    print(t)

    if flag=='MELB':

        count=0
        for job in all_jobs:
            jd=job.split(',')
            vacanay=jd[2]
            vacanay=vacanay.upper()
            for vac in t:
                p = re.compile(r'\b'+vac.upper()+'\\b')

                if p.search(vacanay) and (jd[0]!= 'Unknown' and jd[0]!='Property Jobs' and jd[0]!='Hospitality & Catering Jobs' and
                                          jd[0]!='Customer Services Jobs' and jd[0]!='Part time Jobs') :
                    if jd[1] not in dict_of_jobs:
                        dict_of_jobs[jd[1]]=1
                    else:
                        dict_of_jobs[jd[1]]+=1

    else:
        print ("Without Melbourne Region")
        count=0
        for job in all_jobs:
            jd=job.split(',')

            vacanay=jd[2]
            vacanay=vacanay.upper()

            for vac in t:

                p = re.compile(r'\b'+vac.upper()+'\\b')
                if  p.search(vacanay) and jd[3]!="Melbourne Region" and (jd[0]!= 'Unknown' and jd[0]!='Property Jobs' and jd[0]!='Hospitality & Catering Jobs' and
                                      jd[0]!='Customer Services Jobs' and jd[0]!='Part time Jobs') :
                    print ("going in",jd[3])
                    if jd[1] not in dict_of_jobs:
                        dict_of_jobs[jd[1]]=1
                    else:
                        dict_of_jobs[jd[1]]+=1
    print("final",dict_of_jobs)
    print (flag)

    return (dict_of_jobs)


def quiz_new(request):
    return render(request, 'recuritassist/quiz_new.html')   # this returns the  quiz.html page back to the website

def quiz_result(request):
    service = {'msg': None}
    nearby_service = {'msg': None}
    context = {}
    print("check the values")
    print(request.POST)
    if (request.POST.get('Question1') == "Yes" or request.POST.get('Question2') == "Yes" or \
        request.POST.get('Question4') == "Yes" or request.POST.get('Question5') == "Yes" and
        request.POST.get('Question3') == "No"):
        service['msg'] = "Accredited Training"
    elif (request.POST.get('Question1') == "No" or request.POST.get('Question2') == "No" or \
            request.POST.get('Question4') == "No" or request.POST.get('Question5') == "No" and
            request.POST.get('Question3') == "Yes"):
        service['msg'] = "Employer-required Training"
    elif (request.POST.get('Question1') == "Yes" or request.POST.get('Question2') == "Yes" or \
            request.POST.get('Question4') == "Yes" or request.POST.get('Question5') == "Yes") and request.POST.get('Question3') == "Yes":
        service['msg'] = "Employer-required Training and Accredited Training"
    else:
        service['msg'] = "Please choose the answer for the questions first!"
    if 'suburb' in request.POST:
        suburb = request.POST.get('suburb')

        objall = Providers.objects.all()
        list_of_obj = []
        total = objall.count()
        i = 1
        postcode = 0
        while (i <= total):
            if suburb.upper() == objall.get(ID=i).SITE_SUBURB:
                o1 = objall.get(ID=i)
                postcode = o1.POSTCODE
                # print(o1.POSTCODE)
                str1 = o1.URL
                index = str1.find('http')
                if index != 0 and len(str1) > 1:
                    o1.URL = "http://" + str1
                    print(o1.URL)
                else:
                    print(o1.URL)
                # print ( o1.SITE_NAME + o1.ADDRESS + o1.CONTACT + o1.URL + o1.EMAIL_ADDRESS  )
                list_of_obj.append(o1)

            i += 1
    else:
        service['msg'] = "Something went wrong"
        return HttpResponse('/')

    # Way to get data for postcode is 1 different with providers
    list_of_nearby = []
    temp = 1
    while (temp <= total):
        if abs(objall.get(ID=temp).POSTCODE - postcode) < 10 and (objall.get(ID=temp).POSTCODE != postcode):
            o2 = objall.get(ID=temp)
            str2 = o2.URL
            index = str2.find('http')
            if index != 0 and len(str2) > 1:
                o2.URL = "http://" + str2
                # print(o2.URL)
            # else:
            #     print(o2.URL)
            # print ( o1.SITE_NAME + o1.ADDRESS + o1.CONTACT + o1.URL + o1.EMAIL_ADDRESS  )
            list_of_nearby.append(o2)
        temp += 1

    for item in list_of_nearby:
        print("original postcode:" + str(postcode))
        print("new postcode:" + str(item.POSTCODE))
    print(postcode)
    print(service)

    i = 0
    pos = 0
    print(list_of_obj)
    final = []
    for obj in list_of_obj:

        print(obj.ADDRESS)
        i += 1

        for c in range(i, len(list_of_obj) - 1):
            if obj.ADDRESS == list_of_obj[c].ADDRESS:
                final.append(pos)

        pos += 1
    s = set(final)
    final = list(s)

    for i in range(len(final)):
        del list_of_obj[final[0]]
        del final[0]
        final = [item - 1 if item > 0 else item for item in final]

    if len(list_of_obj) == 0:
        context['msg'] = "Please enter the correct suburb.....redirecting!"
        return render(request, 'recuritassist/failure.html', {'obj': context})
    # elif len(list_of_obj) < 4:
    #     nearby_service['msg'] = "Some providers in nearby suburb!"
    #     return render(request, 'recuritassist/new_result.html',
    #                   {'obj': list_of_obj, 'nearby': list_of_nearby, 'service': service, 'nearby_service':nearby_service})
    else:
        return render(request, 'recuritassist/new_result.html', {'obj': list_of_obj, 'service': service, 'nearby': list_of_nearby})

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
        postcode = 0
        while(i<= total):
            if suburb.upper() == objall.get(ID=i).SITE_SUBURB:
                o1=objall.get(ID=i)
                postcode = o1.POSTCODE
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

    list_of_nearby = []
    temp = 1
    while (temp <= total):
        if abs(objall.get(ID=temp).POSTCODE - postcode) < 10 and (objall.get(ID=temp).POSTCODE != postcode):
            o2 = objall.get(ID=temp)
            str2 = o2.URL
            index = str2.find('http')
            if index != 0 and len(str2) > 1:
                o2.URL = "http://" + str2
                # print(o2.URL)
            # else:
            #     print(o2.URL)
            # print ( o1.SITE_NAME + o1.ADDRESS + o1.CONTACT + o1.URL + o1.EMAIL_ADDRESS  )
            list_of_nearby.append(o2)
        temp += 1

    print(service)
    i=0
    pos=0
    print(list_of_nearby)
    final =[]
    for nobj in list_of_nearby:

        print(nobj.ADDRESS)
        i+=1

        for c in range(i,len(list_of_nearby)-1):
            if nobj.ADDRESS == list_of_nearby[c].ADDRESS:

                final.append(pos)

        pos+=1
    n=set(final)
    final=list(n)

    for i in range(len(final)):
        del list_of_nearby[final[0]]
        del final[0]
        final = [item-1 if item > 0 else item for item in final]

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
        return render(request,'recuritassist/new_result.html',{'obj':list_of_obj, 'service':service, 'nearby': list_of_nearby})


@csrf_exempt
def location_choose(request): #This function used in the first one show the job shortage in one location
    result = {}
    totaljobs=0
    location_name = request.POST.get('suburb')
    print(location_name)
    totaljobs= access_jobs(location_name)

    temp = sorted(totaljobs.items(), key=lambda x: x[1], reverse=True)
    print(temp)
    for i in range(0,len(temp)):
        result[temp[i][0]] = temp[i][1]
    print(result)

    return HttpResponse(json.dumps(result))

@csrf_exempt
def salary_information(request): #This function used in the first one show the job shortage in one location
    print(request.POST)
    temp={}
    location = request.POST.get('suburb')
    category = request.POST.get('category')
    url = "http://api.adzuna.com/v1/api/jobs/au/history?app_id=4cb38e73&app_key=ca142ad047eb88bae578bdca2a3eef4f&where=" + location + "&category=" + category + "&content-type=application/json"
    data = requests.get(url).json()
    salary = data.get('month')
    for key in sorted(salary.keys()):
        temp[key]=salary[key]
    print(temp)
    return HttpResponse(json.dumps(temp))

@csrf_exempt
def jobs(request): #This function used to get the job details

    job_desc= job_advert(request.POST.get('title'),request.POST.get('location'))
    for k in job_desc.keys():
        print("dict content")
        # alist = []
        alist = job_desc[k].split(',')
        print(alist)
        adict = {}
        adict['job_title'] = alist[0]
        adict['company_name'] = alist[1]
        adict['location'] = alist[2]
        adict['url'] = alist[3]
        job_desc[k] = adict
    print("result")
    print(job_desc)
    return HttpResponse(json.dumps(job_desc))

@csrf_exempt
def top_jobs_without_mel(request): #This function used in the second one show top 10 suburb best for the job you choose

    flag= "MELB"
    if (request.POST.get('area')) == "noMelb":
        flag="no"
    print("flag",flag)
    result = {}
    print(request.POST)
    job_name = request.POST.get('jobs')
    print(job_name)
    totaljobs= top_suburbs(job_name,flag)
    temp = sorted(totaljobs.items(), key=lambda x: x[1], reverse=True)
    print ("sorted",temp)
    if len(temp) > 10:
        for i in range(0,10):
            result[temp[i][0]] = temp[i][1]
    else:
        for i in range(0,len(temp)):
            result[temp[i][0]] = temp[i][1]
    print(result)
    print("here")
    return HttpResponse(json.dumps(result))
