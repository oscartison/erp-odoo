from odoo import fields, models


class Book(models.Model):
    _inherit = 'esi.book'
    rent_ids = fields.Many2one('esi.book.rent', string='emprunts')
