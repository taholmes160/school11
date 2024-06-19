"""Initial migration

Revision ID: 4e0c5c038900
Revises: 
Create Date: 2024-06-19 15:41:54.437393

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '4e0c5c038900'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###

    op.alter_column('users', 'password_hash',
               existing_type=mysql.VARCHAR(length=512),
               type_=sa.String(length=512),
               nullable=False)
    op.alter_column('users', 'role_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.alter_column('users', 'first_name',
               existing_type=mysql.VARCHAR(length=50),
               type_=sa.String(length=80),
               existing_nullable=True)
    op.alter_column('users', 'last_name',
               existing_type=mysql.VARCHAR(length=50),
               type_=sa.String(length=80),
               existing_nullable=True)
    op.alter_column('users', 'profile_picture',
               existing_type=mysql.VARCHAR(length=255),
               type_=sa.String(length=120),
               existing_nullable=True)
    op.alter_column('users', 'bio',
               existing_type=mysql.TEXT(),
               type_=sa.String(length=500),
               existing_nullable=True)
    op.alter_column('users', 'phone_number',
               existing_type=mysql.VARCHAR(length=15),
               type_=sa.String(length=20),
               existing_nullable=True)
    op.alter_column('users', 'password_reset_token',
               existing_type=mysql.VARCHAR(length=100),
               type_=sa.String(length=120),
               existing_nullable=True)
    op.drop_index('phone_number', table_name='users')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('phone_number', 'users', ['phone_number'], unique=False)
    op.alter_column('users', 'password_reset_token',
               existing_type=sa.String(length=120),
               type_=mysql.VARCHAR(length=100),
               existing_nullable=True)
    op.alter_column('users', 'phone_number',
               existing_type=sa.String(length=20),
               type_=mysql.VARCHAR(length=15),
               existing_nullable=True)
    op.alter_column('users', 'bio',
               existing_type=sa.String(length=500),
               type_=mysql.TEXT(),
               existing_nullable=True)
    op.alter_column('users', 'profile_picture',
               existing_type=sa.String(length=120),
               type_=mysql.VARCHAR(length=255),
               existing_nullable=True)
    op.alter_column('users', 'last_name',
               existing_type=sa.String(length=80),
               type_=mysql.VARCHAR(length=50),
               existing_nullable=True)
    op.alter_column('users', 'first_name',
               existing_type=sa.String(length=80),
               type_=mysql.VARCHAR(length=50),
               existing_nullable=True)
    op.alter_column('users', 'role_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('users', 'password_hash',
               existing_type=sa.String(length=128),
               type_=mysql.VARCHAR(length=512),
               nullable=True)

    # ### end Alembic commands ###
