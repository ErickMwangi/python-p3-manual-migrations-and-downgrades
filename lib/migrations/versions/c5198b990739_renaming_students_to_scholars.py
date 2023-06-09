"""Renaming students to scholars

Revision ID: c5198b990739
Revises: 791279dd0760
Create Date: 2023-06-09 23:28:56.584760

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c5198b990739'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
