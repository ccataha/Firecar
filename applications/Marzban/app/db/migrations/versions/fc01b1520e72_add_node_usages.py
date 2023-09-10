"""add node usages

Revision ID: fc01b1520e72
Revises: c106bb40c861
Create Date: 2023-05-07 12:08:23.331402

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc01b1520e72'
down_revision = 'c106bb40c861'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('node_usages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('node_id', sa.Integer(), nullable=True),
    sa.Column('uplink', sa.BigInteger(), nullable=True),
    sa.Column('downlink', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['node_id'], ['nodes.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('created_at', 'node_id')
    )
    op.create_index(op.f('ix_node_usages_id'), 'node_usages', ['id'], unique=False)
    # op.add_column('node_user_usages', sa.Column('created_at', sa.DateTime(), nullable=False))
    # op.create_unique_constraint(None, 'node_user_usages', ['created_at', 'user_id', 'node_id'])
    # ### end Alembic commands ###

    # manual
    op.drop_table('node_user_usages')
    op.create_table('node_user_usages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('node_id', sa.Integer(), nullable=True),
    sa.Column('used_traffic', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['node_id'], ['nodes.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('created_at', 'user_id', 'node_id')
    )
    op.create_index(op.f('ix_node_user_usages_id'), 'node_user_usages', ['id'], unique=False)



def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    # op.drop_constraint(None, 'node_user_usages', type_='unique')
    # op.drop_column('node_user_usages', 'created_at')
    op.drop_index(op.f('ix_node_usages_id'), table_name='node_usages')
    op.drop_table('node_usages')
    # ### end Alembic commands ###

    # manual
    op.drop_table('node_user_usages')
    op.create_table('node_user_usages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_username', sa.String(34), nullable=True),
    sa.Column('node_id', sa.Integer(), nullable=True),
    sa.Column('used_traffic', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['node_id'], ['nodes.id'], ),
    sa.ForeignKeyConstraint(['user_username'], ['users.username'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_username', 'node_id')
    )
    op.create_index(op.f('ix_node_user_usages_id'), 'node_user_usages', ['id'], unique=False)
