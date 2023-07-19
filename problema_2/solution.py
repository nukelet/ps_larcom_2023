"""
Reverse a list in-place in O(n) time and O(1) space.
"""
def invert_list(input: list):
    size = len(input)
    midpoint = int(size/2)
    # swap the first and last elements, then the second and second-to-last,
    # and so on
    for i in range(0, midpoint):
        tmp = input[i]
        input[i] = input[size - i - 1]
        input[size - i - 1] = tmp

def test_even_length():
    data = [1, 2, 3, 4, 5, 6]
    input = list(data) # copy the list since the inversion is in-place
    invert_list(input)
    assert input == data[::-1]

def test_odd_length():
    data = [1, 2, 3, 4, 5]
    input = list(data) # copy the list since the inversion is in-place
    invert_list(input)
    assert input == data[::-1]

test_even_length()
test_odd_length()
