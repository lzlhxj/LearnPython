# 1.声明一个list
my_list = [1, 2, 3, 4, 5]
# 打印list
print("1.my_list: ", str(my_list))

# 2.判断是否是list
if isinstance(my_list, list):
    print("2.It's a list")

# 3.浮点数
print("3.float(4E210): ", str(float(4E210)))  

# 4.十进制转换为十六进制、八进制、二进制
print("4.10 in hex, oct, bin: ")
print("\t", hex(10))
print("\t", oct(10))
print("\t", bin(10))

# 5.数字表达式操作符
print("5.数字表达式操作符: ")
def my_generator():
    for i in range(3):
        yield i
gen = my_generator()
print("\t生成器函数next(gen): ", str(next(gen)))
print("\t生成器函数next(gen): ", str(next(gen)))
print("\t生成器函数next(gen): ", str(next(gen)))
print("\t1 if 1 else 0: ", str(1 if 1 else 0))
print("\t3 ** 3: ", str(3 ** 3))
print("\t1 in my_list: ", str(1 in my_list))

add_one = lambda x: x + 1
print("\tadd_one(3): ", str(add_one(3)))
print("\t强制转换int(3.14): ", str(int(3.14)))
print("\t强制转换float(3): ", str(float(3)))

# 6. 数字的bit_length()函数表示二进制位数
a = 11
print("6.数字的bit_length()函数表示二进制位数: ")
print("\t10.bit_length(): ", str(a.bit_length()))


# 7. 数字相关模块及相关类
print("7.数学模块、小数模块、分数模块: ")
import math                     # 导入math模块
import decimal                  # 导入decimal模块
from decimal import Decimal     # 导入Decimal类

# 数学计算
math_result = math.sqrt(16)
print("\tmath.sqrt(16): ", str(math_result))

# 小数计算
temp_decimal = Decimal('3.14') + Decimal('2.0')
print("\tDecimal('3.14') + Decimal('2.0'): ", str(temp_decimal))
decimal.getcontext().prec = 4   # 设置decimal模块的精度
temp_decimal2 = Decimal('10.175')
print("\tdecimal.getcontext().prec保留4位有效数字: ", temp_decimal2 + 0)
print("\tround()函数保留小数点后两位: 10.545=", round(10.545,2), "100.175=", round(100.175,2), "10.175=", round(10.175,2))

# 分数计算
from fractions import Fraction
temp_fraction = Fraction(3, 4)
print("\tFraction(3, 4): ", str(temp_fraction))


# 8.集合
print("8.集合: ")
s1 = set([1,10,100])
print("\t数值集合: ", str(s1)) 
s1.add(1000)
s1.remove(1)
print("\t集合s1: ", str(s1))

s2 = set(["hello","world"])
print("\t字符串集合: ", str(s2))

s3 = set("hello")
print("\t字符集合: ", str(s3))

