from django.contrib import admin
from catalog.models import Genre, Book, BookInstance, Author, Language


# Register your models here.
admin.site.register(Genre)
# admin.site.register(Author, AuthorAdmin)
admin.site.register(Language)


class BooksInline(admin.TabularInline):
    model = Book
    extra = 0


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name',('date_of_birth', 'date_of_death') ]
    inlines = [BooksInline]


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'due_back', 'status')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields':('book', 'imprint', 'id')
        }),
        ('Availiability', {
           'fields': ('status', 'due_back')
        }),
    )

