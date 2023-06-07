from django.contrib import admin
from .models import Form


class FormAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email') # Creates a current table with given fields
    search_fields = ('first_name', 'last_name', 'email') # Creates a search field
    list_filter = ('date', 'occupation') # Creates a filter table with given fields
    ordering = ('first_name',) # Sets the names in the alphabet order
    readonly_fields = ('email', 'occupation',) # Makes a readonly field for given fields


admin.site.register(Form, FormAdmin)