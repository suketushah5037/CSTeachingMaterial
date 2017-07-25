#Write and read from files
f = open("file.txt","w") 
f.write("Hello World")
f.close()
f = open("file.txt","r")
data = f.read()
print(data)
f.close()


newlist = []
#add first item
newdict = {}

newdict['rank'] = 1
newdict['name'] = "Carl"

newlist.append(newdict)

#add second item
newdict = {}

newdict['rank'] = 100
newdict['name'] = "Ajith"

newlist.append(newdict)
print(newlist)


#JSON format
#[{"rank": 1, "name": "Anna"}, {"rank": 100, "name": "Joshua"}]

#sorting with your own fuction

def sortbyrank(element):
    return element['name']

#Sort using a key - sortbyrank is the name of the function that we write 
newlist.sort(key=sortbyrank)

print("sorted list")
print(newlist)
