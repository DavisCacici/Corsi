thisDict = {
    "Nome": "Pippo",
    "Cognome": "Pluto",
    "Età": 78,
    "Età": 87
}

print(thisDict["Nome"])
thisDict["Nome"] = "Stefano"
print(thisDict["Nome"])
thisDict["Città"] = "Ravenna"
print(thisDict)
print(len(thisDict))
print(thisDict.get("Città"))
thisDict.update({"color": "red"})
print(thisDict['color'])
thisDict.update({"color": "yellow"})
print(thisDict.get("color"))
thisDict.pop('Città')
print(thisDict)
thisDict.popitem()
print(thisDict)
del thisDict["Età"]
print(thisDict)
thisDict.clear()
print(thisDict)
