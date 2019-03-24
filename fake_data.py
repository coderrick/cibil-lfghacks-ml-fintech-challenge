import json
import csv
from faker import Faker
from faker import Factory
from faker.providers import internet, phone_number, isbn
import random
import helpermodule1
import os


threshold = 0.94  ##change this for random number chooser, number roughly indicates percentage of normal transactions

fake = Faker()
fake2 = Factory.create()
fake2.add_provider(internet)
fake2.add_provider(phone_number)
fake2.add_provider(isbn)

item_classes = ["dental_health", "general_health", "maternity_health", "furniture", "groceries", "automotive_accessories", "automotive_maintenance", "automotive_purchase", "jewelry", "entertainment", "dining", "education"]

vendor_classes = ["pharmacy", "restaurant", "automotive_service", "automotive_sales", "department_store", "jeweler", "movie", "amusement", "gas", "education_provider", "grocery", "health_provider", "financial"]

##10 orgs, 10 bank account numbers
orgbankaccounts = []
for i in range (0,10):
    orgbankaccounts.append(fake2.isbn10(separator=""))
##    print (i)
##    print (orgbankaccount[i])
    
items = []
for i in range (0, 100):
    itemdata = {}
    item_name = fake.name()
    categoryselect = random.randint(0,11)
    category = item_classes[categoryselect]
    vendorselect = random.randint(0, 12)
    vendor = vendor_classes[vendorselect] 
    price = random.randint(0,9)

    itemdata["item_name"] = item_name
    itemdata["category"] = category
    itemdata["vendor"] = vendor
    itemdata["price"] = price
    items.append(itemdata)

def WriteDictToCSV(csv_file,csv_columns,dict_data):
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in dict_data:
                writer.writerow(data)
    except IOError:
            print("I/O error")    
    return 

WriteDictToCSV("./items.csv", ["item_name","category","vendor","price"], items)

