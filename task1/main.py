def find_intersection_elements(n, m):
    # Запрашиваем элементы первого множества и сохраняем их в списке list_1
    print("Введите элементы первого множества:")
    list_1 = list(map(int, input().split()))

    # Запрашиваем элементы второго множества и сохраняем их в списке list_2
    print("Введите элементы второго множества:")
    list_2 = list(map(int, input().split()))

    # Создаем список для хранения пересечения элементов
    intersection_elements = []

    # Находим пересечение двух списков
    for num in list_1:
        if num in list_2 and num not in intersection_elements:
            intersection_elements.append(num)

    # Сортируем результат по возрастанию
    intersection_elements.sort()

    return intersection_elements

# Запрашиваем у пользователя кол-во элементов в первом и втором множествах
n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))

# Находим и выводим пересечение элементов двух множеств
result = find_intersection_elements(n, m)
print("Числа, которые встречаются в обоих множествах и отсортированы по возрастанию:", result)