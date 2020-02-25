"""empty message

Revision ID: 9c1debd9d2b3
Revises: 2199434281bf
Create Date: 2020-02-25 09:31:44.403333

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c1debd9d2b3'
down_revision = '2199434281bf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('apartment', 'society_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('building', 'society_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('society', 'management_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('society', 'management_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('building', 'society_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('apartment', 'society_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
