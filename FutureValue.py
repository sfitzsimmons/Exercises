# this exercise asks me to compute the future value of a specified principal amount, rate of interest, and a number of
# years.

principle_amount = 10000
rate_of_interest = 3.5
years = 7


def future_amount(principle, roi, duration):

    current = principle
    for i in range(duration):
        interest = current * (roi * .01)
        current += interest
    return round(current, 2)


print(future_amount(principle_amount, rate_of_interest, years))
