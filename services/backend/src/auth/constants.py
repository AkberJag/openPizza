class ErrorCode:
    AUTHENTICATION_REQUIRED = "Authentication required."
    AUTHORIZATION_FAILED = "Authorization failed. User has no access."
    ACCOUNT_DISABLED = "Unauthorized: Account disabled."
    INVALID_TOKEN = "Invalid token."
    INVALID_CREDENTIALS = "Invalid credentials."
    EMAIL_TAKEN = "Email is already taken."
    USER_NOT_FOUND = "User Not Found"


# metadatas
metadata_info_login: dict = {
    "summary": "Login with Email and Password",
    "response_description": "User login successful",
    "description": """**Authenticates a user based on email and password.**

This endpoint allows users to log in by providing their email and password.
Upon successful authentication, it returns the user's data and sets an
HTTP-only cookie with an access token.
* ! username expects an email address !

### Return
- User object on successful authentication.
""",
}
