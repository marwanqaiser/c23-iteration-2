import  json,requests
import time

def fetch_all():

    # gets everything in the top 10 pages from the API in 10 requests in Victoria
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
            print ("index",j)
            print (i[j])

            if len(i[j]['location']['area'])>3 and (i[j]['location']['area'][1]=="Victoria") :
                jobs.append(i[j]['category']['label'] +','+ i[j]['location']['area'][3] +','+ i[j]['title'])

    with open('api_data.txt', 'w') as filehandle:
        for listitem in jobs:
            filehandle.write('%s\n' % listitem)
    filehandle.close()



def main():
    fetch_all()

if __name__ == "__main__":
    main()



