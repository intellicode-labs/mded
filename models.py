import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timezone


Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = "user"

    id = sa.Column('id', sa.Integer, primary_key=True)
    email = sa.Column("email", sa.String(50), nullable=False, unique=True)
    username = sa.Column('username', sa.String(50), nullable=False, unique=True)
    passwd = sa.Column('passwd', sa.String(50), nullable=False)
    name = sa.Column('name', sa.String(50), nullable=False)
    address = sa.Column('address', sa.String(100), nullable=True)
    pincode = sa.Column('pincode', sa.String(12), nullable=True)
    craeted_at = sa.Column('craeted_at', sa.DateTime, nullable=False, default=datetime.now(timezone.utc))
    updated_at = sa.Column('updated_at', sa.DateTime, nullable=False, default=datetime.now(timezone.utc))
    is_active = sa.Column('is_active', sa.Boolean, nullable=False, default=True)

    def __repr__(self):
        return f"id: {self.id}, username: {self.username}"

