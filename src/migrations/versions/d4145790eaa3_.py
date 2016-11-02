"""empty message

Revision ID: d4145790eaa3
Revises: None
Create Date: 2016-11-01 22:46:43.169322

"""

# revision identifiers, used by Alembic.
revision = 'd4145790eaa3'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('twilio',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('account_sid', sa.String(length=255), nullable=True),
    sa.Column('auth_token', sa.String(length=255), nullable=True),
    sa.Column('twilio_number', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('twilio_users',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('twilio_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['twilio_id'], ['twilio.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.add_column(u'user', sa.Column('twilio_accounts', sa.String(length=255), nullable=True))
    op.drop_column(u'user', 'van')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column(u'user', sa.Column('van', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column(u'user', 'twilio_accounts')
    op.drop_table('twilio_users')
    op.drop_table('twilio')
    ### end Alembic commands ###