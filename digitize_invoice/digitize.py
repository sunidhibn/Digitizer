from .models import Digitizer
from digitize_invoice.serializers import * 
from faker import Faker
filler=Faker()

def digitize(invoice):
    object=Digitizer()
    object.invoice=invoice
    object.status=filler.boolean(chance_of_getting_true=80)
    object.data={
        "invoice no.": filler.ean8(),
        "comapany" : filler.company(),
        "Cashier" : filler.name(),
        "buyer" : filler.name(),
        "contact no." : filler.phone_number(),
    }
    object.digitized_at=filler.date_time_between('now', '+1d')
    object.save()
    # data_serializer=DigitizerSerializer(object)
    # data_serializer.save()

