import json
json_str = '{"Name":"Harshit Verma","Age":22,"Roll no.":1884110027,"Degree":"B.tech"}'
json_obj = json.loads(json_str)
print(json_str)
print(type(json_obj))
out_str = json.dumps(json_obj, indent=4, sort_keys=False,
                     separators=('.', '='))
print(out_str)
