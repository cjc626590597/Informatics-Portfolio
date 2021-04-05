import re

str = "￥6999"
str = int(str.split('￥')[1])
if 0<=str<2000:
    str = "0~2000 ￥"
elif 2000<=str<4000:
    str = "2000~4000 ￥"
elif 4000<=str<6000:
    str = "4000~6000 ￥"
elif 6000<=str<8000:
    str = "6000~8000 ￥"
elif 8000<=str<10000:
    str = "8000~10000 ￥"
elif 10000 <= str:
    str = "more than 10000 ￥"
print(str)
# pattern = re.compile(r'￥.*￥（.*）参数$')
# rawValue = re.sub(pattern, '', str)
# print(rawValue)