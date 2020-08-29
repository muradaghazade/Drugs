from flask import Flask, jsonify
from main import *
import uuid


from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind=engine)
session = Session()


app = Flask(__name__)


class ItemSerializer:
    def __init__(self, item):
        self.item = item


    def to_dict(self):
        return {
            'uuid': self.item.uuid,
            'name': self.item.name,
            'wholesale_price': self.item.wholesale_price,
            'sale_price': self.item.sale_price
        }




@app.route('/api/v1/company/<uuid:uuid>/items')
def items(uuid):
    company = session.query(Company).filter_by(uuid=uuid).first()


    if company:
        items = session.query(Item).filter_by(company_uuid = company.uuid).all()
        serialized = [ItemSerializer(item).to_dict() for item in items]
        return jsonify({
            'name': company.name,
            'uuid': company.uuid,
            'items_count': len(items),
            'items': serialized
            })
    else:
        return jsonify({"error": "error"})




if __name__ == '__main__':
    app.run(debug=True)