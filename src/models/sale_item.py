from bson import ObjectId
import datetime

from mongoengine import Document, StringField, DateTimeField, DecimalField, ValidationError, \
    ObjectIdField

ALLOWED_SELLERS = ['foo', 'bar', 'a', 'b', 'c']


def valid_seller_name(seller_name):
    if seller_name.lower() not in ALLOWED_SELLERS:
        raise ValidationError(field_name='seller_name',
                              message="{} is not an allowed seller.".format(seller_name))


class SaleItem(Document):
    _id = ObjectIdField(primary_key=True, default=ObjectId)
    seller_name = StringField(max_length=300, required=True, validation=valid_seller_name)
    customer_name = StringField(max_length=300, required=True)
    item_name = StringField(max_length=300, required=True)
    item_value = DecimalField(min_value=0, required=True)
    sale_date = DateTimeField(default=datetime.datetime.utcnow)
