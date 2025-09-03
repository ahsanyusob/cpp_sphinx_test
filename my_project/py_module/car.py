class Car:
    """
    A simple car class.

    Attributes
    ----------
    brand : str
        The brand of the car.
    speed : int
        The current speed in km/h.
    """

    def __init__(self, brand):
        """
        Initialize the car.

        Parameters
        ----------
        brand : str
            The brand of the car.
        """
        self.brand = brand
        self.speed = 0

    def accelerate(self, value):
        """
        Increase speed.

        Parameters
        ----------
        value : int
            Amount to increase speed by.
        """
        self.speed += value