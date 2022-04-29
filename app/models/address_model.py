from uuid import uuid4

from app.configs.database import db
from marshmallow import Schema, fields
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class AddressModel(db.Model):
    __tablename__ = 'address'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    street = Column(String, nullable=False)
    number = Column(Integer, nullable=False)
    complement = Column(String, nullable=False)
    state = Column(String, nullable=False)
    cep = Column(String,nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))

    users = relationship('UserModel', backref='address', uselist=False)


class AddressSchema(Schema):
    class Meta:
       ordered = True
       include_fk = True

    street = fields.Str()
    number = fields.Integer()
    complement = fields.Str()
    state = fields.Str()
    cep = fields.Str()