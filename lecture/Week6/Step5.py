# import os
#
# text_data_path= 'C:\최효진\lecture\Week6\meta-data\store1'
#
# file_list = os.listdir(text_data_path)
#
# text_list = []
# for file in file_list:
#     print(file)
#     file_path = text_data_path + '/' + file
#     try:
#
#     # 파일 존재여부 꼭 확인
#         if os.path.isfile(file_path):
#             f =open(file_path, 'r', encoding = 'utf-8')
#             text_list.append(f.read().split('\n'))
#             print(text_list)
#     except Exception as e:
#         print(e)
#     finally:
#         pass
#
# order_data = dict()
#
# for data in text_list:
#     for each_data in data:
#         print(each_data)
#         order = each_data.split(',')
#         # print(order)
#         for menu_cnt in order:
#             sub_order = menu_cnt.split(' ')
#             order_menu = sub_order[0]
#             order_cnt = sub_order[1]
#
#             if order_menu in order_data:
#                 order_data[order_menu] += int(order_cnt)
#             else:
#                 order_data[order_menu] = int(order_cnt)
#
# print(order_data)



#pickle 모듈 배우기
# 바이널리 파일 형식으로 변수에 저장된 객체를 저장해서, 객체타임을 그래도 유지하여 파일에 저장 및 읽어올 수 있다

def pickleFile():
    import pickle
    try:
        a_list = ['a','b','c','d']
        with open('C:\최효진\lecture\Week6.pickle','wb') as f:
            # 바이너리 파일 생성
            pickle.dump(a_list,f)
        with open('C:\최효진\lecture\Week6.pickle','rd') as f:
            data = pickle.load(f)
            print(type(data))
            print(len(data))

    except Exception as e:
        print(e)


def pickleFile():
    import pickle
    try:
        class book:
            def __init__(self,title, writer,price,publisher):
                self.title = title
                self.writer = writer
                self.price = price
                self.publisher = publisher

            book1 = book('a','b',7000,'d')
            book2 = book('e','f',8000,'h')

            with open('C:\최효진\lecture\Week6.pickle', 'wb') as f:
                # 바이너리 파일 생성
                pickle.dump(book1, f)
                pickle.dump(book2, f)
            with open('C:\최효진\lecture\Week6.pickle', 'rd') as f:
                data = pickle.load(f)
                print(type(data))
                print(data.title,data.writer,data.price,data.publisher)

    except Exception as e:
        print(e)

pickleFile()