from odoo import fields, models, exceptions, api


class Rent(models.Model):
    _name = 'esi.book.rent'

    book_id = fields.Many2one('esi.book', string="Livre", required=True)
    member_id = fields.Many2one('res.partner', string="Emprunteur", domain=[('member', '=', True)], required=True)
    state = fields.Selection(
        [('prete', 'Exemplaire prêté'), ('retour', 'Exemplaire retourné'), ('perdu', 'Exemplaire perdu')],
        default='prete')
    rent_date = fields.Date(
        "Date de l'emprunt",
        default=lambda self: fields.Datetime.now())
    return_date = fields.Date(
        "Date de retour")

    @api.constrains("book_id")
    def check_rent(self):
    
        for rent in self.book_id.rent_ids:
            if rent and not rent.state == 'retour':
                raise exceptions.ValidationError("Ce livre n'a pas encore été rendu !")

    def setRetour(self):
        self.state = 'retour'

    def setPerdu(self):
        self.state = 'perdu'


