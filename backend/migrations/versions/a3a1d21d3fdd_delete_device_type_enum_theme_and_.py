"""Delete device_type, enum theme and integer font_size

Revision ID: a3a1d21d3fdd
Revises: 80b008cc01ff
Create Date: 2024-06-01 17:00:32.814806

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a3a1d21d3fdd'
down_revision = '80b008cc01ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('interactions', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'content', ['content_id'], ['id'])

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('theme',
               existing_type=mysql.VARCHAR(length=50),
               type_=sa.Enum('light', 'dark'),
               existing_nullable=True)
        batch_op.alter_column('font_size',
               existing_type=mysql.VARCHAR(length=50),
               type_=sa.Integer(),
               existing_nullable=True)
        batch_op.drop_column('device_type')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('device_type', mysql.VARCHAR(length=50), nullable=True))
        batch_op.alter_column('font_size',
               existing_type=sa.Integer(),
               type_=mysql.VARCHAR(length=50),
               existing_nullable=True)
        batch_op.alter_column('theme',
               existing_type=sa.Enum('light', 'dark'),
               type_=mysql.VARCHAR(length=50),
               existing_nullable=True)

    with op.batch_alter_table('interactions', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    # ### end Alembic commands ###
