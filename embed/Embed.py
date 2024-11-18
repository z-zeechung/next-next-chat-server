from abc import  ABC, abstractmethod
from typing import List

from data_types import Vector


class Embed(ABC):

    @abstractmethod
    def embed(self, texts: List[str]) -> List[Vector]:
        ...