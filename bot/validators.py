def validate_order(order_type, price=None):
    order_type = order_type.upper()

    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Invalid order type")

    if order_type == "LIMIT" and price is None:
        raise ValueError("Price required for LIMIT order")