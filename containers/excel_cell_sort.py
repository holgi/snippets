""" Sort the content of an list containing excel cells

> l = ["A2", "A10", "AA3", "AB1"]
> sorted(l)
['A10', 'A2', 'AA3', 'AB1']
> excel_cell_sort(l)
['A2', 'A10', 'AA3', 'AB1']

from http://www.codinghorror.com/blog/2007/12/sorting-for-humans-natural-sort-order.html
"""

import re


_NATURAL_SORT_REGEX_DIGITS = re.compile("([0-9]+)")


def _nartural_sort_convert(text):
    return int(text) if text.isdigit() else text.lower()


def _nartural_sort_alphanum_key(text):
    return tuple(
        _nartural_sort_convert(part)
        for part in _NATURAL_SORT_REGEX_DIGITS.split(text)
    )


def _excel_cell_sort_key(cell):
    nat_sort_result = _nartural_sort_alphanum_key(cell)
    column, row = nat_sort_result[:2]
    return tuple((len(column), column, row))


def excel_cell_sort(iterable):
    return sorted(iterable, key=_excel_cell_sort_key)


