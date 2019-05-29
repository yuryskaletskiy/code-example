import pystache
import os


def get_model_1():
    return {
        "typeList": True,
        "tableName": "hosts",
        "hasWhere": True,
        "where": [
            { "field": "firmware_id", "eq_val": "1", "comma": True},
            { "field": "bmc_login", "eq_val": "admin", "quot": True},
        ],
        "orderBy": "ip DESC"
    }

def get_model_2():
    return {
        "typeList": True,
        "tableName": "hosts",
        "orderBy": "name",
        "limit": 3
    }

def get_model_3():
    return {
        "typeCountGroupBy": True,
        "tableName": "hosts",
        "groupColumn": "host_type_id"
    }


model = get_model_1()
with open(os.path.join("templates", "query.sql.mustache"), 'r') as f:
    template = f.read()

sql = pystache.render(template, model)
print(sql)

model = get_model_2()
with open(os.path.join("templates", "query.sql.mustache"), 'r') as f:
    template = f.read()

sql = pystache.render(template, model)
print(sql)

model = get_model_3()
with open(os.path.join("templates", "query.sql.mustache"), 'r') as f:
    template = f.read()

sql = pystache.render(template, model)
print(sql)

