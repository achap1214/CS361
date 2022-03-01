import json

with open('stockprices.json', 'r') as f:
    jsonData = f.read()
    data = json.loads(jsonData)

while True:
    with open('C:\CS361\Flask_App\symbolprice.txt', 'r') as f:
        symbol = f.read()
    if '$' not in symbol:
        with open('C:\CS361\Flask_App\symbolprice.txt', 'w') as f:
            for key in data:
                if key == symbol:
                    f.write("$" + str(data[key]))
