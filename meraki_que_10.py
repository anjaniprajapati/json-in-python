# import json 
# languages=["english","hindi","tamil","gujrati","bengali","english","english","gujrati","marathi","bengali","hindi","hindi","hindi"]		
# i=0;d={} ; l1=[]
# count1=0;count2=0;count3=0;count4=0;count5=0;count6=0
# while i <len(languages):
# 	if languages[i] not in l1:
# 		l1.append(languages[i])
	
# 	if languages[i]=="english":
# 		count1+=1
# 	if languages[i]=="hindi":
# 		count2+=1
# 	if languages[i]=="tamil":
# 		count3+=1
# 	if languages[i]=="gujrati":
# 		count4+=1
# 	if languages[i]=="bengali":
# 		count5+=1
# 	if languages[i]=="marathi":
# 		count6+=1	
# 	i+=1
# l=[count1,count2,count3,count4,count5,count6]
# b=l1
# py_ob=dict(zip(b,l))
# json_ob=json.dumps(py_ob,indent=6)
# print(json_ob)


import json 
languages=["english","hindi","tamil","gujrati","bengali","english","english","gujrati","marathi","bengali","hindi","hindi","hindi"]		
i=0;dic={} ; l1=[]
count1=0;count2=0;count3=0;count4=0;count5=0;count6=0
while i <len(languages):
	if languages[i] not in l1:
		l1.append(languages[i])
	
	if languages[i]=="english":
		count1+=1
	if languages[i]=="hindi":
		count2+=1
	if languages[i]=="tamil":
		count3+=1
	if languages[i]=="gujrati":
		count4+=1
	if languages[i]=="bengali":
		count5+=1
	if languages[i]=="marathi":
		count6+=1	
	i+=1
l=[count1,count2,count3,count4,count5,count6]
j=0
while j<len(l):
    dic[l1[j]]=(l[j])
    j+=1
json_ob=json.dumps(dic,indent=6)
print(json_ob)