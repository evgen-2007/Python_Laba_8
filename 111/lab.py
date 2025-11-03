import os

# Визначимо імена файлів
file_name_1 = "TF12_1.txt"
file_name_2 = "TF12_2.txt"

# === а) Створення файлу TF12_1 ===
print(f"a) Створення файлу '{file_name_1}'...")
try:
    # Дані для запису (рядки різної довжини)
    data_for_file_1 = [
        "Це перший рядок файлу.\n",
        "А це другий рядок файлу.\n",
        "Це вже третій.\n",
        "Ще трішки. Це четвертий рядок, "
        "Вже п'ятий рядок.\n",
        "Кінець!"
    ]
    
    with open(file_name_1, 'w', encoding='utf-8') as f:
        f.writelines(data_for_file_1)
        
    print(f"Файл '{file_name_1}' успішно створено.")

except IOError as e:
    print(f"Помилка при створенні файлу {file_name_1}: {e}")
    # Якщо файл не створився, подальші кроки не мають сенсу
    exit()

# === б) Читання TF12_1 та запис у TF12_2 ===
print(f"\nб) Читання з '{file_name_1}' та запис у '{file_name_2}'...")
try:
    # Читаємо ВЕСЬ вміст файлу TF12_1 в одну велику змінну
    with open(file_name_1, 'r', encoding='utf-8') as f_in:
        content = f_in.read()

    # Записуємо у файл TF12_2 за потрібним шаблоном
    with open(file_name_2, 'w', encoding='utf-8') as f_out:
        current_index = 0  # Поточна позиція у 'content'
        line_length = 1    # Довжина рядка, яку потрібно записати (1, 2, ... 10)
        
        while current_index < len(content):
            # Вирізаємо шматок тексту
            # content[start:end]
            chunk = content[current_index : current_index + line_length]
            
            # Записуємо шматок у файл з додаванням нового рядка
            f_out.write(chunk + '\n')
            
            # Оновлюємо індекс
            current_index += line_length
            
            # Оновлюємо довжину для наступного рядка
            line_length += 1
            if line_length > 10:
                line_length = 1  # Скидаємо лічильник назад до 1
                
    print(f"Файл '{file_name_2}' успішно заповнено за шаблоном.")

except FileNotFoundError:
    print(f"Помилка: Вхідний файл '{file_name_1}' не знайдено.")
except IOError as e:
    print(f"Помилка при читанні/записі файлів: {e}")
    exit()

# === в) Читання вмісту TF12_2 та друк ===
print(f"\nв) Друк вмісту файлу '{file_name_2}':")
print("-" * (30 + len(file_name_2)))
try:
    with open(file_name_2, 'r', encoding='utf-8') as f:
        for line in f:
            # Використовуємо end='', щоб print не додавав свій символ 
            # нового рядка, оскільки line вже містить його
            print(line, end='')

    print(f"\n" + "-" * (30 + len(file_name_2)))
    print("Друк файлу завершено.")

except FileNotFoundError:
    print(f"Помилка: Файл '{file_name_2}' не знайдено.")
except IOError as e:
    print(f"Помилка при читанні файлу {file_name_2}: {e}")