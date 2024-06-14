import base64

image = 'moyu.png'

# # 将图片encode为二进制字符串方法一
# with open(image, 'rb') as f:
#     str = base64.b64encode(f.read())
# print(type(str))

# 将图片encode为二进制字符串方法二
f = open(image, 'rb')
f_str = base64.b64encode(f.read())
f.close()
f1 = open('2.txt', 'wb')
f1.write(f_str)
f1.close()

# 将二进制字符串（图片）decode为图片
# str = f_str
f2 = open("2.txt", 'rb')
str = f2.read()
file_str = open('2.png', 'wb')
file_str.write(base64.b64decode(str))
file_str.close()
