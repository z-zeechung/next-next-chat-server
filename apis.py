from caption.DummyCaption import DummyCaption
from embed.BgeSmallEn import BgeSmallEn
from embed.BgeSmallZh import BgeSmallZh
from llm.Qwen1_5B import Qwen1_5B
from paint.DummyPaint import DummyPaint
from search.Baidu import Baidu


CHAT_APIS = {
    "qwen-1.5b": Qwen1_5B
}

EMBED_APIS = {
    "bge-small-en": BgeSmallEn,
    "bge-small-zh": BgeSmallZh
}

CAPTION_APIS = {
    "dummy": DummyCaption
}

PAINT_APIS = {
    "dummy": DummyPaint
}

SEARCH_APIS = {
    "baidu": Baidu
}