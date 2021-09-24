"""create list_item table

Revision ID: 41569c792cf0
Revises: bfeffe225137
Create Date: 2021-09-24 11:39:24.480843

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41569c792cf0'
down_revision = 'bfeffe225137'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'list_items',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('content', sa.UnicodeText(1000), nullable=False),
        sa.Column('list_id', sa.Integer),
        sa.Column('parent_item_id', sa.Integer, ForeignKey("list_item.id"))
    )


def downgrade():
    op.drop_table('list_items')
