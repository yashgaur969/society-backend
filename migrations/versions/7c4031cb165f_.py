"""empty message

Revision ID: 7c4031cb165f
Revises: f9fcc2057e92
Create Date: 2020-02-24 09:43:20.931801

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c4031cb165f'
down_revision = 'f9fcc2057e92'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('access_token_table')
    op.add_column('user', sa.Column('access_token', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'access_token')
    op.create_table('access_token_table',
    sa.Column('access_token', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('access_token', name='access_token_table_pkey')
    )
    # ### end Alembic commands ###