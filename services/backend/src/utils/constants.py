"""Global constants."""


from enum import Enum


class Environment(str, Enum):
    LOCAL = "LOCAL"
    STAGING = "STAGING"
    TESTING = "TESTING"
    PRODUCTION = "PRODUCTION"

    @property
    def is_debug(self):
        return self in (self.LOCAL, self.STAGING, self.TESTING)

    @property
    def is_testing(self):
        return self == self.TESTING

    @property
    def is_deployed(self) -> bool:
        return self in (self.STAGING, self.PRODUCTION)


tags_metadata = [
    {
        "name": "Auth",
        "description": "User authentication. The **login** logic is here.",
    },
    {
        "name": "User",
        "description": "Operations with users, except the **login** logic.",
    },
    {
        "name": "Category",
        "description": "Operations with Food Categories.",
    },
    {
        "name": "Item",
        "description": "Operations with Food items.",
    },
    {
        "name": "Order",
        "description": "Operations with Orders. Create **New Order** and view all **orders** logics are here.",
    },
]

api_metadata = {
    "contact": {
        "name": "View this on GitHub",
        "url": "https://github.com/AkberJag/openPizza",
    },
    "description": """
## _This is a 🚧 work in progress 🚧 side project_
---

### Auth 🔐
You will be able to **login** with a user name (email) and passcode. (implemented)

### User 👥
You will be able to:
- **Register** a new user with username (email) and passcode. (implemented)
- **User Details** of the current logged in user. (implemented) 

### Category 🥣
You will be able to:
- **Add Category** with name. (implemented)
- **Get all Categories** from the db. (implemented) 
- **Get a Category** by id. (implemented) 

### Item 🍩
You will be able to:
- **Add Item.** (implemented)
- *Update Item.* (_not implemented_)
 
### Order 🛒
You will be able to:
- **Place Order** with order details and items. (implemented)
- **Get all Orders** from the db. (implemented) 
- **Get an Order** by id. (implemented) 

""",
}
