import random


# 1 编写一个函数，求多个数中的最大值
def get_max(*args):
    x = args[0]
    for arg in args:
        if arg > x:
            x = arg
    return x


print(get_max(1, 2, 3, 4, 5, 6, 89, 2312, 41, 314))


# 2 编写一个函数，实现摇骰子的功能，打印N个骰子的点数和
def get_sum(n):
    m = 0
    for i in range(n):
        x = random.randint(1, 6)
        m += x
    return m


print(get_sum(4))


# 3 编写一个函数，提取指定字符串中所有的字母，然后拼接在一起产生一个新的字符串。
def get_alphas(word):
    new_str = ''
    for w in word:
        if w.isalpha():
            new_str += w
    return new_str


print(get_alphas('hello123good456'))


# 4 写一个函数，默认求10的阶乘，也可以求其他数字的阶乘
def get_factorial(n=10):
    x = 1
    for i in range(1, n + 1):
        x *= i
    return x


print(get_factorial())


# 5 写一个函数，求多个数的平均值
def get_average(*args):
    x = 0
    for arg in args:
        x += arg
    return x / len(args)


print(get_average(10, 1, 2, 2, 3, 4))


# 6 写一个自己的capitalize函数，能够将指定字符串的首字母变成大写字母。
def my_capitalize(word):
    c = word[0]
    if 'z' >= c >= 'a':
        new_str = word[1:]
        return c.upper() + new_str
    return word


print(my_capitalize('hello'))


# 7 写一个自己的endswith函数，判断一个字符串是否以指定的字符串结束
def my_endswith(old_str, str1):
    return old_str[-len(str1):] == str1


print(my_endswith('hello', 'lo'))


# 8 写一个自己的isdigit函数，判断一个字符串是否是纯数字字符串
def my_digit(old_str):
    for s in old_str:
        if not '0' <= s <= '9':
            return False
    return True


print(my_digit('123hd90'))


# 9 写一个自己的upper函数，将一个字符串中所有的小写字母变成大写字母。
def my_upper(word):
    new_str = ''
    # 'A' == '65'   a =='97'
    for s in word:
        if 'a' <= s <= 'z':
            upper_s = chr(ord(s) - 32)
            new_str += upper_s
        else:
            new_str += s
    return new_str


print(my_upper('hello123good'))


# 10 写一个函数实现自己in操作，判断指定序列中，指定的元素是否存在。
def my_in(it, ele):
    for i in it:
        if i == ele:
            return True
    else:
        return False


print(my_in(['zhangsan', 'lisi', 'wangwu'], 'lisi'))


# 11 写一个自己的replace函数，将指定字符串中指定的旧字符串转换成指定的新字符串
def my_replace(all_str, old_str, new_str):
    return new_str.join(all_str.split(old_str))


print(my_replace('how you and you fine you ok', 'you', 'me'))


# 12 写一个自己的max函数，获取指定序列中元素的最大值。如果序列是字典，取字典值的最大值
def get_max2(seq):
    if type(seq) == dict:
        seq = list(seq.values())
    x = seq[0]
    for i in seq:
        if i > x:
            x = i
    return x


print(get_max2({'a': 12, 'b': 13, 'c': 14}))
