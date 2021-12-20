from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'
    books_written = fields.Many2many('esi.book', string='liste de livres')
    nb_books = fields.Integer(string="Nombre de livres", compute='_count_books', required=True, store=True)

    @api.depends('books_written')
    def _count_books(self):
        for r in self:
            r.nb_books = len(r.books_written)
