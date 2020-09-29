from rest_framework import serializers
from .models import Invoice,Digitizer

class InvoiceSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField()
    invoice = serializers.FileField(allow_empty_file=True)
    class Meta:
        model = Invoice
        fields = "__all__"

class DigitizerSerializer(serializers.ModelSerializer):
    invoice=InvoiceSerializer()

    def update(self, instance, validated_data):
        instance.data.update(validated_data["data"])
        instance.save()
        return instance

    class Meta:
        model=Digitizer
        fields=('invoice','status','data','digitized_at')

