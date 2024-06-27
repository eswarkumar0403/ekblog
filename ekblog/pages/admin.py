from django.contrib import admin


# Register your models here.
from .models import Contact


class ContactAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'subject','is_resolved', 'contacted_at')
    list_filter = ('is_resolved', 'contacted_at',)
    list_editable = ('is_resolved',)


admin.site.register(Contact, ContactAdmin)
    


