"""
In the customers database, there exists a customer whose last name is equal to 
there phone number, when written on a dialpad.  

    1        2        3
 (     )  ( abc )  ( def )
    4        5        6
 ( ghi )  ( jkl )  ( mno )
    7        8        9
 ( pqrs)  ( tuv )  ( wxyz)
             0
          (     )

That is to say "Bob" would map to 262
"""

import typing
import pandas as pd


# A list, where each index contains the corresponding letters from the dialpad.
digitToLetters = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]


def nameEqualsPhone(name: str, phone: str) -> bool:
    # Names are space seperated, but may have more than 2
    cleanName = name.split()[-1].lower()
    # Phone numbers are - seperated
    cleanPhone = phone.replace("-", "")

    # Both should be the same length
    if len(cleanName) != len(cleanPhone):
        return False

    # If they are, we need to check each digit.
    for letter, digit in zip(cleanName, cleanPhone):
        if letter not in digitToLetters[int(digit)]:
            return False

    # If all letters match the digits, then we have a winner!
    return True


def main() -> None:
    customers = pd.read_csv("5784/noahs-customers.csv")

    matches = [
        (name, phone)
        for name, phone in zip(customers["name"], customers["phone"])
        if nameEqualsPhone(name, phone)
    ]

    print(matches)


if __name__ == "__main__":
    main()
