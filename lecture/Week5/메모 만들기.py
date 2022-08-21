seq = 0

class memo:
    no = 0
    title = ''
    content = ''

    def __init__(self,title, content):
        global seq
        seq += 1
        self.no = seq
        self.title = title
        self.content = content

    def setcontent(self, content):
        self.content = content

    def getcontent(self):
        return self.content

class memolist:
    memo_list = []
    def insertmemo(self,title,content):
        self.memo_list.append(memo(title,content))

    def selectmemo(self):
        for memo in self.memo_list:
            print('===============')
            print('번호:',memo.no)
            print('번호:', memo.title)
            print('번호:', memo.content)

    def getmemo(self, s_word,type):
        if type == 1:
            for memo in self.memo_list:
                if memo.no == s_word:
                    print('===============')
                    print('번호:', memo.no)
                    print('번호:', memo.title)
                    print('번호:', memo.content)
        elif type == 2:
            for memo in self.memo_list:
                if s_word in memo.title:
                    print('===============')
                    print('번호:', memo.no)
                    print('번호:', memo.title)
                    print('번호:', memo.content)
        elif type == 3:
            for memo in self.memo_list:
                if s_word in memo.content:
                    print('===============')
                    print('번호:', memo.no)
                    print('번호:', memo.title)
                    print('번호:', memo.content)

while True:
    type = input('메모입력: 1, 메모선택: 2, 메모목록: 3, 종료 : 0 \n')
    if type == '1':
            while True:
                title = input('제목을 입력하세요 \n')
                content = input('내용을 입력하세요\n')
                memo1 = memolist()
                memo1.insertmemo(title,content)
                yn = input('다음 메모를 입력하시겠습니까? y/n')
                if yn == 'y' or yn == 'Y':
                    continue
                elif yn == 'n' or yn == 'N':
                    print('종료')
                    break
                else:
                    print('잘 못된 값입니다')
                    break
    elif type == '3':
        memo1 = memolist()
        memo1.selectmemo()

    elif type == '2':
        while True:
            search_type = int(input('메모번호: 1, 제목검색: 2, 내용검색: 3, 종료 : 0 \n'))
            if search_type == 1:
                s_word = input('확인할 메모 번호를 입력하세요\n')
                memo1.getmemo(s_word,1)
            elif search_type == 2:
                s_word = input('검색할 제목을 입력하세요\n')
                memo1.getmemo(s_word, 2)
            elif search_type == 3:
                s_word = input('검색할 내용을 입력하세요\n')
                memo1.getmemo(s_word, 3)
            else :
                break

    elif type == '0':
        break



