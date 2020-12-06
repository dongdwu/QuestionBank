# 比较3个字符串的最大值、最小值
# 先两两比较出最大值、最小值，再用得出的最大值、最小值和第三个字符串比较

def calulate_extreme(x, y, z):
    """
    :param x: one number variable
    :param y: one number variable
    :param z: one number variable
    :return:  maximun，minimun
    """
    max_ = x if x > y else y
    min_ = x if x < y else y
    max_ = z if z > max_ else max_
    min_ = z if z < min_ else min_
    return max_, min_


if __name__ == '__main__':
    print(calulate_extreme(89, 23, 45))