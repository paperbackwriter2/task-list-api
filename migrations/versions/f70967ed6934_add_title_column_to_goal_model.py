"""Add title column to Goal model

Revision ID: f70967ed6934
Revises: b1cb402c21ec
Create Date: 2021-10-27 18:22:08.314921

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f70967ed6934'
down_revision = 'b1cb402c21ec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('goal', sa.Column('id', sa.Integer(), nullable=False))
    op.add_column('goal', sa.Column('title', sa.String(), nullable=True))
    op.drop_column('goal', 'goal_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('goal', sa.Column('goal_id', sa.INTEGER(), autoincrement=True, nullable=False))
    op.drop_column('goal', 'title')
    op.drop_column('goal', 'id')
    # ### end Alembic commands ###