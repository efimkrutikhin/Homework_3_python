def max_collected_berries(berries, chosen_bush):
    n = len(berries)
    max_collected = 0

    # Проверяем, что выбранный номер куста находится в допустимых границах
    if chosen_bush < 0 or chosen_bush >= n:
        print("Недопустимый номер куста.")
        return

    # Вычисляем суммарное количество ягод, которое можно собрать с трех кустов
    collected = berries[chosen_bush] + berries[(chosen_bush + 1) % n] + berries[(chosen_bush + 2) % n]
    
    # Обновляем максимальное количество собранных ягод
    max_collected = max(max_collected, collected)

    return max_collected

# Пример использования
n = int(input("Введите количество кустов: "))
berries = []
for i in range(n):
    berry_count = int(input(f"Введите количество ягод на кусте {i + 1}: "))
    berries.append(berry_count)

chosen_bush = int(input(f"Введите номер куста (от 0 до {n-1}): "))
result = max_collected_berries(berries, chosen_bush)
if result is not None:
    print("Максимальное количество ягод, которое может собрать собирающий модуль:", result)
