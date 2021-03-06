"""empty message

Revision ID: 1b535e5a8b74
Revises: 32d4757e5774
Create Date: 2014-04-25 15:06:55.172385

"""

# revision identifiers, used by Alembic.
revision = '1b535e5a8b74'
down_revision = '32d4757e5774'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('active', sa.Boolean(), nullable=True))
    op.add_column('user', sa.Column('confirmed_at', sa.DateTime(), nullable=True))
    op.add_column('user', sa.Column('password', sa.String(length=255), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'password')
    op.drop_column('user', 'confirmed_at')
    op.drop_column('user', 'active')
    ### end Alembic commands ###
