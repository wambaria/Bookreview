from django.contrib import admin

class BookReviewAdminSite(admin.AdminSite):
    title_header = "Bookreview header"
    site_header = "Bookreview Administration"
    index_title = "Bookreview site admin"