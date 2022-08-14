import random

def RSPgame() :
    rsp = [ 'rock', 'sissor', 'paper']
    my_rsp = input ('가위바위보 게임을 시작할까요? 가위: s, 바위: r, 보: p')

    dict_rsp = {'r':'rock', 's':'sissor', 'p':'paper'}
    ai_choice = random.choice(rsp)
    my_choice = dict_rsp.get(my_rsp)

    print(ai_choice)
    print(my_choice)
    if my_choice == None :
        print('무효입니다.')
        game_result = 'err'


    if my_choice == 'r' and ai_choice == 'p' or\
        my_choice == 's' and ai_choice == 'r' or\
        my_choice == 'p' and ai_choice == 's':

        print("당신은 졌습니다")
        game_result = -1

    elif my_choice == 'r' and ai_choice == 'r' or\
        my_choice == 's' and ai_choice == 's' or\
        my_choice == 'p' and ai_choice == 'p':

        print("당신은 비겼습니다")
        game_result = 0

    else:
        print("당신은 이겼습니다")
        game_result = 1
    return game_result

def getstartRSPgame(cnt):
i = 0
while i < 10:
    RSPgame()
    i += 1

    print(game_result_set)
    print("승:{} 패:{} 무:{}".format(game_result_set.count(1), \
                               game_result_set.count(-1),\
                               game_result_set.count(0)))