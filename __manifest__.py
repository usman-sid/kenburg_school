# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Ken Burg School System',
    'version': '18.0.1.0',
    'author': 'Usman Siddique',
    'sequence': -103,
    'category': 'School Management System',
    'summary': 'To Manage All Records of School',
    'description': """School Management System""",
    'depends': ['website', 'base', 'portal'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/school_record_wizard_view.xml',
        'views/teacher_view.xml',
        'views/student_view.xml',
        'views/record_view.xml',
        'views/res_company.xml',
        'views/teacher_template.xml',
        'views/portal_teacher_detail.xml',
        #'views/website_menu.xml',
        'views/menu.xml',
        'report/teachers_report_view.xml',
        'report/teachers_report_template.xml',
    ],
    'demo': [],
    'installable': True,
    'assets': {},
    'license': 'LGPL-3',
}
