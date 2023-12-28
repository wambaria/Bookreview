from django.db import models
from django.contrib import auth

class Publisher(models.Model):
    """The Publishing company"""
    name = models.CharField(
        max_length =50,
        help_text = "Input name of the Publisher"
        )
    website = models.URLField(
        help_text = "The Publishing company's website"
        )
    email = models.EmailField(
        help_text = "The publishing comapnys emails"
    )

    def __str__(self):
        return self.name
    
class Book(models.Model):
    """The Published books"""
    title = models.CharField(
        max_length =70,
        help_text ="Input name of the book"
    )
    publication_date = models.DateField(
        verbose_name ="Date the book wa published"
    )
    isbn = models.CharField(
        max_length =20,
        verbose_name = "ISBN number of the book"
    )
    publisher =models.ForeignKey(
        Publisher, on_delete =models.CASCADE
    )
    contributor = models.ManyToManyField(
        'Contributor', through="Bookcontributor"
    )

    def __str__(self):
        return self.title

    
class Contributor(models.Model):
    """A contributor to the book e.g editor"""
    first_name = models.CharField(
        max_length = 50,
        help_text = "The contributors first name"
    )
    last_name = models.CharField(
        max_length = 50,
        help_text = "The contributors last name"
    )
    email = models.EmailField(
        max_length = 200,
        help_text = "Enter the contributor email"
    )

    def __st__(self):
        return self.first_name
    
class Bookcontributor(models.Model):
    class ContributionRole(models.TextChoices):
        AUTHOR = "AUTHOR", "Author"
        CO_AUTHOR = 'CO_AUTHOR', "Co-Author"
        EDITOR = "EDITOR", "Editor"

    book = models.ForeignKey(
        Book, on_delete = models.CASCADE
    )
    contributor = models.ForeignKey(
        Contributor, on_delete = models.CASCADE
    )
    role = models.CharField(
        verbose_name ="The role the contributor has in the book", 
        choices = ContributionRole.choices,
        max_length =20
    )

class Review(models.Model):
    content = models.TextField(help_text="The Review text.")
    rating = models.IntegerField(help_text="The rating the reviewer has given.")
    date_created = models.DateTimeField(
        auto_now_add=True,
        help_text="The date and time the review was created"
    )
    date_edited = models.DateTimeField(
        null = True,
        help_text = "The date the review was last edited"
    )
    creator = models.ForeignKey(
        auth.get_user_model(), on_delete=models.CASCADE
    )
    book = models.ForeignKey(
        Book, on_delete = models.CASCADE,
        help_text = "The book that is referred by this review"
    )