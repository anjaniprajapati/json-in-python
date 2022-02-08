import json 
a=["neelam","programer","24","2400",]
b=["komal","trainer","24","20000"]
c=["anuradha","HR","25","40000"]
d=["Abhishek","manager","29","63000"]
l=[a,b,c,d]
l1=["name","Designatio","age","salary"]
l2=["emp1","emp2","emp3","emp4"]
dict={}
i=0
while i<len(l):
    d={}
    j=0
    while j<len(l[i]):
        if j==0:
            x=l1[j]
            y=l[i][j]
            d[x]=y
        elif j==1:
            x1=l1[j]
            y1=l[i][j]
            d[x1]=y1
        elif j==2:
            x2=l1[j]
            y2=l[i][j]
            d[x2]=y2
        else:
            x3=l1[j]
            y3=l[i][j]    
        j+=1
    t=l2[i]
    dict[t]=d   
    i+=1
js_ob=json.dumps(dict,indent=6)
print(js_ob)

out_file=open("que_8.json","w")
json.dump(dict,out_file,indent=6)
out_file.close()