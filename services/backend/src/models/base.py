"""Model Base"""

from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    __name__: str
    id: Any

    @declared_attr
    def __tablename__(cls) -> str:
        """auto generate the table name from the model class
        Eg: table name for the model 'User' will be users
        """
        return f"{cls.__name__.lower()}s"
