from application import db

def get_cre_info(mdref):

    passed_sql = "select a.code, a.infills, template, restriction_name from cre a join mdref b on a.code = b.code where b.mdref ='" + mdref + "'"
    passed_res = db.engine.execute(passed_sql)
    crelist = {"cres" : []}
    for row in passed_res:
        cre = {}
        cre["code"] = row.code
        cre["template"] = row.template
        cre["infills"] = row.infills
        cre["restriction_name"] = row.restriction_name

        crelist["cres"].append(cre)

    return crelist
