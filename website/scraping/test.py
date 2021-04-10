import re

# str = "￥6999"
# str = int(str.split('￥')[1])
# if 0<=str<2000:
#     str = "0~2000 ￥"
# elif 2000<=str<4000:
#     str = "2000~4000 ￥"
# elif 4000<=str<6000:
#     str = "4000~6000 ￥"
# elif 6000<=str<8000:
#     str = "6000~8000 ￥"
# elif 8000<=str<10000:
#     str = "8000~10000 ￥"
# elif 10000 <= str:
#     str = "more than 10000 ￥"
# print(str)
# pattern = re.compile(r'￥.*￥（.*）参数$')
# rawValue = re.sub(pattern, '', str)
# print(rawValue)

# 2×Cortex-A76 Based 2.86GHz+2×Cortex-A76 Based 2.36GHz+4×Cortex-A55 1.95GHz
strs = "2*Cortex-A76 Based 2.6GHz+2*Cortex-A76 Based 1.92GHz+4*Cortex-A55 1.8GHz"
strs = strs.replace('A55 ','').replace('A77 ','').replace('Based ','').replace('×','x').replace('Cortex-','').replace('Cortex ','')
if 'x' in strs:
    isX = True
else:
    isX = False
strs = strs.split("+")
cpus = []
nums = []
sumGhz = 0.0
sum = 0
averageCpu = 0.0
# try:
print(strs)
if len(strs) > 1:
    if not isX:
        for str in strs:
            pattern = re.compile(r'A.* ')
            str = re.sub(pattern, '', str)
            str = str.split("*")
            print(str)
            cpus.append(float(str[0].split("G")[0]))
            nums.append(int(str[1]))
        for i in range(len(cpus)):
            sumGhz = sumGhz + cpus[i] * nums[i]
            sum = sum + nums[i]
        averageCpu = round(sumGhz / sum,2)
    elif isX:
        for str in strs:
            pattern = re.compile(r'A.* ')
            str = re.sub(pattern, '', str)
            str = str.split("x")
            cpus.append(float(str[1].split("G")[0]))
            nums.append(int(str[0]))
        for i in range(len(cpus)):
            sumGhz = sumGhz + cpus[i] * nums[i]
            sum = sum + nums[i]
            print(sumGhz)
        averageCpu = round(sumGhz / sum,2)
else:
    averageCpu = float(strs[0].split("G")[0])
print(averageCpu)
# except:
#     print(strs)