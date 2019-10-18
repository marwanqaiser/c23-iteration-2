# Author: Mohammad Marwan Qaiser
# Last Modified Date: 15/10/2019

# The following code is used to fetch data from API into a file  so that the website response can be improved

import  json,requests
import time

def fetch_all():


    ls=[]
    jobs=[]
    for i in range (1,10):
        print(i)
        page= str(i)
        api_data= "https://api.adzuna.com/v1/api/jobs/au/search/"+page+"?app_id=4cb38e73&app_key=ca142ad047eb88bae578bdca2a3eef4f&where=victoria&results_per_page=50&&content-type=application/json"
        data=requests.get(api_data)
        dict = json.loads(s=data.text)
        ls.append(list(dict['results']))
    #going in each list one by one
    for i in ls:
        print ("list number",i)
        for j in range (0,len(i)):
            #print ("index",j)
           # print (i[j])

            if len(i[j]['location']['area'])>3 and (i[j]['location']['area'][1]=="Victoria") and 'display_name' in i[j]['company'] and "Region" in i[j]['location']['area'][2] and \
                    i[j]['category']['label'] != "PR, Advertising & Marketing Jobs" and \
                    i[j]['category']['label'] != 'Hospitality & Catering Jobs' and \
                    i[j]['category']['label'] != 'Part time Jobs' and \
                    i[j]['category']['label'] != 'Unknown' and \
                    i[j]['category']['label'] != 'Property Jobs' and \
                    i[j]['category']['label'] != 'Customer Services Jobs':
                print (i[j]['location']['area'][2])
                if "," in i[j]['title']:
                    title=i[j]['title']
                    title=title.split(',')
                    print ("discard")
                    jobs.append(i[j]['category']['label'] +','+ i[j]['location']['area'][3] +','+ title[0]+ ','+ i[j]['location']['area'][2] +','+ i[j]['company']['display_name']+','+ i[j]['redirect_url']+ ','+ str(i[j]['id']))
                else:
                   jobs.append(i[j]['category']['label'] +','+ i[j]['location']['area'][3] +','+ i[j]['title']+ ','+ i[j]['location']['area'][2] +','+ i[j]['company']['display_name']+','+ i[j]['redirect_url']+ ','+ str(i[j]['id']))

    with open('api_data.txt', 'w', encoding='utf-8') as filehandle:
        for listitem in jobs:
            filehandle.write('%s\n' % listitem)
    filehandle.close()


    loc=["Melbourne Region","Geelong Region","La Trobe Region","Bendigo Region","Shepparton Region","Ballarat Region","Mildura Region",
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


def main():
    fetch_all()

if __name__ == "__main__":
    main()



