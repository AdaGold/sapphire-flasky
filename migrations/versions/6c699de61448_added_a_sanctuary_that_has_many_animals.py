"""Added a Sanctuary that has many Animals

Revision ID: 6c699de61448
Revises: ed9608d203a9
Create Date: 2023-05-08 11:20:48.051104

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c699de61448'
down_revision = 'ed9608d203a9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sanctuary',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sanctuary')
    # ### end Alembic commands ###