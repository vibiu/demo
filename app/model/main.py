import sqlalchemy as sa
metadata = sa.MetaData()

tbl = sa.Table(
    'tbl', metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('val', sa.String(255)))
