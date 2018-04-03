"""
We know that from 2012-01-01 to 2012-01-31 all images have RA off by 1 degree.
Patch them on the fly.
"""


class Image:
    """
    This might come from a database query.
    """
    def __init__(self, date, ra, dec, fltr):
        self.date = date
        self.ra = ra
        self.dec = dec
        self.filter = fltr


class Patcher:
    def __init__(self, image, min_date, max_date, fn):
        self._image = image
        self.min_date = min_date
        self.max_date = max_date
        self.fn = fn

    # Pretend to be an Image
    def __getattr__(self, name):
        if self.min_date <= self.image.date <= self.max_date:
            img = self.fn(self._image)
        else:
            img = self._image
        return getattr(img, name)

    def __setattr__(self, name, value):
        if name == '_image':
            super().__setattr__(name, value)
        else:
            return setattr(self._image, name, value)
