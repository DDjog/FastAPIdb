"""'Init'

Revision ID: 0ad14e84d1d3
Revises: 
Create Date: 2024-01-28 20:25:29.482740

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0ad14e84d1d3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contacts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=25), nullable=False),
    sa.Column('second_name', sa.String(length=25), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_index('ix_contact_id', table_name='contact')
    op.drop_table('contact')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contact',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('firstname', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('secondname', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('telephone', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('birthday', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('notes', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='contact_pkey')
    )
    op.create_index('ix_contact_id', 'contact', ['id'], unique=False)
    op.drop_table('contacts')
    # ### end Alembic commands ###
