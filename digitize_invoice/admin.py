from django.contrib import admin
from .models import Invoice
# Register your models here.
class InvoiceAdmin(admin.ModelAdmin):
    list_display=('id','invoice','created_at')

admin.site.register(Invoice,InvoiceAdmin)