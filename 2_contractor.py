"""
All that we know, is that in 2017, an order was placed by somebody with the initials JP
for either a coffee or bagel (or both!). We need to find this person. 
"""

import typing
import pandas as pd


# Convert a series of space seperated names to initials
def nameToInitials(fullname: str) -> str:
    return "".join([name[0] for name in fullname.split()])


# Determine if a given SKU is a coffee / bagel
def isOrderCoffeeOrBagel(SKU: str) -> bool:
    # Magic strings pulled from products.csv
    return SKU in ["DLI8820", "BKY1573", "BKY5717"]


# Filter orders and customers data based on date and initials
def initialsSearch(
    df: pd.DataFrame,
    after: str,
    before: str,
    initials: str,
) -> pd.DataFrame:
    # First the ordered column is converted to a datetime
    df["ordered"] = pd.to_datetime(df["ordered"])

    # Next, the frame is filtered based on date and initials.
    filteredOrders = df[
        (df["ordered"] >= after)
        & (df["ordered"] <= before)
        & (df["name"].apply(lambda x: nameToInitials(x) == initials))
    ]

    return filteredOrders


def bagelsCoffeeSearch(df: pd.DataFrame) -> pd.DataFrame:
    return df[df["sku"].apply(lambda x: isOrderCoffeeOrBagel(x))]


def main() -> None:
    customers = pd.read_csv("5784/noahs-customers.csv")
    orders = pd.read_csv("5784/noahs-orders.csv")
    ordersItems = pd.read_csv("5784/noahs-orders_items.csv")
    products = pd.read_csv("5784/noahs-products.csv")

    # Let's join all these together
    ordersItems = ordersItems.merge(products, on="sku")
    orders = orders.merge(ordersItems, on="orderid")
    orders = orders.merge(customers, on="customerid")

    filteredOrders = initialsSearch(orders, "2017-1-1", "2017-12-31", "JP")
    results = bagelsCoffeeSearch(filteredOrders)

    # Lastly, we are interested in the phone number
    print(results["phone"])


if __name__ == "__main__":
    main()
