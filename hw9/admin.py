from django.contrib import admin
from .models import Book, Reader

class BookAvailabilityFilter(admin.SimpleListFilter):
    title = 'Режим просмотра книг'
    parameter_name = 'availability'

    def lookups(self, request, model_admin):
        return (
            ('all', 'Усі книги'),
            ('available', 'Книги у наявності'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'available':
            return queryset.filter(current_reader__isnull=True)
        return queryset

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_year', 'style', 'publisher', 'is_available', 'current_reader')
    search_fields = ('title', 'author')
    
    list_filter = (BookAvailabilityFilter, 'style')

@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'phone', 'email', 'registration_date', 'display_borrowed_books')
    search_fields = ('last_name', 'email')

    def display_borrowed_books(self, obj):
        books = obj.borrowed_books.all()
        if books:
            return ", ".join([b.title for b in books])
        return "Нет взятых книг"
    display_borrowed_books.short_description = "Книги на руках"
