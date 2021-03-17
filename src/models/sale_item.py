from bson import ObjectId
from mongoengine import ObjectIdField, StringField, Document


class SaleItem(Document):
    _id = ObjectIdField(primary_key=True, default=ObjectId)
    name = StringField(max_length=300, required=True)

    @staticmethod
    def get_or_register_new(name):
        existing_item = SaleItem.objects.filter(name=name.lower()).first()
        if existing_item:
            return existing_item
        else:
            new_sale = SaleItem(name=name.lower()).save()
            return new_sale
