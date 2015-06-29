from application import db

def get_cre_info(mdref):

    passed_sql = "select a.code, template from cre a join mdref b on a.code = b.code where b.mdref ='" + mdref + "'"
    passed_res = db.engine.execute(passed_sql)
    crelist = {"cres" : []}
    for row in passed_res:
        cre = {}
        cre["code"] = row.code
        cre["template"] = row.template

        crelist["cres"].append(cre)

    return crelist
