from odoo import models, fields


class Member(models.Model):
    _inherit = 'res.partner'
    number = fields.Char(string="Matricule")
    member = fields.Boolean(default=False)
    rent_ids = fields.Many2one('esi.book.rent', string='Livres empruntés')
