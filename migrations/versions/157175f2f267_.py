"""empty message

Revision ID: 157175f2f267
Revises: 4b6c521a1bf5
Create Date: 2018-06-09 12:01:19.999414

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '157175f2f267'
down_revision = '4b6c521a1bf5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('download', sa.Column('changed_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('download', 'changed_at')
    # ### end Alembic commands ###