print("1. Number degree/n2. Stars/n3. Range numbers")
user_select = int(input("Enter menu item: "))
# ступінь числа


def get_num_pow(number, degree):
    if degree <= 1:
        return number

    return number * get_num_pow(number, degree - 1)


# get_num_pow(2, 3) -> 2 * get_num_pow(2, 2) => 8
# get_num_pow(2, 2) -> 2 * get_num_pow(2, 1) => 4
# get_num_pow(2, 1) => 2


# зірки в ряд
def print_stars(n):
    if n != 0:
        print("*", end="")
        print_stars(n - 1)


# N = 5
# print_stars(5) => print_stars(5 - 1) => N = 4
# print_stars(4) => print_stars(4 - 1) => N = 3
# print_stars(3) => print_stars(3 - 1) => N = 2
# print_stars(2) => print_stars(2 - 1) => N = 1


# сума чисел в діапазоні
def sum_num(a, b):
    if a > b:
        return 0
    else:
        return a + sum_num(a + 1, b)


# a1 = 2
# b1 = 5
# sum_num(2, 5) => sum_num(2 + 1, 5) => 14
# sum_num(3, 5) => sum_num(3 + 1, 5) => 12
# sum_num(4, 5) => sum_num(4 + 1, 5) => 9
# sum_num(5, 5) => 5


match user_select:
    case 1:
        print(get_num_pow(2, 3))

    case 2:
        try:
            N = int(input("Enter number: "))
            print_stars(N)
        except ValueError:
            print("Enter only numbers please!")
        except Exception as e:
            print(f"Error: {e}")
    case 3:
        try:
            a1 = int(input("Enter a: "))
            b1 = int(input("Enter b: "))
            result = sum_num(a1, b1)
            print(f"Sum_num {result}")
        except ValueError:
            print("Enter only numbers please!")
        except Exception as e:
            print(f"Error: {e}")
    case _:
        print("Error!!!")
