# IntLinkedList
整数を格納するためのPythonの双方向連結リスト。

## `IntLinkedList.Dummy` 列挙型
先頭と末尾のダミー要素を表す列挙型。

### メンバー
- `HEAD`: 先頭のダミー要素
- `TAIL`: 末尾のダミー要素

## `__init__(self) -> None`
先頭と末尾のダミー要素を持つように初期化する。

## `append(self, item: int, previous_item: int = Dummy.HEAD) -> None`
アイテムをリストに追加する。すでに存在するアイテムを指定してはならない。

### 引数
- `item` (int): 追加するアイテム。
- `previous_item` (int, optional): この後に `item` を追加する。デフォルトは先頭のダミー要素。

### 例外
- `IntLinkedListException`: `item`がこのリストに存在する場合、または、`previous_item`がこのリストに存在しない場合。

## `append_left(self, item: int, next_item: int = Dummy.TAIL) -> None`
アイテムをリストに追加する。

### 引数
- `item` (int): 追加するアイテム。
- `next_item` (int, optional): この前にアイテムを追加する。デフォルトは末尾のダミー要素。

### 例外
- `IntLinkedListException`: `item`がこのリストに存在する場合、または、`next_item`がこのリストに存在しない場合。

## `remove(self, item: int)`
リストからアイテムを削除する。

### 引数
- `item` (int): 削除するアイテム。

### 例外
- `IntLinkedListException`: `Dummy.HEAD` か `Dummy.TAIL` が指定された場合、または、`item` がこのリストに存在しない場合。

## `to_list(self) -> List[int]`
リストをPythonのリストに変換する。

### 戻り値
- `List[int]`: リストのアイテムを含むPythonのリスト。
