from __future__ import print_function 
import requests
from bs4 import BeautifulSoup as bs
import json
# r = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Tunis,tn&appid=21f75fcefb73c7e7bd396a9b0a9b80e8");
# print r.content
data = {"attributesToSearch":["title","company.name","tags","summary","description","location.name"],"parser":"source","page":"1","hitsPerPage":10,"sortBy":"updated_at","sortOrder":"desc","facets":[{"field":"salary_min","type":"min"},{"field":"salary_max","type":"max"},{"field":"job_type.name.full","type":"terms"},{"field":"company.name.full","type":"terms"},{"field":"category.name.full","type":"terms"},{"field":"location.name.full","type":"terms","size":0},{"field":"tags.full","type":"terms"}],"term":"stage","domain_company":1}
r = requests.post("https://tungolia.jobi.tn/filter/joboffer",json=data);
# soup = bs(r.content)
# weatherInfo = json.loads(r.content)
# for element in weatherInfo: 
#     print element, weatherInfo[element]

result = json.loads(r.text)
# for element in result["facets"]:
#     print element
# print result["hits"]
# for e in result["hits"]:
#     print e["description"].encode('ascii', 'ignore').decode('ascii')
#     print """-------------------------------------------------------------------------------------------\n-------------------------------------------------------------------------------------------"""
        # print e[el]
# for el in result["hits"]:
#     for e in el :
#         print e
print ("[")
for el in result["hits"]:
    print  ('{"category" : "', el['category']['name'].encode('ascii', 'ignore').decode('ascii'),end='')
    print  ('","release_date" :"', el['release_date'],end='')
    print  ('","location" : "', el['location'][ 'name'],end='')
    print  ('","title" : "', el['title'].encode('ascii','ignore').decode('ascii'),end='') 
    print  ('","description" : "', el['description'].replace("\n","\\n").replace('\r', '').replace('"',"'").encode('ascii','ignore').decode('ascii'),end='')
    print  ('","company" : "', el['company']['name'],end='')
    print  ('","slug" : "', el['slug'] ,end='')
    print  ('"},')
print ("{}]")