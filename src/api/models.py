from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Table, Column, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
import secrets
from datetime import datetime, timedelta

db = SQLAlchemy()

shopping_cart = Table(
    'shopping_cart',
    db.metadata,Column("id", Integer, primary_key=True),
    Column('amount', Integer, nullable=False),
    Column("fk_product", ForeignKey("products.id"), nullable=False),
    Column("fk_user", ForeignKey("user.id"), nullable=False)
)

class User(db.Model):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    first_name: Mapped[str] = mapped_column(String(60), nullable=False)
    last_name: Mapped[str] = mapped_column(String(60), nullable=False)
    address: Mapped[str] = mapped_column(String(120), nullable=False)
    role: Mapped[str] = mapped_column(String(20), nullable=False, default="user")  # Default role is 'user'

    reset_token: Mapped[str] = mapped_column(nullable=True)
    reset_token_expires: Mapped[datetime] = mapped_column(nullable=True)

    products: Mapped[List["Products"]] = relationship(secondary=shopping_cart, back_populates="users")

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "address": self.address,
            "role": self.role
        }
        
    def generate_reset_token(self):
        self.reset_token = secrets.token_urlsafe(32)
        self.reset_token_expires = datetime.utcnow() + timedelta(hours=1)

class Products(db.Model):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    product_name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    price: Mapped[int] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(String(320), nullable=False)
    color: Mapped[str] = mapped_column(nullable=False)
    product_type: Mapped[str] = mapped_column(nullable=False)
    gender: Mapped[str] = mapped_column(nullable=False)
    size: Mapped[str] = mapped_column(nullable=False)
    stock: Mapped[int] = mapped_column(nullable=False, default=0)
    product_photo: Mapped[str] = mapped_column(String(120), nullable=True)
    
    users: Mapped[List["User"]] = relationship(secondary=shopping_cart, back_populates="products")

    def serialize(self):
        return {
            "id": self.id,
            "product_name": self.product_name,
            "price": self.price,
            "description": self.description,
            "color": self.color,
            "product_type": self.product_type,
            "gender": self.gender,
            "size": self.size,
            "stock": self.stock,
            "product_photo": self.product_photo
            
        }