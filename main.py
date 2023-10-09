
# ступінь числа
def get_num_pow(number, degree):
    if degree <= 1:
        return number

    return number * get_num_pow(number, degree - 1)


print(get_num_pow(2, 3))

# get_num_pow(2, 3) -> 2 * get_num_pow(2, 2) => 8
# get_num_pow(2, 2) -> 2 * get_num_pow(2, 1) => 4
# get_num_pow(2, 1) => 2

