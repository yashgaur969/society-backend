"""empty message

Revision ID: 65843ef94271
Revises: ca32465c4122
Create Date: 2020-02-24 19:43:07.847313

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65843ef94271'
down_revision = 'ca32465c4122'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('apartment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('number_of_wings', sa.Integer(), nullable=True),
    sa.Column('number_of_floors', sa.Integer(), nullable=True),
    sa.Column('number_of_flats', sa.Integer(), nullable=True),
    sa.Column('total_flats', sa.Integer(), nullable=True),
    sa.Column('society_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['society_id'], ['society.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('apartment')
    # ### end Alembic commands ###
