from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import Providers
import requests
import json



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
    for job in job_list:
        url = "https://api.adzuna.com/v1/api/jobs/au/search/1?app_id=4cb38e73&app_key=ca142ad047eb88bae578bdca2a3eef4f&where=" + location_name +"&what=" + job + "&content-type=application/json"
        data = requests.get(url)
        dict = json.loads(s=data.text)
        context[job] = dict['count'] #get the number of jobs
        totaljobs+=dict['count']
    print(totaljobs)
    return HttpResponse(json.dumps(context))

@csrf_exempt
def top_jobs(request): #This function used in the second one show top 10 suburb best for the job you choose
    context = {}
    dict = {}
    result = {}
    # the whole list without melbourne regions is like this
    # because it is too long I think we dont need use the whole list, just randomly pick 30 suburbs from it.
    # using this function:
    # import random
    # random.shuffle(location_without_mel)
    # print(new[:30])
    # location_without_mel = ['Alexandra', 'Anglesea', 'Apollo Bay', 'Ararat', 'Attwood', 'Avoca', 'Bacchus Marsh', 'Ballan', 'Ballarat',
    #                         'Balwyn', 'Bannockburn', 'Beechworth', 'Belgrave', 'Belmont', 'Benalla', 'Bendigo', 'Berwick', 'Birchip',
    #                         'Blackburn', 'Boort', 'Briar Hill', 'Bright', 'Broadford', 'Brunswick', 'Bunyip', 'Camberwell',
    #                         'Casterton', 'Castlemaine', 'Charlton', 'Cheltenham', 'Churchill', 'Clunes', 'Cobden', 'Cobram', 'Coburg',
    #                         'Cohuna', 'Colac', 'Collingwood', 'Coria', 'Corryong', 'Cowes', 'Cuogewa', 'Daylesford', 'Donald',
    #                         'Doncaster', 'Doncaster East', 'Drouin', 'Drysdale', 'East Geelong', 'Echuca', 'Edenhope', 'Edithvale',
    #                         'Elmore', 'Elsternwick', 'Eltham', 'Ensay', 'Eskdale', 'Euroa', 'Fitzroy', 'Fitzroy North', 'Forster',
    #                         'Geelong', 'Gisborne', 'Glenroy', 'Grovedale', 'Hamilton', 'Hastings', 'Hawthorn', 'Hawthorn East',
    #                         'Healesville', 'Heathcote', 'Heywood', 'Horsham', 'Inverloch', 'Kerang', 'Kilmore', 'Kinglake',
    #                         'Koo Wee Rup', 'Kyabram', 'Kyneton', 'Lake Tyers ', 'Lake Entrance', 'Lancefield', 'Lara', 'Leongatha',
    #                         'Lorne', 'Maffra', 'Maldon', 'Mallacoota', 'Mansfield', 'Maryborough', 'Marysville', 'Melbourne', 'Melton',
    #                         'Melton South', 'Merbein', 'Mildura', 'Mill Park', 'Mitcham', 'Moe', 'Monbulk', 'Moonee Ponds', 'moorabbin',
    #                         'Mooroopna', 'Mordialloc', 'Morwell', 'Myrtleford', 'Neerim South', 'Newcomb', 'Nhill', 'Noble Park',
    #                         'Norlane', 'North Geelong', 'Northcote', 'Numurkah', 'Ocean Grove', 'Omeo', 'Orbost', 'Ouyen', 'Pakeham',
    #                         'Port Fairy', 'Portarlington', 'Portland', 'Prahran', 'Preston', 'Queenscliff', 'Red Cliffs', 'Reservoir',
    #                         'Robinvale', 'Romsey', 'Rosebud West', 'Rowville', 'Rutherglen', 'Sale', 'sab demo', 'Sea Lake',
    #                         'Sebastopol', 'Seymour', 'Shepparton', 'St Albans', 'St Arnaud', 'Stawell', 'Sunbury', 'Swan Hill',
    #                         'Swifts Creek', 'Sydenham', 'Tallangatta', 'Tarneit', 'Tatura', 'Terang', 'Timboon', 'Torquay',
    #                         'Traralgon', 'Wallan', 'Walwa', 'Wangatatta', 'Warburton', 'Warracknabeal', 'Warragul', 'Warrnambool',
    #                         'Watergardens', 'Warun Ponds', 'Wedderburn', 'Wendouree', 'Whittington', 'Whittlesea', 'Wodonga',
    #                         'Wonthaggi', 'Woodend', 'Wycheproof', 'Yarra Junction', 'Yarram', 'Yarrawonga', 'Yea']

    location_without_mel = ['Moonee Ponds', 'Maffra', 'Rutherglen', 'Leongatha', 'Mooroopna', 'Mill Park', 'Yarrawonga', 'Sydenham',
                            'Queenscliff', 'Whittington', 'Elmore', 'East Geelong', 'Corryong', 'Mallacoota', 'Swan Hill', 'Sunbury',
                            'St Albans', 'North Geelong', 'Wonthaggi', 'Stawell', 'Casterton', 'Heywood', 'Elsternwick', 'Doncaster',
                            'Cobden', 'Ballarat', 'Koo Wee Rup', 'Cowes', 'Romsey', 'Cheltenham']
    print(request.POST)
    job_name = request.POST.get('jobs')
    with_Mel = request.POST.get('withMel')
    Without_Mel = request.POST.get('without_Mel')
    # Could add some locations you think is okay to the list, which is used to make comparing
    # i remore Melbourne and Geelong because there are too many data for geelong mel and mel cbd
    if with_Mel == 'Yes':
        print(with_Mel)
        print("into yes")
        # because the whole list is too long so here only keep the old one
        location_list = ["Airport West", "Balwyn", "Bendigo", "Anglesea", "Berwick", "Box Hill", "Brunswick", "Cheltenham", "Clayton",
                    "Caulfield", "Dandenong", "Docklands","Elsternwick","Flemington","Frankston","Caulfield","Kensington","Lilydale"
                         ,"Carlton","Mornington","North Geelong","North Melbourne","Pakenham","South bank","South yarra","St kilda","Springvale","Richmond"]

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

    if with_Mel != 'Yes':
        print("start without mel")
        result_without_mel = {}
        context_new = {}
        for new_location in location_without_mel:
            new_url = "https://api.adzuna.com/v1/api/jobs/au/search/1?app_id=4cb38e73&app_key=ca142ad047eb88bae578bdca2a3eef4f&where=" + new_location + "&results_per_page=20&what=" + job_name + "&content-type=application/json"
            new_data = requests.get(new_url)
            new_dict = json.loads(s=new_data.text)
            context_new[new_location] = new_dict['count']  # get the number of jobs in each area
        # new_dict2 = {v: k for k, v in context.items()}
        # dict_slice = lambda adict, start, end: {k: adict[k] for k in adict.keys()[start:end]}
        # result = dict_slice(context,0,10) #The first 10 place is shown, index 0-9
        print("new context_new")
        print(context_new)
        temp_new = sorted(context_new.items(), key=lambda x: x[1], reverse=True)
        print("new temp_new")
        print(temp_new)
        for i in range(0, 10):
            result_without_mel[temp_new[i][0]] = temp_new[i][1]
        print(result_without_mel)

        # Pass the data to js
        return HttpResponse(json.dumps(result_without_mel))

