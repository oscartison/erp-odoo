from odoo import fields, models, exceptions, api

class Rent(models.Model):
    _name = 'esi.book.rent'

    book_id = fields.One2many('esi.book','rent_ids', string="Livre", required = True)
    member_id = fields.One2many('res.partner','rent_ids', string="Emprunteur", domain=[('member', '=', True)], required = True)
    state = fields.Selection(
        [('prete', 'Exemplaire prêté'), ('retour', 'Exemplaire retourné'), ('perdu', 'Exemplaire perdu')], default='prete')
    rent_date = fields.Date(
        "Date de l'emprunt",
        default=lambda self: fields.Datetime.now())
    return_date = fields.Date(
        "Date de retour")
