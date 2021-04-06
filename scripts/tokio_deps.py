#!/usr/bin/env python3.9
# pip3 install pandas
import os
import pandas


def things():
    runs = pandas.read_parquet("./subtrees-clean.parquet")
    return runs


if __name__ == "__main__":
    things()
