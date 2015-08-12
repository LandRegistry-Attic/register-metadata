from application import db

def get_cre_info(mdref):

    passed_sql = "select a.code, a.infills, template, restriction_name, \
    a.sub_role_code, c.entry_role_code, d.reg_child_code \
    from cre a join mdref b on a.code = b.code \
    join subrole c on a.sub_role_code = c.sub_role_code \
    join role d on c.entry_role_code = d.entry_role_code where b.mdref ='" + mdref + "'"
    passed_res = db.engine.execute(passed_sql)
    crelist = {"cres" : []}
    for row in passed_res:
        cre = {}
        cre["code"] = row.code
        cre["template"] = row.template
        cre["infills"] = row.infills
        cre["restriction_name"] = row.restriction_name
        cre["sub_role_code"] = row.sub_role_code
        cre["entry_role_code"] = row.entry_role_code
        cre["reg_child_code"] = row.reg_child_code

        crelist["cres"].append(cre)

    return crelist
