from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import *

Session = sessionmaker(bind=engine)
session = Session()

path = '/Users/tariyelaghazada/desktop/drugs/drugs.csv'

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


#pharmaceutical_forms
pharmaceutical_forms = set(d['pharmaceutical_form'] for d in data)
for form in pharmaceutical_forms:
    pf = PharmaceuticalForm(name=form)
    session.add(pf)
    session.commit()


# ingredients, packagings,  pharmaceutical_forms