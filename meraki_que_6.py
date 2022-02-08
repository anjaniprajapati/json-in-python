import json 
dic='{"a":1,"a": 2,"a": 3,"a": 4,"b": 1, "b": 2}'
py_ob=json.loads(dic)
print("\nOriginal Python object:-\n")
print(dic)
print("\nUnique Key in a JSON objec:-\n")
print(py_ob)