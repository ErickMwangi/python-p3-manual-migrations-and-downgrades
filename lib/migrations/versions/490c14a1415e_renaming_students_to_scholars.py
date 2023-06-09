"""Renaming students to scholars

Revision ID: 490c14a1415e
Revises: c5198b990739
Create Date: 2023-06-09 23:42:43.799127

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '490c14a1415e'
down_revision = 'c5198b990739'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
