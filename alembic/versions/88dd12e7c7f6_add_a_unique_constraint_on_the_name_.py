"""Add a unique constraint on the name column of the concept table

Revision ID: 88dd12e7c7f6
Revises: 
Create Date: 2024-09-20 11:06:47.501625

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '88dd12e7c7f6'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # add a unique constraint
    op.create_unique_constraint(None, 'concept', ['name'])


def downgrade() -> None:
    # remove a unique constraint
    op.drop_constraint(None, 'concept', type_='unique')
