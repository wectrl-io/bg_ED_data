#!/usr/bin/env python
# -*- coding: utf8 -*-

import providers.electrohold.prices as el_prices
import providers.electrohold.outages as el_outages


def main():
    print("Starting work...")

    check_id = 123456789101

    print("Electricity outages data:")
    print(el_outages.get_outages(check_id))

    print("Electricity prices data:")
    print(el_prices.get_prices())

    print("Finitto!")



if __name__ == "__main__":
    main()
