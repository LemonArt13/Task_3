num = input("Введіть ціле число у форматі XXXXX: ")

def histogram(num):
    if num.isdigit():

        digits = [int(digit) for digit in num]

        max_digit = max(digits)

        print(" ".join(map(str, digits)))

        print("_" * (len(digits) * 2))

        for i in range(max_digit, 0, -1):
            row = ""
            for digit in digits:
                if digit >= i:
                    row += "# "
                else:
                    row += "  "
            print(row)
    else:
        print("Error \nВведене значення не є цілим числом. ")

histogram(num)