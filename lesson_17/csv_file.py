import csv

# REad CSV file
with open('DataManipulation.csv') as dm:
    data = csv.reader(dm)
    for line in data:
        print(line)
        print(type(line))

# Read CSV file as a dictionary (if the file has names of the columns)
with open('DataManipulation.csv') as dm:
    data = csv.DictReader(dm)
    for line in data:
        print(line)
        print(type(line))

# Read CSV file with encoding different than utf-8
with open('SampleCSVFile.csv', encoding='cp1252') as sf:
    data = sf.readlines()
    for line in data:
        print(line)

# Read CSV file with encoding different then utf-8 (ignoring errors)
with open('SampleCSVFile.csv', errors='ignore') as sf:
    data = sf.readlines()
    for line in data:
        print(line)

# 1,"Eldon Base for stackable storage shelf, platinum",Muhammed MacIntyre,3,-213.25,38.94,35,Nunavut,
# Storage & Organization,0.8
field_names = ['id', 'description', 'name', 'dig1', 'dig2', 'dig3', 'dig4', 'str1', 'str2', 'dig5']

# Read CSV as a dictionary (first row become the keys for the rest of the rows)
with open('SampleCSVFile.csv', encoding='cp1252') as sf:
    data = csv.DictReader(sf)
    for line in data:
        print(line)

# Read CSV as a dictionary with given columns names
with open('SampleCSVFile.csv', encoding='cp1252') as sf:
    data = csv.DictReader(sf, fieldnames=field_names)
    for line in data:
        print(line)


