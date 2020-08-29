import csv
import random
import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from main import *

Session = sessionmaker(bind=engine)
session = Session()

path = '/Users/muradaghazada/desktop/drugs/drugs.csv'

with open(path, newline='\n') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [r for r in reader]

# companies
companies = set(d['company'] for d in data)
for compname in companies:
    c = Company(name=compname)
    session.add(c)
    session.commit()


# ingredients
ingredients = set(d['ingredient_name'] for d in data)
for ingredient in ingredients:
    i = Ingredient(name=ingredient)
    session.add(i)
    session.commit()


# packagings
packagings = set(d['packaging'] for d in data)
for package in packagings:
    p = Packaging(name=package)
    session.add(p)
    session.commit()


# pharmaceutical_forms
pharmaceutical_forms = set(d['pharmaceutical_form'] for d in data)
for form in pharmaceutical_forms:
    pf = PharmaceuticalForm(name=form)
    session.add(pf)
    session.commit()


# items
for item in data:

    item_data = {
        'name': item['item_name'],
        'ingredient_uuid': session.query(Ingredient).filter_by(name = item['ingredient_name']).first().uuid,
        'company_uuid': session.query(Company).filter_by(name = item['company']).first().uuid,
        'dosage_qty': random.randint(0, 500)/100,
        'dosage_unit': random.choice(['ml/mq', 'ml', 'mq']),
        'wholesale_price': float(item['wholesale_price']),
        'sale_price': float(item['sale_price']),
        'submitted_at': datetime.datetime.strptime(item['submitted_at'], '%d.%m.%Y').utcnow()
    }

    it = Item(**item_data)
    session.add(it)
    session.commit()


# item forms
for form in data:

    form_data = {
        'item_uuid': session.query(Item).filter_by(name = form['item_name']).first().uuid,
        'form_uuid': session.query(PharmaceuticalForm).filter_by(name = form['pharmaceutical_form']).first().uuid
    }

    fo = ItemForms(**form_data)
    session.add(fo)
    try:
        session.commit()
    except Exception as identifier:
        session.rollback()
    


# item packaging
for package in data:

    package_data = {
        'item_uuid': session.query(Item).filter_by(name = package['item_name']).first().uuid,
        'packaging_uuid': session.query(Packaging).filter_by(name = package['packaging']).first().uuid
    }

    pack = ItemPackagings(**package_data)
    session.add(pack)
    try:
        session.commit()
    except Exception as identifier:
        session.rollback()



