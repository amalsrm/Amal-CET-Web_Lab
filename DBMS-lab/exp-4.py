
import pymongo
url="mongodb://localhost:27017/"
s=pymongo.MongoClient(url)
db=s["College"]
coll=db["Stud_list"]
for x in coll.find({"gender":"female","course":"MCA"},{"name":1,"_id":0,"mark":1}):
	print(x)
print("\n.....................................................\n")
for x in coll.find({"course":"MCA"}).sort("mark",-1).limit(1):
	print('\n'+x["name"]["fname"]+" "+x["name"]["lname"])
	print(x["address"]["house_name"]+" "+x["address"]["city"])
	print(x["gender"]+'\n'+x["course"]+'\n'+str(x["mark"])+'\n'+x["grade"])
print("\n.....................................................\n")
for i in coll.find({"gender":"male","grade":"A+"}):
	print('\n'+i["name"]["fname"]+" "+i["name"]["lname"])
print("\n......................................................\n")
for x in coll.find({"course":"Mechanical"}).sort("mark",-1).limit(3):
	print('\n'+x["name"]["fname"]+" "+x["name"]["lname"])
print("\n.....................................................\n")
for x in coll.find({"gender":"female","mark":{"$gt": 90}}):
	print('\n'+x["name"]["fname"]+" "+x["name"]["lname"])
	print(x["address"]["house_name"]+" "+x["address"]["city"])
	print(x["gender"]+'\n'+x["course"]+'\n'+str(x["mark"])+'\n'+x["grade"]+'\n'+str(x["phone"]["no"]))
print("\n......................................................\n")
for x in coll.find({"gender":"female","mark":{"$lt": 90,"$gt":80}}):
	print('\n'+x["name"]["fname"]+" "+x["name"]["lname"])
	print(x["address"]["house_name"]+" "+x["address"]["city"])
	print(x["gender"]+'\n'+x["course"]+'\n'+str(x["mark"])+'\n'+x["grade"]+'\n'+str(x["phone"]["no"]))
print("\n.......................................................\n")
for x in coll.find({"name.fname":{"$regex":"^D"}}):
	print('\n'+x["name"]["fname"]+" "+x["name"]["lname"])
	print(x["address"]["house_name"]+" "+x["address"]["city"])
	print(x["gender"]+'\n'+x["course"]+'\n'+str(x["mark"])+'\n'+x["grade"]+'\n'+str(x["phone"]["no"]))
print("\n........................................................\n")
for x in coll.find({"address.city":"Kollam"}):
	print('\n'+x["name"]["fname"]+" "+x["name"]["lname"])
	print(x["address"]["house_name"]+" "+x["address"]["city"])
	print(x["gender"]+'\n'+x["course"]+'\n'+str(x["mark"])+'\n'+x["grade"]+'\n'+str(x["phone"]["no"]))
print("\n........................................................\n")
for x in coll.find({"$nor":[{"address.city":"Kollam"},{"address.city":"Thiruvananthapuram"}]}):
	print('\n'+x["name"]["fname"]+" "+x["name"]["lname"])
	print(x["address"]["house_name"]+" "+x["address"]["city"])
	print(x["gender"]+'\n'+x["course"]+'\n'+str(x["mark"])+'\n'+x["grade"]+'\n'+str(x["phone"]["no"]))
print("\n.........................................................\n")
for x in coll.find({"address.city":{"$in":["Kollam","Thiruvananthapuram"]},"gender":"female"}):
	print('\n'+x["name"]["fname"]+" "+x["name"]["lname"])
	print(x["address"]["house_name"]+" "+x["address"]["city"])
	print(x["gender"]+'\n'+x["course"]+'\n'+str(x["mark"])+'\n'+x["grade"]+'\n'+str(x["phone"]["no"]))
