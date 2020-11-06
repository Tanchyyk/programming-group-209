"""
This is the "sieve_flavius" module.

The module supplies two functions, remove_even_numbers(),
 sieve_flavius().  For example,

>>> remove_even_numbers([1, 2, 3, 4, 5])
[1, 3, 5]
>>> sieve_flavius(10)
[1, 3, 7, 9]
"""

def remove_even_numbers(arr: list) -> list:
    """
    Function removes even numbers from the list.
    >>> remove_even_numbers([1, 2, 3])
    [1, 3]
    """
    for i in arr:
        if i % 2 == 0:
            arr.remove(i)
    return arr


def sieve_flavius(num: int) -> list:
    """
    Function returns lucky numbers.
    >>> sieve_flavius(10)
    [1, 3, 7, 9]
    """
    if num < 1:
        return []

    list_of_numbers = list(range(1, num + 1))
    list_of_numbers = remove_even_numbers(list_of_numbers)

    i = 1
    while list_of_numbers[i] <= len(list_of_numbers):
        new_list = []
        for j in range(len(list_of_numbers)):
            if (j + 1) % list_of_numbers[i] != 0:
                new_list.append(list_of_numbers[j])

        list_of_numbers = new_list
        i += 1
    return list_of_numbers
