from odoo import fields, models, api


class Book(models.Model):
    _inherit = 'esi.book'
    rent_ids = fields.Many2one('esi.book.rent', string='emprunts')
    nb_rents = fields.Integer("Nombre d'emprunts", compute="_count_rents")

    @api.depends('likes')
    def _count_rents(self):
        for book in self:
            book.nb_rents = len(book.rent_ids)
