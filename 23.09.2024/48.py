def a(w1, w2):
    set1 = set(w1)
    set2 = set(w2)
    unique_chars = (set1 - set2) | (set2 - set1)
    return len(unique_chars)
w1 = "привет"
w2 = "ветер"
result = a(w1, w2)
print("Количество уникальных символов:", result)