from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import Providers
import requests
import json,os
from django.conf import settings



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

def quiz(request):
    return render(request, 'recuritassist/quiz.html')   # this returns the  quiz.html page back to the website

def access_jobs(suburb):
    all_jobs=[]
    dict_of_jobs={}
    file_path = os.path.join(settings.BASE_DIR, 'recruitassist/api_data.txt')
    with open(file_path, 'r') as filehandle:
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
    with open(file_path, 'r') as filehandle:
        for line in filehandle:
            # remove linebreak which is the last character of the string
            j = line[:-1]
            # add item to the list
            all_jobs.append(j)


    if flag=='MELB':

        count=0
        for job in all_jobs:
            jd=job.split(',')
            vacanay=jd[2]
            vacanay=vacanay.upper()

            if job_name.upper() in vacanay and (jd[0]!= 'Unknown' and jd[0]!='Property Jobs' and jd[0]!='Hospitality & Catering Jobs' and
                                      jd[0]!='Customer Services Jobs' and jd[0]!='Part time Jobs') :
                if jd[0] not in dict_of_jobs:
                    dict_of_jobs[jd[1]]=1
                else:
                    dict_of_jobs[jd[1]]+=1

    else:

        count=0
        for job in all_jobs:
            jd=job.split(',')
            vacanay=jd[2]
            vacanay=vacanay.upper()

            if job_name.upper() in vacanay and jd[1]!='Melbourne'and (jd[0]!= 'Unknown' and jd[0]!='Property Jobs' and jd[0]!='Hospitality & Catering Jobs' and
                                      jd[0]!='Customer Services Jobs' and jd[0]!='Part time Jobs') :
                if jd[0] not in dict_of_jobs:
                    dict_of_jobs[jd[1]]=1
                else:
                    dict_of_jobs[jd[1]]+=1
    print("final",dict_of_jobs)
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
    context = {}
    dict = {}
    result = {}
    totaljobs=0
    print(request.POST)
    location_name = request.POST.get('suburb')
    print(location_name)
    # Could add some jobs you think is okay to the list, which is used to make comparing
    # I removed business because it is too board and too many jobs about it, you could search for the amount on adzuna before add
    job_list = ["ICT", "Accounting", "Health", "Engineering", "Marketing", "Finance", "Science", "Business",
                "Education","Arts"]
    # put work title in what=""
    # put location in where=""
    # please do some research about how the api works for the full-time job only
    totaljobs= access_jobs(location_name)

    temp = sorted(totaljobs.items(), key=lambda x: x[1], reverse=True)
    print(temp)
    for i in range(0,len(temp)):
        result[temp[i][0]] = temp[i][1]
    print(result)

    return HttpResponse(json.dumps(result))

