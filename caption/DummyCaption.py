from typing import Generator
from caption.Caption import Caption


class DummyCaption(Caption):
    def caption(self, image: str, prompt: str) \
         -> Generator[str, None, None]:
        info = f"this is a dummy caption api. the input prompt is `{prompt}`"
        for i in info.split(" "):
            yield i+" "