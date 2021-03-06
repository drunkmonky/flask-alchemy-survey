"""empty message

Revision ID: 43747d017635
Revises: c73380702e8b
Create Date: 2018-09-12 16:09:53.128810

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '43747d017635'
down_revision = 'c73380702e8b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'email_confirmed_at')
    op.drop_column('user', 'active')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('active', sa.BOOLEAN(), server_default=sa.text(u'false'), autoincrement=False, nullable=False))
    op.add_column('user', sa.Column('email_confirmed_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
