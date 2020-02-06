""" Sort the conten of an list in a natural way

> l = ["A2", "A10", "A1", "A3"]
> sorted(l)
['A1', 'A10', 'A2', 'A3']
> natural_sort(l)
['A1', 'A2', 'A3', 'A10']

from http://www.codinghorror.com/blog/2007/12/sorting-for-humans-natural-sort-order.html
"""

import re


_NATURAL_SORT_REGEX_DIGITS = re.compile("([0-9]+)")


def _nartural_sort_convert(text):
    return int(text) if text.isdigit() else text.lower()


def _nartural_sort_alphanum_key(text):
    return (
        _nartural_sort_convert(part)
        for part in _NATURAL_SORT_REGEX_DIGITS.split(text)
    )


def natural_sort(iterable):
    return sorted(iterable, key=_nartural_sort_alphanum_key)
