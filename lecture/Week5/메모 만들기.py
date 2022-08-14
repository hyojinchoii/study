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

