"""empty message

Revision ID: 14fcdf122612
Revises: 3680c3777428
Create Date: 2015-08-11 14:38:05.277524

"""

# revision identifiers, used by Alembic.
revision = '14fcdf122612'
down_revision = '3680c3777428'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
    sa.Column('entry_role_code', sa.String(), nullable=False),
    sa.Column('entry_role_seq_no', sa.Integer(), nullable=True),
    sa.Column('reg_child_code', sa.String(), nullable=False),
    sa.Column('role_cat_code', sa.String(), nullable=False),
    sa.Column('entry_role_desc', sa.String(), nullable=False),
    sa.Column('entry_status_code', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('entry_role_code')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('role')
    ### end Alembic commands ###
