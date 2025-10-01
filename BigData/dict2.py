thisDict = {
	"name": "Jason",
	"surname": "Rossi",
	"active": True,
	"favouriteNumber": 54,
	"birthday": {
		"day": 1,
		"month": 1,
		"year": 2000
	},
	"languages": [ "it", "en" ]
}
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
# print(type(thisDict))
# for chiave, valore in thisDict.items():
#     print(chiave, valore)
 
for x, y in myfamily.items():
    # print(x, y)
    for t, p in y.items():
        print(t, p)   