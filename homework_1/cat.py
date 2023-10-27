"""
Implementation of coding exercise 2.1 (Part 1)
"""

class Cat:
    """
    This class represents a very simple implementation of a cat.
    """
    def __init__(self, name):
        self.name = name

    def greet(self, other):
        return (f"Hello I am {self.name}! I see you are also a cool fluffy kitty {other.name}, let’s together purr at the human, so that they shall give us food!")
