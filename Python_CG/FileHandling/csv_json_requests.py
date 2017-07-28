#imports for reading from csv and json and from the filesystem
import csv
import os
import json

#create a directory called "Remove"
os.makedirs('Remove', exist_ok=True)

#Read data from csv.csv, put it into a list, and write row by row into output.csv and 
#output.txt (tab separated), row by row, in append mode
#Reading from a CSV file
exampleFile = open('csv.csv')
#instead of a simple read, we use csv.reader to read from csv files
#simple read also will achieve the same purpose but the interface will
#not be tuned for reading from csv files alone but for files in general
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)

print(exampleData)


#Writing into a CSV file
#Two files for showing how to use with a different delimiter

outputFile = open('output.csv', 'a', newline='')
#since it is not comma separated, it is a ".txt"
outputFile1 = open('output.txt', 'a', newline='')

outputWriter = csv.writer(outputFile)
outputWriter1 = csv.writer(outputFile1, delimiter='\t', lineterminator='\n\n')
#outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])


for row in exampleData:
    outputWriter.writerow(row)
    outputWriter1.writerow(row)

#close after writing all
outputFile.close()
outputFile1.close()
exampleFile.close()

#Pick up all .csv files from the current directory, open it, skip the first row,
#add the rest of the rows in a list, write the list contents to a
#files with the same name but in a new directory called "Remove"
for csvFilename in os.listdir('.'):
       if not csvFilename.endswith('.csv'):
            continue    # skip non-csv files

       print('Removing header from ' + csvFilename + '...')

       # TODO: Read the CSV file in (skipping first row).
        # Read the CSV file in (skipping first row).
       csvRows = []
       csvFileObj = open(csvFilename)
       readerObj = csv.reader(csvFileObj)
       for row in readerObj:
           if readerObj.line_num == 1:
                continue    # skip first row
           csvRows.append(row)
       csvFileObj.close()
       # TODO: Write out the CSV file.
       csvFileObj = open(os.path.join('Remove', csvFilename), 'w',
                    newline='')
       csvWriter = csv.writer(csvFileObj)
       for row in csvRows:
           csvWriter.writerow(row)
       csvFileObj.close()

#Read from a JSON file
import json
print("json")
stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0,"felineIQ": null}'

jsonDataAsPythonValue = json.loads(stringOfJsonData)
print("json string as json data")
print(jsonDataAsPythonValue)

#dump into json
pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie',
'felineIQ': None}
print("python dictionary as json data")
stringOfJsonData2 = json.dumps(pythonValue)
print(stringOfJsonData2)


#get data from web site
#need pip install for it
import json, requests, sys
# Compute location from command line arguments.
##if len(sys.argv) < 2:
##    print('Usage: quickWeather.py location')
##    sys.exit()
##location = ' '.join(sys.argv[1:])

#hardcode location

#if we dont have weather data from a website, use the weatherdata.json and parse

# Download the JSON data from OpenWeatherMap.org's API.
#http://samples.openweathermap.org/data/2.5/forecast?id=524901&appid=b1b15e88fa797225412429c1c50c122a1
url ='http://samples.openweathermap.org/data/2.5/forecast?id=524901&appid=b1b15e88fa797225412429c1c50c122a1'
response = requests.get(url)
response.raise_for_status()

#response holds a large json text
weatherData = json.loads(response.text)
w = weatherData['list']
print('Current weather in %s:'.format('my city'))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
