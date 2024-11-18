from search.Search import Search
from typing import List

from data_types import SearchResult


class Google(Search):

    def search(self, query: str, count: int, index: int) -> List[SearchResult]:
        ...