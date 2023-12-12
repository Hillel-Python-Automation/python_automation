# 8. Використайте прикріплений файл json та прочитайте його за допомогою модулю json.
import json

with open("sample2.json", "r") as json_file:
    content = json.load(json_file)
    print(content)
