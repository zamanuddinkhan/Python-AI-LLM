a, b, c = 40, 0, 0
i, j = 0, 0

while i < 10:
    try:
        try:
            for j in range(0, 10):
                if i == j:
                    c = a / b
                    print(c)
                print(i)
        except ZeroDivisionError:
            i = i + 1
        finally:
            i = i + 1
    except Exception:
        i = i + 1
    finally:
        i = i + 1
    i = i + 1