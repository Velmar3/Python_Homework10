class ReadNoDescPoint3D:
    def __set_name__(self, owner, name):
        self.name = "_x"

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class DescPoint3D:

    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError("Координата должна быть целым числом")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_coord(value)
        setattr(instance, self.name, value)


class Point3D:
    x = DescPoint3D()
    y = DescPoint3D()
    z = DescPoint3D()
    xr = ReadNoDescPoint3D()

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z


p = Point3D(8, 3, 6)
# p.xr = 9
print(p.xr, p.__dict__)