"""Manually update enum for interactions

Revision ID: 4f484bdd2ade
Revises: b205527ace9b
Create Date: 2024-09-21 15:28:47.195664

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f484bdd2ade'
down_revision = 'b205527ace9b'
branch_labels = None
depends_on = None


def upgrade():
    # Manually updating the enum type for interaction_type
    op.execute("ALTER TABLE interactions MODIFY interaction_type ENUM('LIKE', 'UNLIKE', 'SAVE', 'UNSAVE', 'VIEW')")

def downgrade():
    # Revert to the previous enum values if necessary
    op.execute("ALTER TABLE interactions MODIFY interaction_type ENUM('LIKE', 'SAVE', 'VIEW')")