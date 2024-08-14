from datetime import date, datetime
from django.core.management.base import BaseCommand
from book.models import Auther, Book


class Command(BaseCommand):
    help = 'Generate test data for Auther and Book models'

    def handle(self, *args, **kwargs):
        Auther.objects.all().delete()
        Book.objects.all().delete()

        for auther, books in test_data.items():
            auther = Auther.objects.create(name=auther)

            for book in books:
                published_at = datetime.strptime(
                    book["published_at"], "%Y-%m-%d")
                Book.objects.create(title=book["title"], published_at=date(
                    published_at.year, published_at.month, published_at.day),
                                    auther=auther)

        self.stdout.write(self.style.SUCCESS(
            'Successfully generated test data'))


test_data = {
    "Shakespeare": [
        {"title": "Hamlet", "published_at": "1603-01-01"},
        {"title": "Romeo and Juliet", "published_at": "1597-01-01"},
        {"title": "Macbeth", "published_at": "1606-01-01"},
        {"title": "Othello", "published_at": "1604-01-01"},
        {"title": "A Midsummer Night's Dream", "published_at": "1595-01-01"},
    ],
    "Tolstoy": [
        {"title": "War and Peace", "published_at": "1869-01-01"},
        {"title": "Anna Karenina", "published_at": "1877-01-01"},
        {"title": "The Death of Ivan Ilyich", "published_at": "1886-01-01"},
        {"title": "Resurrection", "published_at": "1899-01-01"},
        {"title": "The Kreutzer Sonata", "published_at": "1889-01-01"},
    ],
    "Dostoevsky": [
        {"title": "Crime and Punishment", "published_at": "1866-01-01"},
        {"title": "The Brothers Karamazov", "published_at": "1880-01-01"},
        {"title": "The Idiot", "published_at": "1869-01-01"},
        {"title": "Demons", "published_at": "1872-01-01"},
        {"title": "Notes from Underground", "published_at": "1864-01-01"},
    ],
    "Christie": [
        {"title": "Murder on the Orient Express", "published_at": "1934-01-01"},
        {"title": "The Murder of Roger Ackroyd", "published_at": "1926-01-01"},
        {"title": "And Then There Were None", "published_at": "1939-01-01"},
        {"title": "Death on the Nile", "published_at": "1937-01-01"},
        {"title": "The A.B.C. Murders", "published_at": "1936-01-01"},
    ],
    "Maugham": [
        {"title": "Of Human Bondage", "published_at": "1915-01-01"},
        {"title": "The Moon and Sixpence", "published_at": "1919-01-01"},
        {"title": "The Painted Veil", "published_at": "1925-01-01"},
        {"title": "The Razor's Edge", "published_at": "1944-01-01"},
        {"title": "The Magician", "published_at": "1908-01-01"},
    ],
}
