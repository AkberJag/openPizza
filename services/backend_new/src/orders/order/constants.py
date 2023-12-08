class ErrorCode:
    ITEM_NOT_FOUND = "Item Not Found"
    ORDER_NOT_FOUND = "Order Not Found"


# metadatas
metadata_info_place_order: dict = {
    "summary": "Place new order.",
    "response_description": "Order placed",
    "description": "This endpoint will create a new order with the required fields *customer id* and *order items*.",
}

metadata_info_get_all_orders: dict = {
    "summary": "Get all orders.",
    "response_description": "All orders from DB",
    "description": "This endpoint will return all orders from the db",
}

metadata_info_get_order_details: dict = {
    "summary": "Get a order details by it's id.",
    "response_description": "Order details",
    "description": "This endpoint will return an Order by id with all the items it have.",
}
