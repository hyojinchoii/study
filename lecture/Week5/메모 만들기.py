class memo:
    title = ''
    content = ''

    def __init__(self,title, content):
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

type = input('메모입력: 1, 종료 : 0')
while True:
    if type == '1':
        title = input('제목을 입력하세요 \n')
        content = input('내용을 입력하세요\n')
        memo1 = memolist()
        memo1.insertmemo(title,content)
        yn = input('다음 메모를 입력하시겠습니까? y/n')
        if yn == 'y' or yn == 'Y':
            continue
        elif yn == 'n' or yn == 'N':
            break
        else:
            print('잘 못된 값입니다')
            break
    elif type == 0 :
        break




