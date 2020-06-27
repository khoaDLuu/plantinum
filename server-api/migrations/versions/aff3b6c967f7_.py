"""empty message

Revision ID: aff3b6c967f7
Revises: 6c89a25ee18d
Create Date: 2020-06-27 19:00:53.037371

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aff3b6c967f7'
down_revision = '6c89a25ee18d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('sensor_data', 'time_recorded',
               existing_type=sa.DATE(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('sensor_data', 'time_recorded',
               existing_type=sa.DATE(),
               nullable=False)
    # ### end Alembic commands ###