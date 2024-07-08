"""update blog table

Revision ID: 6295b8d85614
Revises: 28d06cd59c9c
Create Date: 2024-07-08 23:14:42.454207

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '6295b8d85614'
down_revision: Union[str, None] = '28d06cd59c9c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blogs_users',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('users_id', sa.Uuid(), nullable=False),
    sa.Column('blogs_id', sa.Uuid(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['blogs_id'], ['blogs.id'], ),
    sa.ForeignKeyConstraint(['users_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('companies_users')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('companies_users',
    sa.Column('id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('users_id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('blogs_id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('active', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['blogs_id'], ['blogs.id'], name='companies_users_blogs_id_fkey'),
    sa.ForeignKeyConstraint(['users_id'], ['users.id'], name='companies_users_users_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='companies_users_pkey')
    )
    op.drop_table('blogs_users')
    # ### end Alembic commands ###