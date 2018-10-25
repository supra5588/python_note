# file=open('/Users/ethanlin/PycharmProjects/Hello/write_and_read')
#
# text = file.read()
#
# print(text)
#
# file.close()


# with open('/Users/ethanlin/PycharmProjects/Hello/write_and_read') as f:
#     print(f.read())

# with open('/Users/ethanlin/PycharmProjects/Hello/write_and_read', 'w') as f:
#     f.write("hello world 會覆蓋前一段文字\n")


with open('/Users/ethanlin/PycharmProjects/Hello/write_and_read', 'a') as f:
    f.write("QQ")

# print(help(open))  # 可以開啟 open 的使用文件
