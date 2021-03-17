from models.sale_item import SaleItem
from models.sale_register import SaleRegister


class SalesRanking:

    @staticmethod
    def build_ranking():
        ranking = dict()
        sale_items = SaleItem.objects.all()
        for item in sale_items:
            pipeline = [
                {'$match': {'sale_item_id': item.id}},
                {
                    '$group': {
                        '_id': "$seller_name",
                        'salesTotal': {'$sum': "$value"},
                    },
                },
                {'$sort': {'salesTotal': -1}}
            ]
            ranking[item.name] = SaleRegister.objects().aggregate(pipeline)
        return ranking
