"""criando compania

Revision ID: 932e181b30b4
Revises: 2aad708aedd1
Create Date: 2022-04-28 21:56:04.027385

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '932e181b30b4'
down_revision = '2aad708aedd1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('company',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('fantsy_name', sa.String(), nullable=True),
    sa.Column('cnpj', sa.String(), nullable=False),
    sa.Column('point', sa.String(), nullable=False),
    sa.Column('phone', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password_hash', sa.String(), nullable=False),
    sa.Column('ong', sa.String(), nullable=False),
    sa.Column('quantity_collect', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('company')
    # ### end Alembic commands ###