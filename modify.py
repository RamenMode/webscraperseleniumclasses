import json

lenClasses = 3629
f = open('NotreDameClasses.json')
data = json.load(f)

print("Break")
a = []
for i in range(lenClasses):
    a.append(f"{i}")

#datainTextJson = {
#"id": [],
#"class": []
#}

#for id in a:
 #   datainTextJson["id"].append(id)
#for course in data:
 #   datainTextJson["class"].append(course)

datainTextJson = []

for x in range(lenClasses):
    datainTextJson.append({})

for i in range(lenClasses):
    datainTextJson[i] = {"id": a[i], "class": data[i]}

print(datainTextJson)
datainJson = json.dumps(datainTextJson)

with open("NotreDameClasses.json", "w") as outfile:
    outfile.write(datainJson)
