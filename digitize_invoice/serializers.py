from rest_framework import serializers
from .models import Invoice,Digitizer
from .digitize import digitize

class InvoiceSerializer(serializers.ModelSerializer):

    id = serializers.ReadOnlyField()
    invoice = serializers.FileField(allow_empty_file=True)
    class Meta:
        model = Invoice
        fields = "__all__"
    
    def create(self, validated_data):
        invoice = Invoice.objects.create(**validated_data)
        digitize(invoice)
        return invoice


class DigitizerSerializer(serializers.ModelSerializer):
    invoice=InvoiceSerializer()

    def update(self, instance, validated_data):
        instance.data.update(validated_data["data"])
        instance.save()
        return instance

    class Meta:
        model=Digitizer
        fields=('invoice','status','data','digitized_at')

