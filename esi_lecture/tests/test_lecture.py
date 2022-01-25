from datetime import datetime, timedelta, date

from odoo.exceptions import UserError
from odoo.tests.common import TransactionCase


class TestLecture(TransactionCase):

    def setUp(self, *args, **kwargs):
        super(TestLecture, self).setUp(*args, **kwargs)  # Création d’un nouvel utilisateur pour les tests
        self.fresh_user = self.env['res.users'].create({
            'login': 'marika',
            'name': "Marika Winska", })
        # Recherche de l’utilisateur avec les droits suffisants sur le module
        self.task_manager = self.env.ref('esi_lecture.task_manager')

    def test_create(self):
        Book = self.env['esi.book'].with_user(self.task_manager)
        book = Book.create({'name': 'Test Book'})
        self.assertEqual(book.nb_likes, 0)

    def test_create_page(self):
        Book = self.env['esi.book'].with_user(self.task_manager)
        book = Book.create({'name': 'Test Book', 'page_count': 100})
        self.assertEqual(book.page_count, 100)

    def test_create_exception_page(self):
        "Not good page count"
        Book = self.env['esi.book'].with_user(self.task_manager)
        with self.assertRaises(UserError):
            book = Book.create({'name': 'Test Book', 'page_count': 0})

    def test_create_exception_date(self):
        "Not good date"
        Book = self.env['esi.book'].with_user(self.task_manager)
        with self.assertRaises(UserError):
            book = Book.create({'name': 'Test Book', 'date_publication': datetime.now()})

    def test_create_exception_date(self):
        "Good date"
        Book = self.env['esi.book'].with_user(self.task_manager)
        book = Book.create({'name': 'Test Book',
                            'date_publication': date.today() + timedelta(days=-1)})
        self.assertEqual(book.date_publication, date.today() + timedelta(days=-1))
