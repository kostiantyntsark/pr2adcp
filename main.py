import random

number = random.randint(1, 10)
guess = int(input("Вгадай число від 1 до 10: "))

if guess == number:
    print("🎉 Вітаю! Ти вгадав!")
else:
    print(f"❌ Ні! Правильне число було: {number}")