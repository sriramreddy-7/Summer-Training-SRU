def is_palindrome(num):
    original = num
    reversed = 0

    while num > 0:
        digit = num % 10
        reversed = reversed * 10 + digit
        num = num // 10

    return original == reversed


def next_palindrome(num):
    num += 1
    while not is_palindrome(num):
        num += 1
    return num


user_input = int(input("Enter a number: "))

result = next_palindrome(user_input)
print("The next palindrome is:", result)