from odoo import models, fields


class ResUser(models.Model):
    _inherit = 'res.users'
    books_liked = fields.Many2many('esi.book', string='Liste de livres likés')
