from enum import Enum, auto
from typing import List
import IntLinkedListException

class IntLinkedList:
    """
    双方向連結リストを表すクラス。
    """
    
    class Dummy(Enum):
        """
        先頭と末尾のダミー要素を表す列挙型。
        """
        HEAD = auto()
        TAIL = auto()
    
    def __init__(self) -> None:
        """
        先頭と末尾のダミー要素を持つように初期化する。
        """
        self.before = {}
        self.after = {}
        
        self.after[self.Dummy.HEAD] = self.Dummy.TAIL
        self.before[self.Dummy.TAIL] = self.Dummy.HEAD
    
    def append(self, item: int, previous_item: int = Dummy.HEAD) -> None:   
        """
        アイテムを追加する。
        すでに存在するアイテムを指定してはならない。

        Args:
            item (int): 追加するアイテム。
            previous_item (int, optional): この後にitemを追加する。デフォルトは先頭のダミー要素。
        Raises:
            IntLinkedListException: itemがこのリストに存在する場合。
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
        アイテムを追加する。

        Args:
            item (int): 追加するアイテム。
            next_item (int, optional): この前にアイテムを追加する。デフォルトは末尾のダミー要素。
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
        リストからアイテムを削除する。

        Args:
            item (int): 削除するアイテム。
        Raises:
            IntLinkedListException: Dummy.HEADかDummy.TAILが指定された場合、または、itemがこのリストに存在しない場合。
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
        リストをPythonのリストに変換する。

        Returns:
            List[int]: リストのアイテムを含むPythonのリスト。
        """
        data_list = []
        current = self.after[self.Dummy.HEAD]
        while current != self.Dummy.TAIL:
            data_list.append(current)
            current = self.after[current]
        return data_list
