def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    new_guess = []

    while len(new_guess) < 3:
        one_num = input("1번쨰 숫자를 입력하세요: ")

        if int(one_num) < 0 or int(one_num) > 9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        elif int(one_num) in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요")
        else:
            new_guess.append(one_num)

            two_num = input("2번째 숫자를 입력하세요: ")


            if int(two_num) < 0 or int(two_num) > 9:
                print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
            elif int(two_num) in new_guess:
                print("중복되는 숫자입니다. 다시 입력하세요")
            else:
                new_guess.append(two_num)

                three_num = input("3번째 숫자를 입력하세요: ")

                if int(three_num) < 0 or int(three_num) > 9:
                    print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
                elif int(three_num) in new_guess:
                    print("중복되는 숫자입니다. 다시 입력하세요")
                else:
                    new_guess.append(three_num)



    return new_guess


# 테스트 코드
print(take_guess())