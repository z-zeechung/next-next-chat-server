from abc import ABC, abstractmethod


class Paint(ABC):

    @abstractmethod
    def paint(self, prompt: str, image: str) -> str:
        ...

