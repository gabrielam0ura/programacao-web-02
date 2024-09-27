"""Descrição não null

Revision ID: c57de0adca16
Revises: 
Create Date: 2024-09-24 19:42:34.181230

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c57de0adca16'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('formulario', schema=None) as batch_op:
        batch_op.alter_column('descricao',
               existing_type=sa.TEXT(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('formulario', schema=None) as batch_op:
        batch_op.alter_column('descricao',
               existing_type=sa.TEXT(),
               nullable=True)

    # ### end Alembic commands ###
