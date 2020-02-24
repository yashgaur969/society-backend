"""empty message

Revision ID: a35fdb16a2c3
Revises: 61357bbc1258
Create Date: 2020-02-21 18:20:20.716646

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a35fdb16a2c3'
down_revision = '61357bbc1258'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('gender', sa.String(), nullable=True))
    op.add_column('user', sa.Column('password_hash', sa.String(), nullable=True))
    op.add_column('user', sa.Column('user_email', sa.String(), nullable=True))
    op.add_column('user', sa.Column('user_name', sa.String(), nullable=True))
    op.drop_column('user', 'last_name')
    op.drop_column('user', 'password')
    op.drop_column('user', 'first_name')
    op.drop_column('user', 'email_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email_id', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('first_name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('last_name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('user', 'user_name')
    op.drop_column('user', 'user_email')
    op.drop_column('user', 'password_hash')
    op.drop_column('user', 'gender')
    # ### end Alembic commands ###