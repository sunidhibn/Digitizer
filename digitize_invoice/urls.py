from django.urls import path,include
from .views import UploadInvoiceView,InvoiceListView,InvoiceDetailView
urlpatterns = [
    path('upload/',UploadInvoiceView.as_view(),name="upload"),
    path('invoicelist/',InvoiceListView.as_view(),name="invoice_list"),
    path('invoice/<int:pk>/',InvoiceDetailView.as_view(),name="invoice_detail"),
]
