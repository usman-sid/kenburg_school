from datetime import date
from odoo import api, fields, models


class SchoolTeacher(models.Model):
    _name = "school.teacher"
    _description = "School Teachers"

    name = fields.Char(string='Teacher Name', required=True)
    date_of_birth = fields.Date(string='Teacher DOB')
    age = fields.Char(string='Age', compute='_compute_age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    active = fields.Boolean(string='Active', default=True)
    student_id = fields.Many2one('school.student', string='Students Record')
    record_ids = fields.One2many('school.record', 'teacher_id', string='Records')

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 1

    def action_print_xlsx(self):
        search_var = self.env["school.teacher"].search([('gender', '=', 'male')])
        print("Search_Var.....", search_var)
        for rec in search_var:
         print("name....", rec.name,
         "age...", rec.age, "gender.....", rec.gender)

    def _get_report_base_filename(self):
        return self.name #dynamic report name
        #return "TeacherReport" #Static report name



# search ORM-Method

# def first_orm(self):
# search_var = self.env["school.teacher"].search([('gender', '=', 'male')])
# print("Search_Var.....", search_var)
# for rec in search_var:
# print("name....", rec.name,
# "age...", rec.age, "gender.....", rec.gender)

# (ref ORM Method)

# def first_orm(self):
# search_var = self.env.ref('ra_school.view_school_teachers_form')
# print("Search_Var.....", search_var.id)
# -----------------------------------------

# (browse ORM Method)

# def first_orm(self):
# search_var = self.env["school.teacher"].browse([12, 9])
# print("Search_Var.....", search_var)
# for rec in search_var:
# print(“Search_var……”, rec, “Name..”, rec.name, “age..”, rec.age, “gender”, rec.gender)
# -----------------------------------------

# (create ORM Method)

# def first_orm(self):
# create_var = self.env['school.teacher'].create({
# "name": 'Ahsan Ali',
# "gender": 'male',
# })
# print("create_var.....", create_var.id)
# ----------------------------------------

# (copy ORM Method)
# def first_orm(self):
# browse_id = self.env['school.teacher'].browse(7)
# browse_id.copy()
# ----------------------------------------

# (unlink ORM Method)
# def first_orm(self):
# browse_id = self.env['school.teacher'].browse(8)
# browse_id.unlink()
