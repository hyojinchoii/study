import os

print(os.getcwd())

print(os.chdir('C:\최효진\lecture\Week6'))

print(os.getcwd())
print(os.chdir())
print(os.listdir('.'))
# 현재 디렉토리의 목록 확인

# 디렉토리 생성
os.mkdir('meta-data')

# 디렉로리 삭제
os.rmdir('meta-data')

# 다중 디렉토리 생성
os.makedirs('meta-data/log')

# 다중 디렉토리 삭제
os.removedirs('meta-data/log')

# 파일 경로찾기  - pass

import os.path
print(os.getcwd())
os.path.abspath('food_k.txt')

# 파일 이름찾기

import os.path
print(os.getcwd())
os.path.dirname('food_k.txt')

# 디렉토리 존재여부 확인

os.path.exists('C:\최효진\lecture\Week6')

# 파일 사이즈 확인

os.path.getsize('C:\최효진\lecture\Week6')

# 해보기

def makelogfile
    # log 존재여부 확인
    # week6 log 디렉토리 생성
    # count_log 존재여부 확인
    # count_log.txt 파일 생성, 있을 경우 이어쓰기
    # 예외처리 try except 꼭 사용하기

os.path.exists('C:\최효진\lecture\Week6\log')
os.makedirs('C:\최효진\lecture\Week6\log')
os.path.exists('C:\최효진\lecture\Week6\countlog')
os.makedirs('C:\최효진\lecture\Week6\count_log.txt')

    import os
    try:
        os.chdir('C:\최효진\lecture\Week6')
        if not os.path.exists('log'):
            os.mkdir('log')

        if not os.path.isfile()




    except FileNotFoundError as e:
        print('파일없음',e)
    except FileExistsError as e:
        print('파일있음',e)
    except Exception as e:
        print('오류발생',e)