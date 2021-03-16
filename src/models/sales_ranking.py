from models.sale_item import SaleItem


class SalesRanking:

    @staticmethod
    def build_ranking():
        pipeline = [
            {
                '$group': {
                    '_id': "$seller_name",
                    'salesTotal': {'$sum': "$item_value"},
                },
            },
            {'$sort': {'salesTotal': -1}}
        ]
        return SaleItem.objects().aggregate(pipeline)
