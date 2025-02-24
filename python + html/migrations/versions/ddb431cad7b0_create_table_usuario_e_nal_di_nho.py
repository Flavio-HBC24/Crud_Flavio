"""create Table usuario E NAL DI NHO

Revision ID: ddb431cad7b0
Revises: 
Create Date: 2024-08-23 10:00:54.997817

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ddb431cad7b0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('idade', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('usuario')
    # ### end Alembic commands ###
