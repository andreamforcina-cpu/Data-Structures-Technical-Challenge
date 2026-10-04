"""
Timed Challenge - Question 7: First Repeated Value

Return the first value that repeats in the collection.

Input: [1, 4, 3, 5, 3, 2, 1]
Output: 3
"""


def first_repeated_value(values):
    # Make sure the input is a list
    if not isinstance(values, list):
        return None

    seen = set()

    for value in values:
        if value in seen:
            return value

        seen.add(value)

    return None


# Tests

print(first_repeated_value([1, 4, 3, 5, 3, 2, 1]))  # 3
print(first_repeated_value([1, 2, 3, 4, 5]))        # None
print(first_repeated_value([]))                     # None
print(first_repeated_value([5, 5]))                 # 5
print(first_repeated_value("not a list"))           # None


"""
Reflection

For this timed challenge, I chose to use a set as my main data structure.
The problem asks me to find the first value that appears more than once, so
I needed a way to quickly check if I had already seen a value. A set works
well for this because checking whether a value is already inside a set is
usually an O(1) operation. This means I can go through the list only once,
giving the solution an overall time complexity of O(n).

The 30-minute time limit made me focus on creating a simple plan before
starting to write the code. Instead of immediately jumping into coding, I
first thought about what the problem was asking, what cases I needed to
consider, and which data structure would make the solution efficient. Once
I had this small plan, writing the actual code became much easier because
I already knew what I wanted each part of the program to do.

One trade-off with using a set is that it requires additional memory because
I have to store the values that I have already seen. However, I think this
is a good trade-off because it makes searching much faster than repeatedly
checking previous values in a list. Under the time pressure, I also focused
on keeping the solution simple instead of making it unnecessarily complex.
I tested the function with the example input, a list with no duplicates,
an empty list, an immediate duplicate, and an incorrect data type. Overall,
planning before coding helped me stay organized and complete the problem
more confidently.
"""