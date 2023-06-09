"""Create column in Animal for sanctuary_id 

Revision ID: 396dc5dc8e01
Revises: 6c699de61448
Create Date: 2023-05-08 11:24:08.466598

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '396dc5dc8e01'
down_revision = '6c699de61448'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('animal', sa.Column('sanctuary_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'animal', 'sanctuary', ['sanctuary_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'animal', type_='foreignkey')
    op.drop_column('animal', 'sanctuary_id')
    # ### end Alembic commands ###
