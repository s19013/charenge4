def f1 (x):
    """
    引数を2で割る
    """
    a=x//2
    print(a)
    return a


def f2 (y):
    """
    4をかける
    """
    s=y*4
    print(s)
    return s

f2(f1(4))
