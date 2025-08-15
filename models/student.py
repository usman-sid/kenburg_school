from datetime import date
from odoo import api, fields, models


class SchoolStudent(models.Model):
    _name = "school.student"
    _rec_name = "student_name"
    _description = "School Students"

    student_name = fields.Char(string='Student Name', required=True)
    father_name = fields.Char(string="Fathers Name")
    date_of_birth = fields.Date(string='Student DOB')
    student_age = fields.Char(string='Students Age', compute='_compute_age')
    student_gender = fields.Selection([('male', 'Male'),
                               ('female', 'Female')], string='Gender')
    student_class = fields.Char(string='Class')
    city = fields.Selection([('faisalabad', 'Faisalabad'),
                             ('lahore', 'Lahore')], string='City Name')
    contact = fields.Char(string='Contact No.')
    teachers_ids = fields.One2many('school.teacher', 'student_id',
                                   string='Teachers Record')

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.student_age = today.year - rec.date_of_birth.year
            else:
                rec.student_age = 1