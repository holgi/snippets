# simplified comparison definition
#
# instead of providing all of __lt__(), __le__(), __gt__(), __ge__(),  and
# __eq__() methods on class, only one of  __lt__(), __le__(), __gt__(), or
# __ge__() must be supplied, extra point for an __eq__() method.


from functools import total_ordering

@total_ordering
class CustomNumber():

    def __init__(self, value)
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value
