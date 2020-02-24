"""empty message

Revision ID: ca32465c4122
Revises: c4d3bae9e6b9
Create Date: 2020-02-24 19:38:57.509107

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca32465c4122'
down_revision = 'c4d3bae9e6b9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('society',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('society_type', sa.String(), nullable=True),
    sa.Column('is_fenced', sa.String(), nullable=True),
    sa.Column('is_guarded', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('building',
    sa.Column('id', sa.Integer(), nullable=False),
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
    op.drop_table('building')
    op.drop_table('society')
    # ### end Alembic commands ###
