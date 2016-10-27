"""empty message

Revision ID: 1619e091f49d
Revises: None
Create Date: 2016-10-26 10:44:01.795545

"""

# revision identifiers, used by Alembic.
revision = '1619e091f49d'
down_revision = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('emergency',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('msg', sa.String(length=1000), nullable=True),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.Column('phone_number', sa.String(length=15), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('messages')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('messages',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('msg', sa.VARCHAR(length=1000), autoincrement=False, nullable=True),
    sa.Column('time', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('phone_number', sa.VARCHAR(length=15), autoincrement=False, nullable=True),
    sa.Column('message_recipient', sa.VARCHAR(length=25), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name=u'messages_pkey')
    )
    op.drop_table('emergency')
    ### end Alembic commands ###