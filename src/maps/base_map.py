#добавить соответствующий класс из коллаба(?)
#закончить методы iter, read(?), write(?)
#отнаследовать TreeMap и HashMap от BaseMap
from abc import ABC, abstractmethod
from typing import Iterable, Tuple, List
from os import path
class BaseMap(ABC):
  @abstractmethod
  def __setitem__(self, key: str, value: int) -> None: ...

  @abstractmethod
  def __getitem__(self, key: str) -> int: ...

  @abstractmethod
  def __delitem__(self, key: str) -> None: ...

  @abstractmethod
  #закончить
  def __iter__(self) -> Iterable[Tuple[str, int]]: ...

  def __contains__(self, key: str) -> bool: ...

  class BaseMap:
      def __setitem__(self, key, value):
          raise NotImplementedError

      def __getitem__(self, key):
          raise NotImplementedError

      def __delitem__(self, key):
          raise NotImplementedError

  class HashMap(BaseMap):
      pass

  class TreeMap(BaseMap):
      pass

  def __eq__(self, other: 'BaseMap') -> bool: ...

  def __bool__(self) -> bool: ...

  @abstractmethod
  def __len__(self): ...

  def items(self) -> Iterable[Tuple[str, int]]: ...

  def values(self) -> Iterable[int]: ...

  def keys(self) -> Iterable[str]: ...

  @classmethod
  def fromkeys(cls, iterable, value=None) -> 'BaseMap': ...

  def update(self, other=None) -> None: ...

  def get(self, key, default=None): ...