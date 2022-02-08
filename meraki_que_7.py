# import json 
# f_name="Text.txt"
# d1={}
# with open(f_name) as df:
#     for line in df:
#         k,v=line.strip().split(None,True)
#         d1[k]=v.split()
# out_f1=open("Test.json","w")
# json.dump(d1,out_f1,indent=6,sort_keys=False)
# out_f1.close()


import json 
f_name="Text.txt"
d1={}
with open(f_name) as df:
    for line in df:
        key,values=line.strip().split(None,True)
        d1[key]=values
out_f1=open("Anjani.json","w")
json.dump(d1,out_f1,indent=10,sort_keys=False)
out_f1.close()


