import json
python_obj={
    "name": "David", 
    "class": "I", 
    "age": 6
}
json_obj= json.dumps(python_obj)
print("\nJSON DATA\n")
print(json_obj,"\n")