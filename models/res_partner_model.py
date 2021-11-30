from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'
    books_written = fields.Many2many('esi.book', string='liste de livres')