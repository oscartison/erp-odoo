from odoo import models, fields


class Member(models.Model):
    _inherit = 'res.partner'
    number = fields.Char(string="Matricule")
    member = fields.Boolean(default=False)
    rent_ids = fields.One2many('esi.book.rent', 'member_id', string='Livres empruntés')
