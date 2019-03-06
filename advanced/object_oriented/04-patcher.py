class Image:
    def __init__(self, date, ra, dec, fltr):
        self.date = date
        self.ra = ra
        self.dec = dec
        self.filter = fltr

    def __repr__(self):
        return f'{self.__class__.__name__}({self.ra}, {self.dec}, ' + \
            f'{self.filter})'


class Patcher:
    def __init__(self, image, min_date, max_date, fn):
        if min_date <= image.date <= max_date:
            self._image = fn(image)
        else:
            self._image = image

    def __getattr__(self, name):
        return getattr(self._image, name)

    def __setattrr__(self, name, value):
        if name == '_image':
            return super().__setattr__(name, value)
        return setattr(self._image, name, value)
