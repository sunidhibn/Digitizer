from django.db import models

class Invoice(models.Model):
    
    invoice = models.FileField(blank=False, null=False, upload_to='documents/')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.invoice.name
    
class Digitizer(models.Model):
    invoice= models.OneToOneField(Invoice,on_delete=models.CASCADE,primary_key=True)
    data=models.JSONField(default=dict,blank=True,null=True)
    status=models.BooleanField(default=False)
    digitized_at=models.DateTimeField(blank=True,null=True)
