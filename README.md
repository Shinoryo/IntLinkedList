# IntLinkedList Specification

## Overview
The `IntLinkedList` class provides a doubly-linked list for storing integers.

## Enumerations
### Dummy
- Enum representing dummy elements at the head and tail.
#### Values
- `HEAD`: Represents the dummy element at the head.
- `TAIL`: Represents the dummy element at the tail.

## Class: `IntLinkedList`
- A doubly-linked list for storing integers.

### Methods
#### `__init__(self) -> None`
- Initializes the linked list with the first and last dummy elements.

#### `append(self, item: int, previous_item: int = Dummy.HEAD) -> None`
- Adds an item after a specified previous_item.
##### Parameters
- `item (int)`: Item to add.
- `previous_item (int, optional)`: Add item after this. Defaults to the dummy element at the head.
##### Raises
- `IntLinkedListException`: If the item already exists in this list or if previous_item does not exist in this list.

#### `append_left(self, item: int, next_item: int = Dummy.TAIL) -> None`
- Adds an item before a specified next_item.
##### Parameters
- `item (int)`: Item to add.
- `next_item (int, optional)`: Add item before this. Defaults to the dummy element at the tail.
##### Raises
- `IntLinkedListException`: If the item already exists in this list or if next_item does not exist in this list.

#### `remove(self, item: int) -> None`
- Removes a specified item from the list.
##### Parameters
- `item (int)`: Item to remove.
##### Raises
- `IntLinkedListException`: If Dummy.HEAD or Dummy.TAIL is specified or if item does not exist in this list.

#### `to_list(self) -> List[int]`
- Converts the list to a Python list.
##### Returns
- `List[int]`: Python list containing items of the list.
