from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from django.shortcuts import get_object_or_404

from .serializers import InvoiceSerializer,DigitizerSerializer
from .models import Invoice,Digitizer


class UploadInvoiceView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

      file_serializer = InvoiceSerializer(data=request.data)

      if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InvoiceListView(generics.ListAPIView):
    queryset=Digitizer.objects.all()
    serializer_class=DigitizerSerializer

class InvoiceDetailView(generics.RetrieveUpdateAPIView):
    queryset=Digitizer.objects.all()
    serializer_class=DigitizerSerializer

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
   
    

   
