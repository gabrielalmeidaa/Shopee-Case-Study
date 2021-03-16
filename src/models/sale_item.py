from bson import ObjectId
import datetime

from mongoengine import Document, StringField, DateTimeField, DecimalField


class SaleItem(Document):
    _id = StringField(primary_key=True, default=ObjectId)
    seller_name = StringField(max_length=300, required=True)
    customer_name = StringField(max_length=300, required=True)
    item_name = StringField(max_length=300, required=True)
    item_value = DecimalField(min_value=0)
    sale_date = DateTimeField(default=datetime.datetime.utcnow)

