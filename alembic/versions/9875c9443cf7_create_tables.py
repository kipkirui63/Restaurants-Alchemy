"""create tables

Revision ID: 9875c9443cf7
Revises: 7ec447641a32
Create Date: 2023-09-04 12:09:07.965822

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9875c9443cf7'
down_revision: Union[str, None] = '7ec447641a32'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
