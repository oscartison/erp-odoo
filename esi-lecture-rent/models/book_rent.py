from odoo import fields, models, exceptions, api

class Rent(models.Model):
    _name = 'esi.book.rent'

    book_id = fields.One2many('esi.book','rent_ids', string="Livre")
    member_id = fields.One2many('res.partner','rent_ids', string="Emprunteur", domain=[('member', '=', True)])
    state = fields.Selection(
        [('prete', 'Exemplaire prêté'), ('retourn', 'Exemplaire retourné'), ('perdu', 'Exemplaire perdu')], default='prete')
    date_pret = fields.Datetime(
        "Date de l'emprunt",
        default=lambda self: fields.Datetime.now())
    date_retour = fields.Datetime(
        "Date de retour")
