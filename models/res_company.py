from odoo import api, fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    ir_attach_1_ids = fields.Many2many(
        'ir.attachment',
        'res_company_ir_attach_1_rel',
        'company_id',
        'attachment_id',
        string='Attachments 1'
    )

    ir_attach_2_ids = fields.Many2many(
        'ir.attachment',
        'res_company_ir_attach_2_rel',
        'company_id',
        'attachment_id',
        string='Attachments 2'
    )

    ir_attach_3_ids = fields.Many2many(
        'ir.attachment',
        'res_company_ir_attach_3_rel',
        'company_id',
        'attachment_id',
        string='Attachments 3'
    )
