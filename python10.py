"""
#
# Part: Python JSON
# API = Application Programming Interface 
#
"""

import json

# make a json String(Dictionary String)
x = '{"name": "John", "age": 20, "city": Phuket"}'

"""
# parse 
y=json.loads(x)

# python Dictionary
print(y)
print(type(y))
print(y["city"])
"""

#python dictionary
a = {
    "name": "Noa",
    "age": 20,
    "city": "Phuket"
}

# convert ot JSON (String)
b = json.dumps(a)

# JSON String
print(b)