@csrf_exempt
def top_jobs(request): #This function used in the second one show top 10 suburb best for the job you choose
    context = {}
    dict = {}
    result = {}
    print(request.POST)
    job_name = request.POST.get('jobs')
    # Could add some locations you think is okay to the list, which is used to make comparing
    # i remore Melbourne and Geelong because there are too many data for geelong mel and mel cbd

    location_list = ["Airport West", "Albert Park", "Alexandra", "Altona", "Altona Meadows", "Anglesea", "Apollo Bay",
                     "Ararat", "Attwood", "Avoca", "Bacchus Marsh", "Ballan", "Ballarat", "Balwyn", "Bannockburn",
                     "Beechworth", "Belgrave", "Belmont", "Benalla", "Bendigo", "Berwick", "Birchip", "Blackburn",
                     "Boort", "Boronia", "Box Hill", "Briar Hill", "Bright", "Broadford", "Broadmeadows", "Brunswick",
                     "Bundoora", "Bunyip", "Camberwell", "Campbellfield", "Carlton", "Casterton", "Castlemaine",
                     "Chadestone", "Charlton", "Chelsea", "Cheltenham", "Churchill", "Clayton", "Clunes", "Cobden",
                     "Cobram", "Coburg", "Cohuna", "Colac", "Collingwood", "Coria", "Corryong", "Cowes", "Craigieburn",
                     "Cranbourne", "Cuogewa", "Dandenong", "Daylesford", "Docklands", "Donald", "Doncaster", "Doncaster East",
                     "Drouin", "Drysdale", "East Geelong", "Echuca", "Edenhope", "Edithvale", "Elmore", "Elsternwick",
                     "Eltham", "Emerald", "Ensay", "Epping", "Eskdale", "Essendon", "Euroa", "Fitzroy", "Fitzroy North",
                     "Flemington", "Footscray", "Forster", "Frankston", "Geelong", "Gisborne", "Glen Waverley", "Glenroy",
                     "Greensborough", "Grovedale", "Hamilton", "Hastings", "Hawthorn", "Hawthorn East", "Healesville",
                     "Heathcote", "Heidelberg", "Heywood", "Horsham", "Hurstbridge", "Inverloch", "Kensington", "Kerang",
                     "Kilmore", "Kinglake", "Koo Wee Rup", "Kyabram", "Kyneton", "Lake Tyers ", "Lake Entrance", "Lancefield",
                     "Lara", "Leongatha", "Lilydale", "Lorne", "Maffra", "Maldon", "Mallacoota", "Mansfield", "Maryborough",
                     "Marysville", "Melbourne", "Melton", "Melton South", "Merbein", "Mildura", "Mill Park", "Mitcham", "Moe",
                     "Monbulk", "Moonee Ponds", "moorabbin", "Mooroopna", "Mordialloc", "Mornington", "Morwell", "Myrtleford",
                     "Narre Warren", "Neerim South", "Newcomb", "Nhill", "Noble Park", "Norlane", "North Geelong", "North Melbourne",
                     "Northcote", "Numurkah", "Oakleigh", "Ocean Grove", "Omeo", "Orbost", "Ouyen", "Pakeham", "Port Fairy",
                     "Portarlington", "Portland", "Prahran", "Preston", "Queenscliff", "Red Cliffs", "Reservoir", "Richmond",
                     "Ringwood", "Robinvale", "Romsey", "Rosebud", "Rosebud West", "Rowville", "Rutherglen", "Sale",
                     "sab demo", "Sea Lake", "Sebastopol", "Seymour", "Shepparton", "South Melbourne", "Southbank",
                     "South Yarra", "Springvale", "St Albans", "St Arnaud", "Stawell", "Sunbury", "Sunshine", "Swan Hill",
                     "Swifts Creek", "Sydenham", "Tallangatta", "Tarneit", "Tatura", "Taylors Lakes", "Terang", "Timboon",
                     "Torquay", "Traralgon", "Tullamarine", "Wallan", "Walwa", "Wangatatta", "Wantirna South", "Warburton",
                     "Warracknabeal", "Warragul", "Warrnambool", "Watergardens", "Warun Ponds", "Wedderburn", "Wendouree",
                     "Werribee", "Whittington", "Whittlesea", "Wodonga", "Wonthaggi", "Woodend", "Wycheproof", "Yarra Junction", "Yarram", "Yarrawonga", "Yea"]

    for location in location_list:
        url = "https://api.adzuna.com/v1/api/jobs/au/search/1?app_id=4cb38e73&app_key=ca142ad047eb88bae578bdca2a3eef4f&where=" + location +"&results_per_page=20&what=" + job_name + "&content-type=application/json"
        data = requests.get(url)
        dict = json.loads(s=data.text)
        context[location] = dict['count'] #get the number of jobs in each area
    # new_dict2 = {v: k for k, v in context.items()}
    # dict_slice = lambda adict, start, end: {k: adict[k] for k in adict.keys()[start:end]}
    # result = dict_slice(context,0,10) #The first 10 place is shown, index 0-9
    temp = sorted(context.items(), key=lambda x: x[1], reverse=True)
    for i in range(0,10):
        result[temp[i][0]] = temp[i][1]
    print(result)
    # Pass the data to js
    return HttpResponse(json.dumps(result))

@csrf_exempt
def top_jobs_without_mel(request): #This function used in the second one show top 10 suburb best for the job you choose
    flag= "MELB"
    if (request.POST.get('area')) == "noMelb":
        flag="no"

    result = {}
    print(request.POST)
    job_name = request.POST.get('jobs')
    print(job_name)
    totaljobs=  top_suburbs(job_name,flag)
    temp = sorted(totaljobs.items(), key=lambda x: x[1], reverse=True)

    for i in range(0,len(temp)):
        result[temp[i][0]] = temp[i][1]
    print(result)
    print("here")
    return HttpResponse(json.dumps(result))

