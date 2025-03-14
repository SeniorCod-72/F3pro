"""Added columns on barbers table

Revision ID: 84a0598809c2
Revises: 
Create Date: 2025-03-14 11:19:45.286372

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '84a0598809c2'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('barbers', sa.Column('specialization', sa.String(), nullable=False))
    op.add_column('barbers', sa.Column('years_of_experience', sa.Integer(), nullable=False))
    op.add_column('barbers', sa.Column('status', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('barbers', 'status')
    op.drop_column('barbers', 'years_of_experience')
    op.drop_column('barbers', 'specialization')
    # ### end Alembic commands ###
