# Функція додавання двох чисел
def add(num1, num2):
    return num1 + num2


# Функція віднімання двох чисел

def subtract(num1, num2):
    return num1 - num2


# Функція для множення двох чисел

def multiply(num1, num2):
    return num1 * num2


# Функція поділу двох чисел
def divide(num1, num2):
    return num1 / num2


def ostacha(num1, num2):
    a = num1 % num2
    return (a)


print("Виберіть операцію -\n" \
      "1. Додати\n" \
      "2. Відняти\n" \
      "3. Помножити\n" \
      "4.1.Остача від ділення\n" \
      "4. Розділити\n")

select = input("Вибір форми операції 1, 2, 3, 4, 4.1 :")

число_1 = int(input("Введіть перше число: "))
число_2 = int(input("Введіть друге число: "))

if select == '1':
    print(число_1, "+", число_2, "=",
          add(число_1, число_2))

elif select == '2':
    print(число_1, "-", число_2, "=",
          subtract(число_1, число_2))

elif select == '3':
    print(число_1, "*", число_2, "=",
          multiply(число_1, число_2))

elif select == '4':
    print(число_1, "/", число_2, "=",
          divide(число_1, число_2))

elif select == '4.1':
    print(число_1, "%", число_2, "=",
          ostacha (число_1, число_2))
else:
    print("Неправильні дані")
