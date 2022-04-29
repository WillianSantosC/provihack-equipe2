"""empty message

Revision ID: 34ab147c28aa
Revises: b809a8f786bf
Create Date: 2022-04-28 20:58:11.583005

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34ab147c28aa'
down_revision = 'b809a8f786bf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('residues', sa.Column('type', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('residues', 'type')
    # ### end Alembic commands ###