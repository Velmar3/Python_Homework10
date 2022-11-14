class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Meta(metaclass=MetaSingleton):
    pass


number1 = Meta()
number2 = Meta()
print(number1, number2)
