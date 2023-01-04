# DO NOT MODIFY AN CLASS ATTRIBUTE , Always modify through a method
from typedproperty import typedproperty , String, Integer, Float
class Product:
    # __slots__ = ("name", "_quant", "price") // no objects dynamicaly can be added or modified, used for performance improvements
    name = String("name")
    quant = Integer("quant")
    price = Float("price")

    # name = typedproperty("name", str)
    # quant = typedproperty("quant", int)
    # price = typedproperty("price", float)


    def __init__(self, name, quant, price):
        self.name = name
        self.quant = quant
        self.price = price

    def __repr__(self):
        #Ideally output of repr should be usable by eval()
        #prints meaning output ( no objects printing :) )
        return 'Product({},{},{})'.format(repr(self.name) , self.quant, self.price)
    #
    # @property
    # def name(self):
    #     return self._name
    #
    # @name.setter
    # def name(self, value):
    #     if not isinstance(value, str):
    #         raise TypeError("Expected an str")
    #     self._name = value
    #
    # @property
    # def quant(self):
    #     return self._quant
    #
    # @quant.setter
    # def quant(self, value):
    #     if not isinstance(value, int):
    #         raise TypeError("Expected an int")
    #     self._quant = value
    #
    # @property
    # def price(self):
    #     return self._price
    #
    # @price.setter
    # def price(self, value):
    #     if not isinstance(value, float):
    #         raise TypeError("Expected an Float")
    #     self._price = value

    @property
    def cost(self):
        return self.quant * self.price

    def sell(self, unit):
        self.quant = self.quant - unit