"""inital migration

Revision ID: cef22473824b
Revises: 
Create Date: 2024-03-23 13:52:52.750875

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cef22473824b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employees',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('hire_date', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('meetings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('topic', sa.String(), nullable=True),
    sa.Column('scheduled_time', sa.DateTime(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('projects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('budget', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('projects')
    op.drop_table('meetings')
    op.drop_table('employees')
    # ### end Alembic commands ###
