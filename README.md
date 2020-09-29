# Digitizer

Used Tech stack : Django and sqlite

### Installation
1. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the dependencies
```bash
pip install -r requirements.txt
```

2. migrate and collectstatic
```bash
./manage.py makemigrations
./manage.py migrate
./manage.py collectstatic
```

3. Run server
```bash
./manage.py runserver
```

4. Access the API to upload invoice
```bash
curl --location --request POST 'http://localhost:8000/upload/' \
--form 'invoice=@/C:/Users/sunidhi/Desktop/myinvoice.pdf'
```
5. Access the API to list all invoice details 
```bash
curl --location --request GET 'http://localhost:8000/invoicelist' \
--header 'Content-Type: application/json'
```
6. Access the API to view individual invoice detail with id in url
```bash
curl --location --request GET 'http://localhost:8000/invoice/6' \
--header 'Content-Type: application/json'
```
7.Access the API to edit status of perticular invoice digitisation data with help of its id in url
```bash
curl --location --request PUT 'http://localhost:8000/invoice/20/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "status": false,
    "data": {
        "Cashier": "Weber, Herman and Medina",
        "contact no.": "(675)825-97030891",
        "address" : "Newyork"
    
    }
}'
```

It staff wants update digitised data , each piece ofinformation can be updated with its key.
If he gives the existing key and updated data, the perticular field will be updated. Ex:contact no. is updated
If he wants to add a field , he should provide new key and value to data. Ex: address field is added here
He can also change the status of “digitized” by making status field as true/false

