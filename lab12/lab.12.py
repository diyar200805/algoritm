# Лабораторная работа №12
# Все задания в одном коде

# ---------------- ЗАДАНИЕ 1 ----------------
print("Задание 1:")
students = {
    "Ali": 5,
    "Diyar": 4,
    "Aruzhan": 5,
    "Nursultan": 3
}

for name, grade in students.items():
    print(name, "-", grade)

# ---------------- ЗАДАНИЕ 2 ----------------
print("\nЗадание 2:")
numbers = [5, 2, 5, 3, 2, 5]
freq = {}

for num in numbers:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

for k, v in freq.items():
    print(k, "->", v)

# ---------------- ЗАДАНИЕ 3 ----------------
print("\nЗадание 3:")
text = "algorithm"
char_count = {}

for ch in text:
    if ch in char_count:
        char_count[ch] += 1
    else:
        char_count[ch] = 1

for k, v in char_count.items():
    print(k, "->", v)

# ---------------- ЗАДАНИЕ 4 ----------------
print("\nЗадание 4:")
phone_book = {
    "Ali": "87001112233",
    "Diyar": "87002223344",
    "Aruzhan": "87003334455",
    "Nursultan": "87004445566",
    "Dana": "87005556677"
}

name = "Diyar"
print("Номер:", phone_book.get(name, "Не найден"))

# ---------------- ЗАДАНИЕ 5 ----------------
print("\nЗадание 5:")
words = ["cat", "dog", "cat", "bird", "dog", "dog"]
count = {}

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

for word, c in count.items():
    if c > 1:
        print(word)

# ---------------- ЗАДАНИЕ 6 ----------------
print("\nЗадание 6:")
s1 = "listen"
s2 = "silent"

print("Анаграммы" if sorted(s1) == sorted(s2) else "Не анаграммы")

# ---------------- ЗАДАНИЕ 7 ----------------
print("\nЗадание 7:")
products = {
    "apple": 500,
    "banana": 300,
    "milk": 700
}

# добавление
products["bread"] = 400

# изменение
products["apple"] = 550

# удаление
del products["banana"]

# поиск
print("Цена apple:", products.get("apple"))

# ---------------- ЗАДАНИЕ 8 ----------------
print("\nЗадание 8:")
nums = [4, 7, 1, 9, 7, 3, 1]
seen = set()

for n in nums:
    if n in seen:
        print("Первое повторяющееся:", n)
        break
    seen.add(n)

# ---------------- ЗАДАНИЕ 9 ----------------
print("\nЗадание 9:")
text = "python is great and python is easy"
words = text.lower().split()
count = {}

for w in words:
    if w in count:
        count[w] += 1
    else:
        count[w] = 1

max_word = max(count, key=count.get)
print("Чаще всего встречается:", max_word)

# ---------------- ЗАДАНИЕ 10 ----------------
print("\nЗадание 10:")

size = 5
hash_table = [[] for _ in range(size)]

def insert(key):
    index = key % size
    hash_table[index].append(key)

data = [10, 15, 20, 7, 12]

for num in data:
    insert(num)

print("Хеш-таблица:")
for i, bucket in enumerate(hash_table):
    print(i, "->", bucket)