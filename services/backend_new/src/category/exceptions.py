from src.category.constants import ErrorCode
from src.utils.exceptions import NotFound


class CategoryNotFound(NotFound):
    DETAIL = ErrorCode.CATEGORY_NOT_FOUND
