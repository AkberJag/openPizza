"""made names unique

Revision ID: 4cb9055e7e61
Revises: 27d1e0071218
Create Date: 2023-10-16 23:40:06.086756

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4cb9055e7e61'
down_revision: Union[str, None] = '27d1e0071218'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_food_categories_category_name', table_name='food_categories')
    op.create_index(op.f('ix_food_categories_category_name'), 'food_categories', ['category_name'], unique=True)
    op.drop_index('ix_food_items_item_name', table_name='food_items')
    op.create_index(op.f('ix_food_items_item_name'), 'food_items', ['item_name'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_food_items_item_name'), table_name='food_items')
    op.create_index('ix_food_items_item_name', 'food_items', ['item_name'], unique=False)
    op.drop_index(op.f('ix_food_categories_category_name'), table_name='food_categories')
    op.create_index('ix_food_categories_category_name', 'food_categories', ['category_name'], unique=False)
    # ### end Alembic commands ###
