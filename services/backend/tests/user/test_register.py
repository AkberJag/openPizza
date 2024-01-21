import pytest
from sqlalchemy.exc import IntegrityError
from your_module import register_new_user, get_current_user_details

class MockDB:
    pass

class MockUser:
    pass

class MockCrudUser:
    @staticmethod
    async def create(db, obj_in):
        pass

    @staticmethod
    async def get_by_email(db, email):
        pass

# Mocking the required functions and classes
crud_user = MockCrudUser()

@pytest.fixture
def db():
    return MockDB()

@pytest.fixture
def user_in():
    return MockUser()

@pytest.mark.asyncio
async def test_register_new_user_successful(db, user_in):
    result = await register_new_user(db, user_in=user_in)
    assert result is not None  # Add your specific assertions here

@pytest.mark.asyncio
async def test_register_new_user_email_taken(db, user_in):
    # Assuming that the create method raises IntegrityError on email conflict
    crud_user.create = pytest.AsyncMock(side_effect=IntegrityError("Email taken"))

    with pytest.raises(EmailTaken):
        await register_new_user(db, user_in=user_in)

@pytest.mark.asyncio
async def test_get_current_user_details(db):
    email = "test@example.com"
    result = await get_current_user_details(db, email=email)
    assert result is not None  # Add your specific assertions here
