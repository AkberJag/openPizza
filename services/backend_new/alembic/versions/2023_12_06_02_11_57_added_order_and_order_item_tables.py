"""Added order and order item tables

Revision ID: 2ff7513903cc
Revises: d5225150a837
Create Date: 2023-12-06 02:11:57.083106

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2ff7513903cc'
down_revision: Union[str, None] = 'd5225150a837'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('tax_val', sa.Integer(), nullable=True),
    sa.Column('order_notes', sa.Text(), nullable=True),
    sa.Column('order_total', sa.Float(), nullable=True),
    sa.Column('user', sa.Integer(), nullable=True),
    sa.Column('order_owner', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['order_owner'], ['users.id'], ),
    sa.ForeignKeyConstraint(['user'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_order_id'), 'order', ['id'], unique=False)
    op.create_table('order_items',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('price_per_unit', sa.Float(), nullable=True),
    sa.Column('item_notes', sa.String(), nullable=True),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.Column('item_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['item_id'], ['item.id'], ),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_order_items_id'), 'order_items', ['id'], unique=False)
    op.create_index(op.f('ix_order_items_name'), 'order_items', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_order_items_name'), table_name='order_items')
    op.drop_index(op.f('ix_order_items_id'), table_name='order_items')
    op.drop_table('order_items')
    op.drop_index(op.f('ix_order_id'), table_name='order')
    op.drop_table('order')
    # ### end Alembic commands ###
