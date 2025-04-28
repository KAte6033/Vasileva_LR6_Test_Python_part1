# # Ввод целого числа Q
# def input_Q():
#     Q = int(input("Введите целое число Q: "))

# # Ввод натурального числа P, которое меньше Q
# P = int(input("Введите натуральное число P (меньше Q): "))
# while P <= 0 or P >= Q:
#     print("Ошибка: P должно быть натуральным и меньше Q.")
#     P = int(input("Введите натуральное число P (меньше Q): "))

# def is_digit_not_negative(user_input):
#     if not user_input.strip():
#         return False
#     try:
#         number = int(user_input)
#         if number < 0 or number == 0:
#             return False
#     except ValueError:
#         return False
#     return True



def is_digit_not_negative(user_input):
    if not user_input.strip():
        return False
    try:
        number = int(user_input)
        if number < 0 or number == 0:
            return False
    except ValueError:
        return False
    return True


def input_positive_integer ():
    promt = "Введите целое положительное число: "
    user_input = input(promt)
    while not is_digit_not_negative(user_input):
        print("Ошибка: значение введено неправильно. Попробуйте снова.")
        user_input = input(promt)
    return int(user_input)


def mod_Q_on_P(q, p):
    # div = q // p
    return (q % p)

def div_Q_on_P(q, p):
    # div = q // p
    # return q // p
    return (q // p)

