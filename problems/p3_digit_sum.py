def digit_sum(n):
    n = abs(n)

    if n == 0:
        return 0

    return (n % 10) + digit_sum(n // 10)


n = int(input("Enter a number: "))
print("Sum of digits:", digit_sum(n))
