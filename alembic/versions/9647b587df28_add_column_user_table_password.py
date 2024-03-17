"""add column user table password

Revision ID: 9647b587df28
Revises: 215b4f68e8e2
Create Date: 2024-03-17 18:15:14.695252

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '9647b587df28'
down_revision: Union[str, None] = '215b4f68e8e2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password', sa.String(length=100), nullable=False))
    op.alter_column('user', 'email',
               existing_type=mysql.VARCHAR(length=50),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'email',
               existing_type=mysql.VARCHAR(length=50),
               nullable=True)
    op.drop_column('user', 'password')
    # ### end Alembic commands ###
