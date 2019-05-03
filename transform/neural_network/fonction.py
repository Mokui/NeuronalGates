# coding: utf-8
from typing import List


def mean(tab: List[int]) -> int:
    # mean function, secured by strong input and output type
    try:
        value = 0
        total = 0
        for k in tab:
            value += k
            total += 1
        return value / total
    except ZeroDivisionError:
        # try catch to manage empty list in input
        return 0