from odoo import models,fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    books = fields.Many2many('esi.book', string="Composés de livres")
