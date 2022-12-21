class MyError(Exception):
    def __init__(self, error):
        self.error = error


def choice_1():
    matrix_a = []
    matrix_b = []
    num = "0123456789"

    while True:
        try:
            size_a = input("Enter size of first matrix:\n> ")
            size_a = size_a.split(sep=" ")
            if len(size_a) > 2 or len(size_a) < 2 or str(size_a[0]) not in num or str(size_a[1]) not in num:
                raise MyError(f'Incorrect input!\nYou should enter the size, like "3 3", "4 5", etc.\n')
            break
        except MyError as err:
            print(err)
        except Exception as err:
            print(err)

    print("Enter first matrix:")
    for z in range(int(size_a[0])):
        while True:
            try:
                elem = input("> ")
                elem = elem.split(sep=" ")
                if int(len(elem)) > int(size_a[1]) or int(len(elem)) < int(size_a[1]):
                    raise MyError(f'You should enter only {size_a[1]} numbers in line!')
                else:
                    matrix_a.append(elem)
                    break
            except MyError as no:
                print(no)

    int_matrix_a = []
    new_list_a = []
    for c in range(int(size_a[0])):
        for x in matrix_a[c]:
            i = int(x)
            new_list_a.append(i)
        int_matrix_a.append(new_list_a)
        new_list_a = []

    while True:
        try:
            size_b = input("Enter size of second matrix:\n> ")
            size_b = size_b.split(sep=" ")
            if len(size_b) > 2 or len(size_b) < 2 or str(size_b[0]) not in num or str(size_b[1]) not in num:
                raise MyError(f'Incorrect input!\nYou should enter the size, like "3 3", "4 5", etc.\n')
            if size_b != size_a:
                raise MyError("The size of the second matrix must be the same as size of the first matrix!")
            break
        except MyError as err:
            print(err)
        except Exception as err:
            print(err)

    print("Enter second matrix:")
    for z in range(int(size_b[0])):
        while True:
            try:
                elem = input("> ")
                elem = elem.split(sep=" ")
                if int(len(elem)) > int(size_b[1]) or int(len(elem)) < int(size_b[1]):
                    raise MyError(f'You should enter only {size_b[1]} numbers in line!')
                else:
                    matrix_b.append(elem)
                    break
            except MyError as no:
                print(no)

    int_matrix_b = []
    new_list_b = []
    for c in range(int(size_b[0])):
        for x in matrix_b[c]:
            i = int(x)
            new_list_b.append(i)
        int_matrix_b.append(new_list_b)
        new_list_b = []

    print("The result is:")
    for i in range(int(size_b[0])):
        k = 0
        for x in int_matrix_a[i]:
            x += int_matrix_b[i][k]
            print(x, end=" ")
            k += 1
        print()


def choice_2():
    matrix = []
    num = "0123456789"
    while True:
        try:
            size = input("Enter size of matrix:\n> ")
            size = size.split(sep=" ")
            if len(size) > 2 or len(size) < 2 or str(size[0]) not in num or str(size[1]) not in num:
                raise MyError(f'Incorrect input!\nYou should enter the size, like "3 3", "4 5", etc.\n')
            break
        except MyError as err:
            print(err)
        except Exception as err:
            print(err)

    print("Enter matrix:")
    for z in range(int(size[0])):
        while True:
            try:
                elem = input("> ")
                elem = elem.split(sep=" ")
                if int(len(elem)) > int(size[1]) or int(len(elem)) < int(size[1]):
                    raise MyError(f'You should enter only {size[1]} numbers in line!')
                else:
                    matrix.append(elem)
                    break
            except MyError as no:
                print(no)
    int_matrix = []
    list_m = []
    for c in range(int(size[0])):
        for x in matrix[c]:
            i = float(x)
            list_m.append(i)
        int_matrix.append(list_m)
        list_m = []
    while True:
        try:
            cons = float(input("Enter constant:\n> "))
            break
        except ValueError:
            print("Incorrect input! You must enter a number and only one.")
    print("The result is:")
    for i in range(int(size[0])):
        for x in int_matrix[i]:
            x *= cons
            print(x, end="  ")
        print()


