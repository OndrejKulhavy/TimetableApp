from queue import Queue


class SetQueue(Queue):
    """
    A specialized queue that ensures unique elements by maintaining a set of all items.

    This class extends the standard Queue class and adds the functionality to track unique items
    using a set named 'all_items'.
    """

    def __init__(self, maxsize=0):
        """
        Initialize a SetQueue instance.

        Parameters:
        - maxsize (int): Maximum size of the queue. If 0, the queue size is unbounded.
        """
        super().__init__(maxsize)
        self.all_items = set()

    def _put(self, item):
        """
        Put an item into the queue if it is not already present.

        Parameters:
        - item: The item to be added to the queue.

        Raises:
        - Full: If the queue is full and cannot accept additional items.
        """
        if item not in self.all_items:
            super()._put(item)
            self.all_items.add(item)


def __len__(self):
    """
    Return the number of elements that have passed through this queue, including those currently in the queue.

    Returns:
    - int: The total number of elements that have been in the queue.
    """
    return len(self.all_items)
