from typing import NamedTuple


class _REGISTRY_KEYS_NT(NamedTuple):
    X_KEY: str = "X"
    U_KEY: str = "U"
    EMBEDDING_KEY: str = "embedding"


REGISTRY_KEYS = _REGISTRY_KEYS_NT()
