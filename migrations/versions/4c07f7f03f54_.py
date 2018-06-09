"""empty message

Revision ID: 4c07f7f03f54
Revises: 00b908d949f9
Create Date: 2018-06-09 15:10:31.389095

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c07f7f03f54'
down_revision = '00b908d949f9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('download', sa.Column('total_download_kb', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('download', 'total_download_kb')
    # ### end Alembic commands ###
