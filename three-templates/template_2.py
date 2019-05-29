import pystache
import os

def get_model():
    return {
        "charts": [
            {
                "divId": "#reportPlaceholder1",
                "title": "За второе полугодие - сводный",
                "sourceUrk": "/reports/data/0",
                "series": [
                    {"dataIndex": 0, "title": "Доходы", "color": "green"},
                    {"dataIndex": 1, "title": "Расходы", "color": "red"},
                ]
            },
            {
                "divId": "#reportPlaceholder2",
                "title": "За второе полугодие - по продуктам",
                "sourceUrk": "/reports/data/1",
                "series": [
                    {"dataIndex": 0, "title": "Hello Kitty", "color": "#000"},
                    {"dataIndex": 1, "title": "PokemonGo", "color": "#111"},
                    {"dataIndex": 2, "title": "Mustache", "color": "#222"},
                ]
            }

        ]
    }


model = get_model()

with open(os.path.join("templates", "report.js.mustache"), 'r') as f:
    template = f.read()

js = pystache.render(template, model)
print(js)
