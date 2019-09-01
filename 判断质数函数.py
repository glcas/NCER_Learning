def isPrime(integer):
    """ if param isn't integer, return -1 """
    try:
        integer = eval(integer)
        if not isinstance(integer, int):
            return - 1
        elif integer < 1:  # 质数定义：从1开始的自然数，仅能被1和自身除
            return False
        else:
            for i in range(2, integer):  # 当为1和2时，range生成空list，迭代被跳过
                if integer % i == 0:
                        return False
            else:
                return True
    except:
        return -1


def main():
    while True:
        print(isPrime(input('Please input:')))


if __name__ == "__main__":
    main()