def choice_3():
    matrix_a = []
    num = "0123456789"
    matrix_b = []

    while True:
        try:
            size_a = input("Enter size of first matrix:\n> ")
            size_a = size_a.split(sep=" ")
            if len(size_a) > 2 or len(size_a) < 2 or str(size_a[0]) not in num or str(size_a[1]) not in num:
                raise MyError(f'Incorrect input!\nYou should enter the size, like "3 3", "4 5", etc.\n')
            break
        except MyError as err:
            print(err)
        except Exception as err:
            print(err)

    print("Enter first matrix:")
    for z in range(int(size_a[0])):
        while True:
            try:
                elem = input("> ")
                elem = elem.split(sep=" ")
                if int(len(elem)) > int(size_a[1]) or int(len(elem)) < int(size_a[1]):
                    raise MyError(f'You should enter only {size_a[1]} numbers in line!')
                else:
                    matrix_a.append(elem)
                    break
            except MyError as no:
                print(no)

    int_matrix_a = []
    new_list_a = []
    for c in range(int(size_a[0])):
        for x in matrix_a[c]:
            i = int(x)
            new_list_a.append(i)
        int_matrix_a.append(new_list_a)
        new_list_a = []

    while True:
        try:
            size_b = input("Enter size of second matrix:\n> ")
            size_b = size_b.split(sep=" ")
            if len(size_b) > 2 or len(size_b) < 2 or str(size_b[0]) not in num or str(size_b[1]) not in num:
                raise MyError(f'Incorrect input!\nYou should enter the size, like "3 3", "4 5", etc.\n')
            break
        except MyError as err:
            print(err)
        except Exception as err:
            print(err)

    print("Enter second matrix:")
    for z in range(int(size_b[0])):
        while True:
            try:
                elem = input("> ")
                elem = elem.split(sep=" ")
                if int(len(elem)) > int(size_b[1]) or int(len(elem)) < int(size_b[1]):
                    raise MyError(f'You should enter only {size_b[1]} numbers in line!')
                else:
                    matrix_b.append(elem)
                    break
            except MyError as no:
                print(no)

    int_matrix_b = []
    new_list_b = []
    for c in range(int(size_b[0])):
        for x in matrix_b[c]:
            i = int(x)
            new_list_b.append(i)
        int_matrix_b.append(new_list_b)
        new_list_b = []

    result = []
    for i in range(len(int_matrix_a)):
        string = []
        for d in range(len(int_matrix_b[0]))
            number = 0
            for k in range(len(int_matrix_a[0])):
                number += int_matrix_a[i][k] * int_matrix_b[k][d]
            string.append(number)
        result.append(string)

    print("The result is:")
    for i in range(len(result)):
        for x in result[i]:
            print(x, end=" ")
        print()


 def choice_4():
            print("""1. Main diagonal
        2. Side diagonal
        3. Vertical line
        4. Horizontal line""")

            while True:
                try:
                    good = "1234"
                    choice_t = input("\nEnter your choice: 1, 2, 3 or 4:\n> ")
                    if choice_t not in good:
                        raise MyError("Incorrect input, try again")
                    break
                except MyError as no:
                    print(no)

            while True:
                try:
                    num = "0123456789"
                    size = input("Enter size of matrix:\n> ")
                    size = size.split(sep=" ")
                    if len(size) > 2 or len(size) < 2 or str(size[0]) not in num or str(size[1]) not in num:
                        raise MyError(f'Incorrect input!\nYou should enter the size, like "3 3", "4 5", etc.\n')
                    break
                except MyError as err:
                    print(err)
                except Exception as err:
                    print(err)

            matrix = []
            print("Enter matrix:")
            for z in range(int(size[0])):
                while True:
                    try:
                        elem = input("> ")
                        elem = elem.split(sep=" ")
                        if int(len(elem)) > int(size[1]) or int(len(elem)) < int(size[1]):
                            raise MyError(f'You should enter only {size[1]} numbers in line!')
                        else:
                            matrix.append(elem)
                            break
                    except MyError as no:
                        print(no)

            int_matrix = []
            new_list = []
            for c in range(int(size[0])):
                for x in matrix[c]:
                    i = int(x)
                    new_list.append(i)
                int_matrix.append(new_list)
                new_list = []

            result = []
            for i in range(len(int_matrix)):
                string = []
                for d in range(len(int_matrix[0])):
                    number = 0
                    for k in range(1):
                        number += int_matrix[d][i]
                    string.append(number)
                result.append(string)

            print("The result is:")
            if choice_t == "1":
                for i in range(len(result)):
                    for x in result[i]:
                        print(x, end=" ")
                    print()

            elif choice_t == "2":
                for c in range(len(result)):
                    result[c].reverse()
                result.reverse()
                for i in range(len(result)):
                    for x in result[i]:
                        print(x, end=" ")
                    print()

            elif choice_t == "3":
                for c in range(len(int_matrix)):
                    int_matrix[c].reverse()
                for i in range(len(int_matrix)):
                    for x in int_matrix[i]:
                        print(x, end=" ")
                    print()

            elif choice_t == "4":
                int_matrix.reverse()
                for i in range(len(int_matrix)):
                    for x in int_matrix[i]:
                        print(x, end=" ")
                    print()


while True:
    try:
        print("""\n1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
0. Exit""")

        choice = input("\nEnter your choice: 1, 2, 3, 4 or 0:\n> ")

        if choice == "1":
            print("ATTENTION! The size of the two matrices must be the same!")
