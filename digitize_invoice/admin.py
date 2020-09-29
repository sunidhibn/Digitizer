from django.contrib import admin
from .models import Invoice,Digitizer
# Register your models here.
class InvoiceAdmin(admin.ModelAdmin):
    list_display=('id','invoice','created_at')

class DigitizerAdmin(admin.ModelAdmin):
    list_display=('pk','invoice','data','status','digitized_at')

admin.site.register(Invoice,InvoiceAdmin)  
admin.site.register(Digitizer,DigitizerAdmin) 