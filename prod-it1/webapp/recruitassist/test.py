import requests
import json

loc=["La Trobe Region","Geelong Region","La Trobe Region","Bendigo Region","Shepparton Region","Ballarat Region","Mildura Region",
          "Warrnambool Region","Horsham Region","Wodonga Region"]

cat=["it-jobs","admin-jobs","healthcare-nursing-jobs","accounting-finance-jobs",
    "teaching-jobs","sales-jobs","Engineering-jobs"]



result={}

for l in loc:
    salary_list=[]
    print (l)
    for c in cat:
        print (c)
        temp={}

        url = "http://api.adzuna.com/v1/api/jobs/au/history?app_id=4cb38e73&app_key=ca142ad047eb88bae578bdca2a3eef4f&where=" + l + "&category=" + c + "&content-type=application/json"
        data = requests.get(url).json()
        salary = data.get('month')
        for key in sorted(salary.keys()):
            temp[key]=salary[key]
        salary_list.append(temp)
    result[l] = salary_list

with open('api_salary.txt', 'w', encoding='utf-8') as filehandle:
    json.dump(result, filehandle)






