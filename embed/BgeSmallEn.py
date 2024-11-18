from typing import List

from embed.Embed import Embed
from data_types import Vector


class BgeSmallEn(Embed):
    def __init__(self):
        from FlagEmbedding import FlagModel
        self.model = FlagModel('BAAI/bge-small-en', use_fp16=True, cache_dir='.cache')

    def embed(self, texts: List[str]) -> List[Vector]:
        embeddings = self.model.encode(texts)
        return [list(v) for v in embeddings]
