
# ступінь числа
def get_num_pow(number, degree):
    if degree <= 1:
        return number

    return number * get_num_pow(number, degree - 1)


print(get_num_pow(2, 3))

# get_num_pow(2, 3) -> 2 * get_num_pow(2, 2) => 8
# get_num_pow(2, 2) -> 2 * get_num_pow(2, 1) => 4
# get_num_pow(2, 1) => 2


# зірки в ряд
def print_stars(n):
    if n != 0:
        print("*", end="")
        print_stars(n - 1)


try:
    N = int(input("Enter number: "))
    print_stars(N)
except ValueError:
    print("Enter only numbers please!")
except Exception as e:
    print(f"Error: {e}")


# N = 5
# print_stars(5) => print_stars(5 - 1) => N = 4
# print_stars(4) => print_stars(4 - 1) => N = 3
# print_stars(3) => print_stars(3 - 1) => N = 2
# print_stars(2) => print_stars(2 - 1) => N = 1
