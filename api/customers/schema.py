
from pydantic import BaseModel

class CustomerCreateSchema(BaseModel):
    name: str
    surname: str
    email: str
    phone_number: str

    class Config:
        schema_extra = {
            "example": {
                "name": "Jan",
                "surname": "Kowalski",
                "email": "jan.kowalski@example.com",
                "phone_number": "000-000-000",
            }
        }


class CustomerUpdateSchema(BaseModel):
    name: str | None
    surname: str | None
    email: str | None
    phone_number: str | None

    class Config:
        schema_extra = {
            "example": {
                "name": "Jan",
                "surname": "Kowalski",
                "email": "jan.kowalski@example.com",
                "phone_number": "000-000-000",
            }
        }


class Customer(CustomerCreateSchema):
    id: int


class OrderCreateSchema(BaseModel):
    customer_id: int
    ordered_items: list[int]

    class Config:
        schema_extra = {
            "example": {
                "customer_id": 0,
                "ordered_items": [0, 1, 2, 3],
            }
        }

class OrderUpdateSchema(BaseModel):
    customer_id: int | None
    ordered_items: list[int] | None

    class Config:
        schema_extra = {
            "example": {
                "customer_id": 0,
                "ordered_items": [0, 1, 2, 3],
            }
        }

class Order(OrderCreateSchema):
    id: int

class ProductCreateSchema(BaseModel):
    name: str
    price: float
    info_about: str

    class Config:
        schema_extra = {
            "example": {
                "name": "Product",
                "price": 0.0,
                "info_about": "Information about the product",
            }
        }

class ProductUpdateSchema(BaseModel):
    name: str | None
    price: float | None
    info_about: str | None

    class Config:
        schema_extra = {
            "example": {
                "name": "Product",
                "price": 0.0,
                "info_about": "Information about the product",
            }
        }

class Product(ProductCreateSchema):
    id: int


# class StudentCreateSchema(BaseModel):
#     first_name: str
#     last_name: str

#     class Config:
#         schema_extra = {
#             "example": {
#                 "first_name": "Zbyszek",
#                 "last_name": "Kieliszek",
#             }
#         }


# class StudentUpdateSchema(BaseModel):
#     first_name: str | None
#     last_name: str | None

#     class Config:
#         schema_extra = {
#             "example": {
#                 "first_name": "Zbysiu",
#             }
#         }


# class Student(StudentCreateSchema):
#     id: int


# class Mark(float, Enum):
#     BARDZO_DOBRY = 5.0
#     DOBRY_PLUS = 4.5
#     DOBRY = 4.0
#     DOSTATECZNY_PLUS = 3.5
#     DOSTATECZNY = 3.0
#     NIEDOSTATECZNY = 2.0