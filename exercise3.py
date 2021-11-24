
# Define a function that receive a list with numbers and strings and return a list only with the
# numbers without duplicates.
# to_be_used = [1, 3, 67, "1", "62", "Foo", "3", 5, 1, 3, False, 1.3]


def remove_duplicates(list_of_duplicates: list) -> list:
    list_without_duplicates = list(set(list_of_duplicates))
    returned_list = []

    for element in list_without_duplicates:
        if isinstance(element, int) or isinstance(element, float):
            if isinstance(element, bool):
                continue
            else:
                returned_list.append(element)

    return returned_list


print(remove_duplicates([1, 3, 67, "1", "62", "Foo", "3", 5, 1, 3, False, 1.3]))
