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


# SQL CASE Anti-pattern
class SqlAntipattern(object):
    def render(self, m):
        if m["typeList"]:
            return self.render_typelist(m)
        if m["typeCountGroupBy"]:
            return self.render_groupby(m)

        raise Exception("Unknown query type")

    def render_where(self, m):
        sql = "WHERE "

        def eqtion(w):
            return "{}={}{}{}".format(
                w["field"],
                "'" if "quot" in w else "",
                w["eq_val"],
                "'" if "quot" in w else "")

        wheres = [eqtion(w) for w in m["where"]]
        sql += ", ".join(wheres)
        return sql + " "

    def render_orderby(self, m):
        return "ORDER BY " + m["orderBy"]

    def render_typelist(self, m):
        sql = "SELECT * FROM " + m["tableName"] + " "
        if "hasWhere" in m:
            sql += self.render_where(m)

        if "orderBy" in m:
            sql += self.render_orderby(m)

        if "limit" in m:
            sql += " LIMIT " + m["limit"]

        return sql

    def render_groupby(self, m):
        sql = "SELECT " + m["groupColumn"]
        sql += ", COUNT(*) FROM " + m["tableName"] + " "
        sql += " GROUP BY " + m["groupColumn"]

        return sql


model = get_model_1()
with open(os.path.join("templates", "query.sql.mustache"), 'r') as f:
    template = f.read()

sql = pystache.render(template, model)
print(sql)


print("-- CODE-BASED RENDERING")
sql = SqlAntipattern().render(model)
print(sql)
print("-- CODE-BASED RENDERING END")



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

