
# Find out how many rabbits are after N years knowing the following:
# n_years = input
# number_rabbits = input
# rabbits_births_number = input
# *Each rabbit can give birth only within the first two years
# *Rabbits live only four years.


def return_number_of_rabbits():
    """
    This method computes the number of rabbits after n years after the following logic:
        After a year the number of rabbits is:
        total_rabbits = initial_rabbits + fertile_rabbits * rabbits_births_number - old_rabbits, where:
            initial_rabbits would be the number of rabbits from the beginning of the year
            fertile_rabbits would be the number of rabbits that are fertile in the year, considering the fact that
            rabbits are fertile only in the first two years
            old_rabbits is the number of rabbits that are more that 4 years old
    :return: The number of rabbits after N years
    """

    n_years = int(input("Please input the number of years after you what to do the calculus: "))
    number_rabbits = int(input("Please input the current number of rabbits: "))
    rabbits_births_number = int(input("Please input the number of rabbits that can occur from a birth: "))

    rabbits = [number_rabbits]
    actual = number_rabbits

    for i in range(n_years):
        initial = actual
        if i < 2:
            fertile = initial
        else:
            fertile = initial - rabbits[i-2]

        new_born = fertile * rabbits_births_number

        if i < 4:
            old = 0
        else:
            old = rabbits[i-4]

        actual = initial + new_born - old
        rabbits.append(new_born)

    return f"The number of rabbits after {n_years} years is: {actual}"


print(return_number_of_rabbits())
