import random

def guess_the_number():
    # game code
    secret_number = random.randint(1, 10)
    attempts = 0

    print("1부터 10까지의 숫자 중 하나를 맞춰보세요!")

    while True:
        user_guess = int(input("추측한 숫자를 입력하세요: "))
        attempts += 1

        if user_guess == secret_number:
            print(f"축하합니다! {attempts}번만에 숫자를 맞추셨습니다.")
            break
        elif user_guess < secret_number:
            print("좀 더 큰 숫자를 선택하세요.")
        else:
            print("좀 더 작은 숫자를 선택하세요.")

if __name__ == "__main__":
    guess_the_number()