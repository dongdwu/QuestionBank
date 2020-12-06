# 写一个函数，定义一个位置参数n以及可变参数numbers，返回实参列表中的第n大的数
def maximun(*numbers):
    digits = list(numbers)
    length_digits = len(digits)
    for index in range(length_digits - 1):
        for index_ in range(length_digits - 1 - index):
            if digits[index_] > digits[index_ + 1]:
                digits[index_], digits[index_ + 1] = digits[index_ + 1], digits[index_]
    return digits


if __name__ == '__main__':
    print(maximun(3, 6, 1, 5, 2))1 
