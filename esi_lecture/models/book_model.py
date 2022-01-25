from odoo import fields, models, exceptions, api

class Book(models.Model):
    _name = 'esi.book'
    name = fields.Char(string="Titre", required=True)
    description = fields.Html(string="Description du livre")
    image = fields.Binary(string="Image", help="Sélectionner une image ici")
    date_publication = fields.Date(string='Date de sortie')
    page_count = fields.Integer(string='Nombre de pages')
    authors = fields.Many2many('res.partner', string="Auteurs")
    likes = fields.Many2many('res.users', string="Likes")
    nb_likes = fields.Integer(string="Nombre de likes", compute="_count_likes")
    product_template = fields.Many2many('product.template', string="Coffret")
    liked_by_user = fields.Boolean(string="User", compute='_count_likes')
    message_like = fields.Char(compute='_count_likes')

    @api.constrains('date_publication')
    def _check_date_publication(self):
        for book in self:
            if book.date_publication >= fields.Date.today():
                raise exceptions.ValidationError('La date de sortie doit être antérieure à la date du jour !')

    @api.constrains('page_count')
    def _check_page_count(self):
        for book in self:
            if book.page_count <= 0:
                raise exceptions.ValidationError('Le nombre de pages doit être strictement positif !')

    @api.depends('likes')
    def _count_likes(self):
        self.nb_likes = len(self.likes)
        if self.env.user in self.likes:
            self.liked_by_user = True
            self.message_like = "Vous avez aimé !"
        else:
            self.liked_by_user = False
            self.message_like = ""

    _sql_constraints = [(
        'name_check',
        'UNIQUE(name)',
        "Un livre avec ce titre existe déjà !"
    )]

    def like(self):
        if self.env.user in self.likes:
            self.write({'likes': [(3, self.env.user.id)]})
        else :
            self.write({'likes': [(4, self.env.user.id)]})

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
