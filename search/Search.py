from abc import ABC, abstractmethod
from typing import List

from data_types import SearchResult

class Search(ABC):

    @abstractmethod
    def search(self, query: str, count: int, index: int) -> List[SearchResult]:
        ...
