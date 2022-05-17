import json
json_str = open("country.json", 'r').read()
json_obj = json.loads(json_str)
# print(json_obj)
out_obj = json.dumps(json_obj, indent=4)
print(out_obj)
