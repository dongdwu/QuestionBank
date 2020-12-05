# 定义可变参数，返回实参中的最大值、最小值

def extreme(*numbers):
    large, small = numbers[0], numbers[0]
    for number in numbers[1:]:
        if number > large:
            large = number
        elif number < small:
            small = number
    return large, small


if __name__ == '__main__':
    print(extreme(8, 1, 3, 5, 7))
