from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
import uuid


engine = create_engine("postgresql://marmeladze:geometry123@localhost/taskbot_backend", echo=True)

Base = declarative_base()


class Company(Base):
    __tablename__ = 'companies'

    uuid = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(200))

    def __repr__(self):
        return f"<Company(uuid='{self.uuid}' name='{self.name}')>"

class Ingredient(Base):
    __tablename__ = 'ingredients'

    uuid = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(200))
    items = relationship("Item", backref="ingredient")
    
    def __repr__(self):
        return f"<Ingredient(uuid='{self.uuid}' name='{self.name}')>"


class PharmaceuticalForm(Base):
    __tablename__ = 'pharmaceutical_forms'

    uuid = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(200))

    def __repr__(self):
        return f"<Form(uuid='{self.uuid}' name='{self.name}')>"


class Packaging(Base):
    __tablename__ = 'packagings'

    uuid = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(200))

    def __repr__(self):
        return f"<Packaging(uuid='{self.uuid}' name='{self.name}')>"


class Item(Base):
    __tablename__ = 'items'

    uuid = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(200))
    ingredient_uuid = Column(Integer, ForeignKey('ingredients.uuid'))        
    company_uuid = Column(Integer, ForeignKey('companies.uuid'))        
    dosage_qty = Column(Float(precision=2))
    dosage_unit = Column(String(10))
    wholesale_price = Column(Float(precision=2))
    sale_price = Column(Float(precision=2))
    submitted_at = Column(DateTime(timezone=True))

    def __repr__(self):
        return f"<Item(uuid='{self.uuid}' name='{self.name}')>"


class ItemForms(Base):
    __tablename__ = 'item_forms'
    item_uuid = Column(Integer, ForeignKey('items.uuid'), primary_key=True)
    form_uuid = Column(Integer, ForeignKey('pharmaceutical_forms.uuid'), primary_key=True)


class ItemPackagings(Base):
    __tablename__ = 'item_packagings'
    item_uuid = Column(Integer, ForeignKey('items.uuid'), primary_key=True)
    packaging_uuid = Column(Integer, ForeignKey('packagings.uuid'), primary_key=True)


Base.metadata.create_all(engine)