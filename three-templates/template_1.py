import pystache
import os


def add_comma(list):
    for a in list[:-1]:
        a["comma"] = True


def get_model():
    res = {
        "documentId": 3323223,
        "checkDate": "01.02.2019 22:20",
        "posId": 34399,
        "posAddr": "Urupinsk, 1 Maya 1",
        "lines": [
            {
                "no": 1,
                "itemtext": "Hello Kitty",
                "amount": 3,
                "sumRub": "55.20"
            },
            {
                "no": 2,
                "itemtext": "Paper pokemons",
                "amount": 1,
                "sumRub": "1230.00"
            },
            {
                "no": 2,
                "itemtext": "Book of Mustache",
                "amount": 1,
                "sumRub": "1000.00"
            }
        ],
        "total": {
            "amount": "3285.20"
        }
    }
    add_comma(res["lines"])
    res["posInUrupinsk"] = res["posId"] > 34000

    return res


model = get_model()

with open(os.path.join("templates", "check.txt.mustache"), 'r') as f:
    template = f.read()

check_text = pystache.render(template, model)
print(check_text)
