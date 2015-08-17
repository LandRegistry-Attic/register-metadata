import json

def get_cre_response():
  return  {
    "cres": [
        {
            "infills": "CD",
            "code": "CD100",
            "sub_role_code": "RC12",
            "restriction_name": "",
            "entry_role_code": "CCHA",
            "reg_child_code": "C",
            "template": "REGISTERED CHARGE dated *CD*."
        },
        {
            "infills": "CDCP",
            "code": "BX102",
            "sub_role_code": "BRES",
            "restriction_name": "",
            "entry_role_code": "CBCR",
            "reg_child_code": "B",
            "template": "RESTRICTION: No disposition of the registered estate by the proprietor of the \
            registered estate is to be registered without a written consent signed by the proprietor for \
            the time being of the Charge dated *CD* in favour of *CP* referred to in the Charges Register."
        },
        {
            "infills": "",
            "code": "CALHL",
            "sub_role_code": "CHAE",
            "restriction_name": "Abbey Life Home Loans Limited",
            "entry_role_code": "CCHR",
            "reg_child_code": "C",
            "template": "Proprietor: #ABBEY LIFE HOME LOANS LIMITED# (Co. Regn. No. 1945802) care of Mortgage \
            Systems Limited, Flagship House, Reading Road North, Fleet, Hants. GU13 8YA."
        },
        {
            "infills": "CDOO",
            "code": "CK300",
            "sub_role_code": "COFA",
            "restriction_name": "",
            "entry_role_code": "COFA",
            "reg_child_code": "C",
            "template": "The proprietor of the Charge dated *CD* *O<>O* referred to above is under an obligation \
            to make further advances. These advances will have priority to the extent afforded by section 49(3) \
            Land Registration Act 2002."
        }
    ]
}
