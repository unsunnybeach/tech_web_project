from fastapi import APIRouter, HTTPException

from .storage import get_customers_storage, get_orders_storage, get_products_storage
from .schema import (
    Customer,
    CustomerCreateSchema,
    CustomerUpdateSchema,
    Order,
    OrderCreateSchema,
    OrderUpdateSchema,
    Product,
    ProductCreateSchema,
    ProductUpdateSchema,
)

router = APIRouter()


CUSTOMERS_STORAGE = get_customers_storage()
ORDERS_STORAGE = get_orders_storage()
PRODUCTS_STORAGE = get_products_storage()


@router.get("/customers")
async def get_customers() -> list[Customer]:
    return list(get_customers_storage().values())

@router.get("/customers/{customer_id}")
async def get_customer(customer_id: int) -> Customer:
    try:
        return CUSTOMERS_STORAGE[customer_id]
    except KeyError:
        raise HTTPException(
            status_code=404, detail=f"Customer with ID={customer_id} does not exist."
        )

@router.post("/customers")
async def create_customer(customer: CustomerCreateSchema) -> Customer:
    index = len(CUSTOMERS_STORAGE)
    CUSTOMERS_STORAGE[index] = Customer(id=index, **customer.dict())

    return CUSTOMERS_STORAGE[index]

@router.patch("/customers/{customer_id}")
async def update_customer(
    customer_id: int, updated_customer: CustomerUpdateSchema
) -> Customer:
    if customer_id not in CUSTOMERS_STORAGE:
        raise HTTPException(
            status_code=404, detail=f"Customer with ID={customer_id} does not exist."
        )

    customer = CUSTOMERS_STORAGE[customer_id]
    customer_data = updated_customer.dict(exclude_unset=True)

    for key, value in customer_data.items():
        setattr(customer, key, value)

    return customer

@router.delete("/customers/{customer_id}")
async def delete_customer(customer_id: int) -> None:
    try:
        del CUSTOMERS_STORAGE[customer_id]
    except KeyError:
        raise HTTPException(
            status_code=404, detail=f"Customer with ID={customer_id} does not exist."
        )



@router.get("/orders")
async def get_orders() -> list[Order]:
    return list(get_orders_storage().values())

@router.get("/orders/{order_id}")
async def get_order(order_id: int) -> Order:
    try:
        return ORDERS_STORAGE[order_id]
    except KeyError:
        raise HTTPException(
            status_code=404, detail=f"Order with ID={order_id} does not exist."
        )

@router.post("/orders")
async def create_order(order: OrderCreateSchema) -> Order:
    index = len(ORDERS_STORAGE)
    ORDERS_STORAGE[index] = Order(id=index, **order.dict())

    return ORDERS_STORAGE[index]

@router.patch("/orders/{order_id}")
async def update_order(
    order_id: int, updated_order: OrderUpdateSchema
) -> Order:
    if order_id not in ORDERS_STORAGE:
        raise HTTPException(
            status_code=404, detail=f"Order with ID={order_id} does not exist."
        )

    order = ORDERS_STORAGE[order_id]
    order_data = updated_order.dict(exclude_unset=True)

    for key, value in order_data.items():
        setattr(order, key, value)

    return order

@router.delete("/orders/{order_id}")
async def delete_order(order_id: int) -> None:
    try:
        del ORDERS_STORAGE[order_id]
    except KeyError:
        raise HTTPException(
            status_code=404, detail=f"Order with ID={order_id} does not exist."
        )



@router.get("/products")
async def get_products() -> list[Product]:
    return list(get_products_storage().values())

@router.get("/products/{product_id}")
async def get_product(product_id: int) -> Product:
    try:
        return PRODUCTS_STORAGE[product_id]
    except KeyError:
        raise HTTPException(
            status_code=404, detail=f"Product with ID={product_id} does not exist."
        )

@router.post("/products")
async def create_product(product: ProductCreateSchema) -> Product:
    index = len(PRODUCTS_STORAGE)
    PRODUCTS_STORAGE[index] = Product(id=index, **product.dict())

    return PRODUCTS_STORAGE[index]

@router.patch("/products/{product_id}")
async def update_product(
    product_id: int, updated_product: ProductUpdateSchema
) -> Product:
    if product_id not in PRODUCTS_STORAGE:
        raise HTTPException(
            status_code=404, detail=f"Product with ID={product_id} does not exist."
        )

    product = PRODUCTS_STORAGE[product_id]
    product_data = updated_product.dict(exclude_unset=True)

    for key, value in product_data.items():
        setattr(product, key, value)

    return product

@router.delete("/products/{product_id}")
async def delete_product(product_id: int) -> None:
    try:
        del PRODUCTS_STORAGE[product_id]
    except KeyError:
        raise HTTPException(
            status_code=404, detail=f"Product with ID={product_id} does not exist."
        )