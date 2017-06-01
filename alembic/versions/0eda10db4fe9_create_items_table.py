"""create items table

Revision ID: 0eda10db4fe9
Revises: 
Create Date: 2017-06-01 20:18:10.425184

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0eda10db4fe9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    conn.execute(
        """
        CREATE TABLE items (
            id SERIAL PRIMARY KEY,
            message TEXT NOT NULL
        );
        """
    )

def downgrade():
    conn = op.get_bind()
    conn.execute(
        """
        DROP TABLE items;
        """
    )
