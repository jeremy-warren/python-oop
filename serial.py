"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        """constructor"""
        self.start = start
        self.current = start

    def generate(self):
        """gives a number one higher than the last given"""
        self.current += 1
        return self.current - 1

    def reset(self):
        """resets the counter"""
        self.current = self.start
