from bot.orders import place_order
from bot.validators import validate_order

def main():

    print("\n===== Binance Futures Trading Bot =====")

    symbol = input("Enter Symbol (e.g. BTCUSDT): ").upper()
    side = input("Enter Side (BUY/SELL): ").upper()
    order_type = input("Enter Order Type (MARKET/LIMIT): ").upper()
    quantity = float(input("Enter Quantity: "))

    price = None

    if order_type == "LIMIT":
        price = input("Enter Price: ")

    try:
        validate_order(order_type, price)

        response = place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )

        print("\n===== ORDER RESPONSE =====")

        if "error" in response:
            print("Order Failed")
            print(response["error"])
        else:
            print(f"Order ID: {response.get('orderId')}")
            print(f"Status: {response.get('status')}")
            print(f"Symbol: {response.get('symbol')}")
            print(f"Side: {response.get('side')}")

    except Exception as e:
        print(f"Validation Error: {str(e)}")


if __name__ == "__main__":
    main()