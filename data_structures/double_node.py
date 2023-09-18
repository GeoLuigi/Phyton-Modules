"""
Double node class
"""

class DoubleNode:
    """
    Double node class definition
    """
    def __init__(self,data = None):
        self.data = data
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.data)
