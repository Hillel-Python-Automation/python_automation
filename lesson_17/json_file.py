import json

### Dictionary to JSON
data = {
    'name': 'John',
    'age': 30,
    'city': "New York"
}
print(type(data))
json_string = json.dumps(data)
print(json_string)
print(type(json_string))

json_string2 = json.dumps(data, indent=2)
print(json_string2)

### JSON string to JSON Object
json_object = json.loads(json_string)
print(type(json_object))
print(json_object)

json_str = '{"name": "John", "age": 30, "city": "Sacramento"}'
json_obj = json.loads(json_str)
print(type(json_obj))
print(json_obj)

print(json_obj['city'])
print(json_obj['age'])
print(json_obj['name'])

json_to_write = None

## Read JSON from file
with open("sample.json") as sj:
    data = json.load(sj)
    print(type(data))
    print(data)
    print(json.dumps(data, indent=2))
    json_to_write = data


## Write JSON to file
with open('sample_w.json', 'w') as sjw:
    json.dump(json_to_write, sjw, indent=4)

with open('sample_wj.json', 'w') as sjw:
    sjw.write(json.dumps(json_to_write))

