"""create todo_list table

Revision ID: bfeffe225137
Revises: 
Create Date: 2021-09-24 11:39:11.569044

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bfeffe225137'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'todo_list',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.Unicode(50), nullable=False)
    )


def downgrade():
    op.drop_table('todo_list')
