from typing import Any

from src.utils.exceptions import NotFound

from .constants import ErrorCode


class ItemNotFound(NotFound):
    def __init__(self, name, **kwargs: dict[str, Any]) -> None:
        self.name = name
        self.DETAIL = f"{ErrorCode.ITEM_NOT_FOUND}: {self.name}"
        super().__init__(**kwargs)


class OrderNotFound(NotFound):
    DETAIL = ErrorCode.ORDER_NOT_FOUND
