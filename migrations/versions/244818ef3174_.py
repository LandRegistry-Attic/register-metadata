"""empty message

Revision ID: 244818ef3174
Revises: 14fcdf122612
Create Date: 2015-08-11 15:31:50.602718

"""

# revision identifiers, used by Alembic.
revision = '244818ef3174'
down_revision = '14fcdf122612'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sub-role',
    sa.Column('sub_role_code', sa.String(), nullable=False),
    sa.Column('entry_role_code', sa.String(), nullable=False),
    sa.Column('sub_role_desc', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('sub_role_code')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sub-role')
    ### end Alembic commands ###
