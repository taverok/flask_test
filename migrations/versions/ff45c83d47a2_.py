"""empty message

Revision ID: ff45c83d47a2
Revises: 4c07f7f03f54
Create Date: 2018-06-09 15:25:41.203171

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ff45c83d47a2'
down_revision = '4c07f7f03f54'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('download', sa.Column('bt_state', sa.String(length=250), nullable=True))
    op.add_column('download', sa.Column('error', sa.UnicodeText(length=4294000000), nullable=True))
    op.alter_column('download', 'status',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('download', 'status',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.drop_column('download', 'error')
    op.drop_column('download', 'bt_state')
    # ### end Alembic commands ###
