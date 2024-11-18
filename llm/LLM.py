from abc import ABC, abstractmethod
from typing import List, Literal, Generator

from data_types import Message, Tool


class LLM(ABC):

    @abstractmethod
    def chat(self, messages: List[Message], model: Literal['regular', 'smart', 'long'], tools: List[Tool]) \
         -> Generator[str, None, None]:
        ...

