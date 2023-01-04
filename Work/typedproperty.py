
def typedproperty(name, d_type):
    attr_name = "-" + name

    @property
    def attr(self):
        return getattr(self, attr_name)

    @attr.setter
    def attr(self, value):
        if not isinstance(value, d_type):
            raise TypeError("Expected {}".format(d_type))
        setattr(self, attr_name, value)

    return attr

# Lambda syntax
#Parameter:return value : invdict.sort(key=lambda p:p["price"])
# >>> def prod_name(p):
# ...     return p["name"]
# ...
# >>>
# >>> invdict.sort(key=prod_name)


String = lambda name: typedproperty(name, str)
Integer = lambda name: typedproperty(name, int)
Float = lambda name: typedproperty(name, float)