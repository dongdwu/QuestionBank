def calc_extreme(x, y):
    """
    :param x:one numberic variable
    :param y:one numberic variable
    :return:maximum or minimum
    """
    return x if x > y else y, x if x < y else y


if __name__ == '__main__':
    print(calc_extreme(3, 6))


