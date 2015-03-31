"""Added achievementcategories

Revision ID: 42ab7edc19e2
Revises: 
Create Date: 2015-03-31 13:57:22.570668

"""

# revision identifiers, used by Alembic.
revision = '42ab7edc19e2'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('achievementcategories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column(u'achievements', sa.Column('achievementcategory_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'achievements', 'achievementcategories', ['achievementcategory_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'achievements', type_='foreignkey')
    op.drop_column(u'achievements', 'achievementcategory_id')
    op.drop_table('achievementcategories')
    ### end Alembic commands ###
