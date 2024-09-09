from random import randint


def generate_numbers():
        numbers = []
        while len(numbers) < 3:
            num = randint(0, 9)
            if num not in numbers:
                numbers.append(num)

        print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
        return numbers


def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    new_guess = []
    while len(new_guess) < 3:
        new_num = int(input(f"{(len(new_guess) + 1)}번째 숫자를 입력하세요: "))

        if new_num < 0 or new_num > 9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        elif new_num in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
        else:
            new_guess.append(new_num)

    return new_guess

def get_score(guesses, solution):
    strike_count = 0
    ball_count = 0

    for i in range(3):
        if guesses[i] == solution[i]:
            strike_count += 1
        elif guesses[i] in solution:
            ball_count += 1

    return strike_count, ball_count

# 여기서부터 게임 시작!
ANSWER = generate_numbers() #답은 한 번 generate number하면 또 반복 할 필요 없이 고정이므로 상수 ANSWER 함수로 정의
tries = 0

while True:
    user_guess = take_guess() # 유저에게 번호 3개를 받는 것은 반복문 안에 있어야 반복적으로 실행이 가능
    s, b = get_score(user_guess, ANSWER) # stike count 와 ball count a, b 함수로 정의하여 가져오기
    # user guess (def take_guess()) 와 ANSWER (def generate_numbers)의 변수로 def get_score에서 return 되는 strike_count, ball_count를 각각 f-string이용해서 s, b로 풀력
    print(f"{s}S {b}B")
    tries += 1

    if s == 3:
        break

print(f"축하합니다. {tries}번 만에 숫자 3개의 값과 위치를 모두 맞히셨습니다.")