# ©  2008-2021 Deltatech
# See README.rst file on addons root folder for license details


{
    "name": "Expenses Deduction",
    "summary": "Expenses Deduction & Disposition of Cashing",
    "version": "16.0.2.0.0",
    "category": "Accounting & Finance",
    "author": "Terrabit, Dorin Hongu",
    "website": "https://www.terrabit.ro",
    "depends": [
        "l10n_ro",
        "account",
        "product",
        "deltatech_partner_generic",
        # "deltatech_payment_to_statement",
    ],
    "license": "OPL-1",
    "data": [
        "views/deltatech_expenses_deduction_view.xml",
        "views/deltatech_expenses_deduction_report.xml",
        "views/report_expenses.xml",
        "views/account_journal_view.xml",
        "security/ir.model.access.csv",
        "security/security.xml",
        "data/data.xml",
    ],
    "images": ["images/main_screenshot.png"],
    "development_status": "Mature",
    "maintainers": ["dhongu"],
}
