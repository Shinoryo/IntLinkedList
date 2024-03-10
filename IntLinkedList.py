from enum import Enum, auto
from typing import List
import IntLinkedListException

class IntLinkedList:
    """
    A doubly-linked list for storing integers.
    """
    
    class Dummy(Enum):
        """
        Enum representing dummy elements at the head and tail.
        """
        HEAD = auto()
        TAIL = auto()
    
    def __init__(self) -> None:
        """
        Initialise with the first and last dummy elements.
        """
        self.before = {}
        self.after = {}
        
        self.after[self.Dummy.HEAD] = self.Dummy.TAIL
        self.before[self.Dummy.TAIL] = self.Dummy.HEAD
    
    def append(self, item: int, previous_item: int = Dummy.HEAD) -> None:   
        """
        Adds an item after a previous_item.

        Args:
            item (int): Item to add.
            previous_item (int, optional): Add item after this. Defaults to the dummy element at the head.
        Raises:
            IntLinkedListException: If the item already exists in this list or if previous_item does not exist in this list.
        """
        if item in self.before.keys():
            raise IntLinkedListException("{}はこのリストに存在するため、追加できません。".format(item))
        if previous_item not in self.after.keys():
            raise IntLinkedListException("{}はこのリストに存在しないため、アイテムを追加できません。".format(previous_item))
        
        self.before[item] = previous_item
        self.after[item] = self.after[previous_item]
        self.before[self.after[previous_item]] = item
        self.after[previous_item] = item
    
    def append_left(self, item: int, next_item: int = Dummy.TAIL) -> None:
        """
        Adds an item before a next_item.

        Args:
            item (int): Item to add.
            next_item (int, optional): Add item before this. Defaults to the dummy element at the tail.
        Raises:
            IntLinkedListException: If the item already exists in this list or if next_item does not exist in this list.
        """
        if item in self.after.keys():
            raise IntLinkedListException("{}はこのリストに存在するため、追加できません。".format(item))
        if next_item not in self.before.keys():
            raise IntLinkedListException("{}はこのリストに存在しないため、アイテムを追加できません。".format(next_item))
        
        self.after[item] = next_item
        self.before[item] = self.before[next_item]
        self.after[self.before[item]] = item
        self.before[next_item] = item
    
    def remove(self, item: int):
        """
        Removes an item from the list.

        Args:
            item (int): Item to remove.
        Raises:
            IntLinkedListException: If Dummy.HEAD or Dummy.TAIL is specified or if item does not exist in this list.
        """
        if item in {self.Dummy.HEAD, self.Dummy.TAIL}:
            raise IntLinkedListException("{}は削除できません。".format(item))
        if item not in self.after.keys():
            raise IntLinkedListException("{}はこのリストに存在しないため、削除できません。".format(item))
        
        self.after[self.before[item]] = self.after[item]
        self.before[self.after[item]] = self.before[item]
        del self.before[item]
        del self.after[item]
    
    def to_list(self) -> List[int]:
        """
        Converts the list to a Python list.

        Returns:
            List[int]: Python list containing items of the list.
        """
        data_list = []
        current = self.after[self.Dummy.HEAD]
        while current != self.Dummy.TAIL:
            data_list.append(current)
            current = self.after[current]
        return data_list
