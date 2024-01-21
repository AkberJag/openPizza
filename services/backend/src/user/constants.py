class ErrorCode:
    AUTHENTICATION_REQUIRED = "Authentication required."
    AUTHORIZATION_FAILED = "Authorization failed. User has no access."
    ACCOUNT_DISABLED = "Unauthorized: Account disabled."
    INVALID_TOKEN = "Invalid token."
    INVALID_CREDENTIALS = "Invalid credentials."
    EMAIL_TAKEN = "Email is already taken."
    USER_NOT_FOUND = "User Not Found"


# metadatas
metadata_info_register: dict = {
    "summary": "Register a new user.",
    "response_description": "User created",
    "description": "This endpoint will register a new user with the required fields *name*, *email*, and *password*.",
}
