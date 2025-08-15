from odoo import api, fields, models


class SchoolRecord(models.Model):
    _name = "school.record"
    _description = "School Records"
    _rec_name = "student_id"

    student_id = fields.Many2one('school.student', string='Students', tracking=True)
    father_name = fields.Char(related='student_id.father_name')
    student_age = fields.Char(related='student_id.student_age')
    student_gender = fields.Selection(related='student_id.student_gender')
    student_class = fields.Char(related='student_id.student_class')
    city = fields.Selection(related='student_id.city')
    contact = fields.Char(related='student_id.contact')
    remarks = fields.Html(string='Remarks')
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'very High'), ], string='Priority')

    teacher_id = fields.Many2one('school.teacher', string='Teachers')
