"""Add user preferences embedding

Revision ID: 7dec079034b4
Revises: 50c4cc7c1c7d
Create Date: 2024-07-01 21:49:25.265978

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7dec079034b4'
down_revision = '50c4cc7c1c7d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_preferences_embeddings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('embedding', sa.LargeBinary(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_preferences_embeddings')
    # ### end Alembic commands ###