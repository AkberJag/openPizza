class ErrorCode:
    CATEGORY_NOT_FOUND = "Category Not Found"


# metadatas

metadata_info_create_category: dict = {
    "summary": "Create a new category.",
    "response_description": "Category created",
    "description": "This endpoint will create a new Category with the required field *name*.",
}

metadata_info_get_all_categories: dict = {
    "summary": "Get all categories.",
    "response_description": "All categories",
    "description": "This endpoint will return all Categories without the items list.",
}

metadata_info_get_category: dict = {
    "summary": "Get a category by id.",
    "description": "This endpoint will return a Category by id with all the items it have.",
}
