import json

# Print Dictionary
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x ,y in thisdict.items():
  print(x,y)

# Copy Dictionary
copyDic = thisdict.copy()
print("Copy: ", copyDic)

# Complex

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)

# Print as JSON
print(json.dumps(myfamily,))

