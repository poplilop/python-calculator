def calc(expr):
    expr = expr.strip().replace(',','.')
    if not expr:
        raise ValueError('Пустое выражение')
    for op in ('+', '-', '*', '/'):
        idx = expr.find(op, 1)
        if idx == -1:
            continue
        left_str = expr[:idx].strip()
        right_str = expr[idx+1:].strip()
        a = float(left_str)
        b = float(right_str)
        if op == '+': return a+b
        if op == '-': return a-b
        if op == '*': return a*b
        if op == '/':
            if b == 0:
                raise ZeroDivisionError('Деление на ноль')
            else:
                return a/b

    raise ValueError(f'нет операции в {expr!r}')