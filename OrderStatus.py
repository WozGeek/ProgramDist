from config import db

class OrderStatus(OrderStatus.Enum):
    CREATE = 0
    SHIPPING = 1
    DELIVERED = 2
    PAID = 3

t= Table('data', MetaData(), Column('value', Enum(OrderStatus)))

connection.execute(t.insert(), {"value": OrderStatus.SHIPPING})
assert connection.scalar(t.select()) is OrderStatus.SHIPPING