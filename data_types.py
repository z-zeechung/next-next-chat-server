from typing import List, Literal

Vector = List[float]


class Message:
    def __init__(self, role: Literal['user', 'assistant', 'system'], content: str):
        self.role = role
        self.content = content


class Tool:

    class ToolParam:
        def __init__(self, name: str, type: str, description: str):
            self.name = name
            self.type = type
            self.description = description

    def __init__(self, name: str, type: str, description: str, params: List[ToolParam]):
        self.name = name
        self.type = type
        self.description = description
        self.params = params


class SearchResult:
    def __init__(self, url: str, digest: str):
        self.url = url
        self.digest = digest