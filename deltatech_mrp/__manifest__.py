# ©  2008-2019 Deltatech
# See README.rst file on addons root folder for license details

{
    "name": "MRP Extension",
    "summary": "MRP Extension - Obsolete",
    "version": "16.0.1.0.2",
    "author": "Terrabit, Dorin Hongu",
    "license": "OPL-1",
    "website": "https://www.terrabit.ro",
    "category": "Generic Modules/Production",
    "depends": ["base", "mrp", "stock", "sale", "product"],
    "data": [
        "views/mrp_view.xml",
        "report/deltatech_mrp_report.xml",
        "views/product_view.xml",
        "security/ir.model.access.csv",
        "security/security.xml",
    ],
    "images": ["images/main_screenshot.png"],
    "installable": True,
    "development_status": "Beta",
    "maintainers": ["dhongu"],
}
