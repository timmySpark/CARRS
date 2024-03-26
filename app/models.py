from app import db
from sqlalchemy import Column, Integer, String, Boolean, Float, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid

# Models

class User(db.Model):
    __tablename__ = 'users'

    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(120), nullable=False)
    role = Column(String(15), nullable=False)
    is_verified = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.username}>'

class Car(db.Model):
    __tablename__ = 'cars'

    car_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    make = Column(String(120), nullable=False)
    model = Column(String(120), nullable=False)
    year = Column(Integer)
    price = Column(Float)
    color = Column(String(30), nullable=False)
    transmission = Column(String(120), nullable=False)
    fuel_type = Column(String(120), nullable=False)
    is_verified = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class Booking(db.Model):
    __tablename__ = 'bookings'

    booking_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    car_id = Column(UUID(as_uuid=True), ForeignKey('cars.car_id'))
    pickup_date = Column(DateTime, nullable=False)
    dropoff_date = Column(DateTime, nullable=False)
    price = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)

    car = relationship('Car', backref='bookings')

class Token(db.Model):
    __tablename__ = 'tokens'

    token_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.user_id'))
    token_type = Column(String(25), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship('User', backref='tokens')

class Payment(db.Model):
    __tablename__ = 'payments'

    payment_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    booking_id = Column(UUID(as_uuid=True), ForeignKey('bookings.booking_id'))
    amount = Column(Float)
    payment_method = Column(String(25), nullable=False)
    payment_status = Column(String(25), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    booking = relationship('Booking', backref='payments')
