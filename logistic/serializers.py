from rest_framework import serializers

from logistic.models import Product, StockProduct, Stock
from drf_writable_nested import WritableNestedModelSerializer


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = StockProduct
        fields = ['id', 'product', 'quantity', 'price']


class StockSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['id', 'address', 'positions']

    # настройте сериализатор для склада

    # def create(self, validated_data):
        # достаем связанные данные для других таблиц
        # print(validated_data)
        # positions = validated_data.pop(validated_data['positions'])
        # print(validated_data.get('product'))
        # создаем склад по его параметрам
        # stock = super().create(validated_data)

        # здесь вам надо заполнить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions

        # return stock

    # def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        # positions = validated_data.pop('positions')

        # обновляем склад по его параметрам
        # stock = super().update(instance, validated_data)
        # prod = ProductPositionSerializer.update(instance, positions)
        # здесь вам надо обновить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions

        # return stock
