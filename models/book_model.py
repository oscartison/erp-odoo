import logging

from odoo import fields, models, exceptions, api
from odoo.tools.safe_eval import datetime

_logger = logging.getLogger(__name__)


class Book(models.Model):
    _name = 'esi.book'
    name = fields.Char(string="Titre", required=True)
    description = fields.Html(string="Description du livre")
    image = fields.Binary(string="Image", help="Selectionner une image ici")
    date_publication = fields.Date(string='Date de sortie')
    page_count = fields.Integer(string='Nombre de page')
    authors = fields.Many2many('res.partner', string="Auteurs")

    @api.constrains('date_publication')
    def _check_date_publication(self):
        for book in self:
            if book.date_publication > fields.Date.today():
                raise exceptions.ValidationError('Date de sortie doit être antérieure à la date du jour')

    @api.constrains('page_count')
    def _check_page_count(self):
        for book in self:
            if book.page_count <= 0:
                raise exceptions.ValidationError('Nombre de pages doit être strictement positif')


    _sql_constraints = [ (
        'name_check',
        'UNIQUE(name)',
        "Titre du livre doit être unique"
    )]

    def copy(self, default=None):
        default = dict(default or {})

        copied_count = self.search_count(
            [('name', '=like', u"Copy of {}%".format(self.name))])
        if not copied_count:
            new_name = u"Copy of {}".format(self.name)
        else:
            new_name = u"Copy of {} ({})".format(self.name, copied_count)

        default['name'] = new_name
        return super(Book, self).copy(default)


