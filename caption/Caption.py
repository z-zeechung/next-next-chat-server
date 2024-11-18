from abc import ABC, abstractmethod
from typing import Generator


class Caption(ABC):

    @abstractmethod
    def caption(self, image: str, prompt: str) \
         -> Generator[str, None, None]:
        ...

