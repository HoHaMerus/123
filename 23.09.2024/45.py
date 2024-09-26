def remove_longest_pet_name(pet_names):
    pets = pet_names.split()
    pets_dict = {i + 1: pet for i, pet in enumerate(pets)}
    
    # Находим питомца с самым длинным именем
    longest_name = max(pets, key=len)
    longest_index = pets.index(longest_name) + 1  # Порядковый номер

    # Удаляем питомца с самым длинным именем
    del pets_dict[longest_index]
    
    return pets_dict

# Входные данные
input_names = "Пушок Гарфилд Муся Кеша Тим"
result_dict = remove_longest_pet_name(input_names)

# Вывод результата
print(result_dict)