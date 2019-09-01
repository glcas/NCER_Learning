while True:
    n, m = map(eval, input('enter two int:').split())
    large, small = max([n, m]), min([n, m])
    while large % small != 0:
        large, small = small, large % small  # 辗转相除，初始大数➗初始小数，之后总是上式小数÷余数，直至余数为零，末式除数为最大公约数
    print('最大公约数是%d，最小公倍数是%d。' % (small, n * m // small))  # 最小公倍数=初始两数之积÷最小公倍数
