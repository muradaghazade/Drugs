from sqlalchemy.orm import sessionmaker
from models import *

Session = sessionmaker()
session = Session()

path = '/Users/tariyelaghazada/desktop/drugs/drugs.csv'

with open(path, newline='\n') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [r for r in reader]


companies = set(d['company'] for d in data)
for compname in companies:
    c = Company(name=compname)
    session.add(c)
    session.commit()


# ingredients, packagings,  pharmaceutical_forms