@csrf_exempt
def top_jobs_without_mel(request): #This function used in the second one show top 10 suburb best for the job you choose
    context = {}
    dict = {}
    result = {}
    print(request.POST)
    job_name = request.POST.get('jobs')
    # Could add some locations you think is okay to the list, which is used to make comparing
    # i remore Melbourne and Geelong because there are too many data for geelong mel and mel cbd
    location_list = [ "Bendigo", "Anglesea", "Echuca", "Dunkeld", "Cheltenham",
                     "Torquay",
                     "Rosebud", "Moyarra", "Flinders", "Elsternwick", "Flemington", "Winchelsea", "Sunbury",
                     "Kensington", "Belmont", "South Geelong", "North Geelong", "Corio", "Waurn Ponds", "Newcomb", "Epsom",
                     "Flora Hill", "East Bendigo", "Strathfieldsaye"]

    for location in location_list:
        url = "https://api.adzuna.com/v1/api/jobs/au/search/1?app_id=4cb38e73&app_key=ca142ad047eb88bae578bdca2a3eef4f&where=" + location + "&results_per_page=20&what=" + job_name + "&content-type=application/json"
        data = requests.get(url)
        dict = json.loads(s=data.text)
        context[location] = dict['count']  # get the number of jobs in each area
    # new_dict2 = {v: k for k, v in context.items()}
    # dict_slice = lambda adict, start, end: {k: adict[k] for k in adict.keys()[start:end]}
    # result = dict_slice(context,0,10) #The first 10 place is shown, index 0-9
    temp = sorted(context.items(), key=lambda x: x[1], reverse=True)
    for i in range(0, 10):
        result[temp[i][0]] = temp[i][1]
    print(result)
    # Pass the data to js
    return HttpResponse(json.dumps(result))
