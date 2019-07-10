def f ():
    """
    文字列を変換して返す
    例外を処理する
    """
    try:
        a=float(input())
        return a
    except:
        print("やり直し")

f()
