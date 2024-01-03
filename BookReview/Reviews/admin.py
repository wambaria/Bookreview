from django.contrib import admin
from Reviews.models import(Publisher, Contributor, Book,
                           Bookcontributor, Review)
# Register your models here.
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Bookcontributor)
admin.site.register(Review)
admin.site.register(Contributor)