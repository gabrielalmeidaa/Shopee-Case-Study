import datetime

from bson import ObjectId
from models.sale_item import SaleItem
from mongoengine import Document, StringField, DateTimeField, ValidationError, \
    ObjectIdField, ReferenceField, DecimalField

ALLOWED_SELLERS = ['foo', 'bar', 'a', 'b', 'c']


def valid_seller_name(seller_name):
    if seller_name.lower() not in ALLOWED_SELLERS:
        raise ValidationError(field_name='seller_name',
                              message="{} is not an allowed seller.".format(seller_name))


class SaleRegister(Document):
    _id = ObjectIdField(primary_key=True, default=ObjectId)
    seller_name = StringField(max_length=300, required=True, validation=valid_seller_name)
    customer_name = StringField(max_length=300, required=True)
    sale_item_id = ReferenceField(SaleItem)
    value = DecimalField(min_value=0, required=True)
    sale_date = DateTimeField(default=datetime.datetime.utcnow)

    @staticmethod
    def register_sale(seller_name, customer_name, item_name, item_value):
        sale_item = SaleItem.get_or_register_new(item_name)
        return SaleRegister(seller_name=seller_name, customer_name=customer_name,
                            sale_item_id=sale_item.id, value=item_value)

