"""empty message

Revision ID: b33b7fc0f627
Revises: efa2f68ef393
Create Date: 2024-06-12 22:45:50.704281

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b33b7fc0f627'
down_revision = 'efa2f68ef393'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('token_blog_list',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('jti', sa.String(length=36), nullable=False),
    sa.Column('token_type', sa.String(length=10), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('revoked_at', sa.DateTime(), nullable=True),
    sa.Column('expires', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('jti')
    )
    with op.batch_alter_table('token_blog_list', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_token_blog_list_user_id'), ['user_id'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('token_blog_list', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_token_blog_list_user_id'))

    op.drop_table('token_blog_list')
    # ### end Alembic commands ###
