import typing
import pandas as pd


def main() -> None:
    customers = pd.read_csv("5784/noahs-customers.csv")
    orders = pd.read_csv("5784/noahs-orders.csv")
    orders_items = pd.read_csv("5784/noahs-orders_items.csv")
    products = pd.read_csv("5784/noahs-customers.csv")

    print(customers)
    print(orders)
    print(orders_items)
    print(products)


if __name__ == "__main__":
    main()
