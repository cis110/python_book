print("Is 2024 a leap year?")
print(((2024 % 4 == 0) and (2024 % 100 != 0)) or (2024 % 400 == 0))

print("Is 2025 a leap year?")
print(((2025 % 4 == 0) and (2025 % 100 != 0)) or (2025 % 400 == 0))

print("Is 2000 a leap year?")
print(((2000 % 4 == 0) and (2000 % 100 != 0)) or (2000 % 400 == 0))

# The code above is repeated three times. We can use variables to make the code more readable.

year = 2024
print(((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0))


year = 2024
print(year)
print("Calculating if above year is a leap year...")

divisible_by_4 = year % 4 == 0
divisible_by_100 = year % 100 == 0
divisible_by_400 = year % 400 == 0
is_leap_year = (divisible_by_4 and not divisible_by_100) or divisible_by_400
print(is_leap_year)
