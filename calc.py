print("=== Калькулятор от St1llariks ===")

# Словарь операций — чисто и профессионально
ops = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
    '**': lambda a, b: a ** b,
    '%': lambda a, b: a % b
}

while True:
    val1 = input("\nЧисло 1 (или 'q' для выхода): ")
    if val1.lower() == 'q': 
        print("Пока!")
        break
        
    op = input(f"Операция ({', '.keys() if hasattr(ops, 'keys') else ', '.join(ops.keys())}): ")
    if op.lower() == 'q': break
    
    val2 = input("Число 2: ")
    if val2.lower() == 'q': break

    try:
        n1, n2 = float(val1), float(val2)
        if op in ops:
            if op in ('/', '%') and n2 == 0:
                print("Ошибка: деление на ноль!")
            else:
                print(f"Результат: {n1} {op} {n2} = {ops[op](n1, n2)}")
        else:
            print("Ошибка: неверная операция!")
    except ValueError:
        print("Ошибка: нужно вводить числа!")