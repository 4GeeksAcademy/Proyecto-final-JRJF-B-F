"""empty message

Revision ID: 934b1a432d45
Revises: 2f7b6461e8da
Create Date: 2025-06-07 16:01:21.257831

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '934b1a432d45'
down_revision = '2f7b6461e8da'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.add_column(sa.Column('stock', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('product_photo', sa.String(length=120), nullable=True))

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('role', sa.String(length=20), nullable=False, server_default='user'))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('role')

    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.drop_column('product_photo')
        batch_op.drop_column('stock')

    # ### end Alembic commands ###
