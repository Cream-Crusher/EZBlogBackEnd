"""add blog_id in post

Revision ID: 9f3af8af659e
Revises: 6295b8d85614
Create Date: 2024-07-13 17:49:14.546016

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9f3af8af659e'
down_revision: Union[str, None] = '6295b8d85614'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('blog_id', sa.Uuid(), nullable=True))
    op.create_foreign_key(None, 'posts', 'blogs', ['blog_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'posts', type_='foreignkey')
    op.drop_column('posts', 'blog_id')
    # ### end Alembic commands ###