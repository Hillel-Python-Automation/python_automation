# 7. Використайте прикріплений файл csv та прочитайте його за допомогою модулю csv.
import csv

with open("input_data.csv") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)




