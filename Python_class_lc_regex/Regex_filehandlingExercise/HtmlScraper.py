#Assignment
#HTML file has the ranks for the most common names for boys and girls separately for a specific year
#Read the html file for the year and all the names and the ranks using regex
#Combine the names and ranks together in a dictionary and add them to a separate list that mixes boys and girls
#Sort them in alphabetic order of the name
#Create a json text and write the sorted list with ranks in the file

import re

#open the file
#modes: r, w, a, r+
babynames_1990 = open("C:\\Users\\Gowri\\Desktop\\CG\\Python_Course\\google-python-exercises\\babynames\\baby1990.html", "r")

#reads the entire file
# - read and readline available
#another syntax
#with open"("file.txt") as f: data = f.read()
data = babynames_1990.read()
#print(data)

#pythex.org - to check your regex
#important flags - ignorecase, multiline(^ and $ match newline also), dotall (. matches the newline), 
regExMatches = re.search('Popularity\sin\s(\d{4})', data)

#print(regExMatches)
#Grouping
print(regExMatches.group(1))

#* is 0 or more, ? is 0 or 1, and + is 1 or more
#findall to find all the matches
regExMatches = re.findall('<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', data)

#print(len(regExMatches))
#tuple of all the three groups
#print(regExMatches[0][1])
#print(regExMatches[0])
#print(regExMatches[0])

#Order them alphabetically
#ignore boy and girl names, mix them up

#New list
newlist = []

for i in range(len(regExMatches)):
    newdict = {}
    newdict['rank'] = regExMatches[i][0]
    newdict['name'] = regExMatches[i][1]
    newlist.append(newdict)
    newdict = {}
    newdict['rank'] = regExMatches[i][0]
    newdict['name'] = regExMatches[i][2]
    newlist.append(newdict)
    #print(newlist)
    #newlist.append(regExMatches[i][1])
    #newlist.append(regExMatches[i][2])

babynames_1990.close()    
#print(len(newlist))
#print(newlist)

##print(newlist[0])
##print(newlist[1])
##print(newlist[2])
##print(newlist[3])

def getName(element):
    return element['name']

print(len(newlist))

#sort the list according to the name
newlist.sort(key=getName)

##print(newlist[0])
##print(newlist[1])
##print(newlist[2])
##print(newlist[3])

#JSON format
#[{"rank": 1, "malename": "Joshua", "femalename": "Anna"}, {"rank": 1, "malename": "Joshua", "femalename": "Anna"}]

#write to the file in json format, do not forget to escape the quotes
babynames_1990_sorted = open("json_1990.json", "w")
babynames_1990_sorted.write("[")

for i in range(len(newlist)):
    jsonstring = "{\"rank\":" + newlist[i]['rank'] + ", \"name\":" + "\"" + newlist[i]['name'] + "\"" + "}"
    #print(jsonstring)
    #do not put a commma for the 1999th item
    if (i < 1999):
        jsonstring = jsonstring + ", "
    babynames_1990_sorted.write(jsonstring)

babynames_1990_sorted.write("]")
babynames_1990_sorted.close()
#close the file
