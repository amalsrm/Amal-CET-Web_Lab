import pymongo
url="mongodb://localhost:27017/"
s=pymongo.MongoClient(url)
db=s['exam']
coll=db['Student']

data=[{"_id":1,"name":"Anjali","place":"Kollam","phone":8582639562,"vaccination_status":"Both vaccinated","RTPCR":"negative","Lab_mark":{"Internal":30,"External":45},"Department":"MCA"},{"_id":2,"name":"Anuradha","place":"Varkala","phone":9992639562,"vaccination_status":"Both vaccinated","RTPCR":"negative","Lab_mark":{"Internal":40,"External":48},"Department":"Civil"},
{"_id":3,"name":"Bismiya","place":"Kollam","phone":9446639562,"vaccination_status":"not vaccinated","RTPCR":"positive","Lab_mark":{"Internal":50,"External":39},"Department":"MCA"},
{"_id":4,"name":"Vimal","place":"Ernakulam","phone":8582639568,"vaccination_status":"First dose only","RTPCR":"positive","Lab_mark":{"Internal":40,"External":42},"Department":"Civil"},
{"_id":5,"name":"Vivek","place":"Kollam","phone":8582639777,"vaccination_status":"Both vaccinated","RTPCR":"negative","Lab_mark":{"Internal":50,"External":50},"Department":"MCA"}]
coll.insert_many(data)
for x in coll.find({"vaccination_status":"not vaccinated"},{"name":1,"phone":1}):
	print(x["name"]+"\n"+str(x["phone"]))
for x in coll.find({"Department":"MCA"}).sort("Lab_mark.External",-1).limit(2):
	print(x["name"]+"\n"+str(x["phone"]))
for x in coll.find({"name":{"$regex":"^A"}}):
	print(str(x["_id"])+"\n"+x["name"]+"\n"+x["Department"])
mysql={"_id":4}
update={"$set":{"vaccination_status":"Both vaccinated"}}
coll.update_one(mysql,update)

for x in coll.find().sort("Lab_mark.External",-1):
	print(x["name"])
