"""empty message

Revision ID: f93e7a0c5edc
Revises: 0c18b0e7affa
Create Date: 2018-10-11 00:14:03.710477

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f93e7a0c5edc'
down_revision = '0c18b0e7affa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('score', sa.Integer(), server_default='0', nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comments', 'score')
    # ### end Alembic commands ###