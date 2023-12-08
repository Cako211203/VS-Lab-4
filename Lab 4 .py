import random

# İlkin siyahını yaratmaq və fayla yazmaq
lst = [random.randint(0, 101) for _ in range(5)]
print("lst = ", lst)

with open('file.txt', 'w') as f:
    f.write(str(len(lst)) + '\n')
    f.write(' '.join(map(str, lst)))

# Fayldan oxumaq və 5-ə bölünməyən ədədləri tapmaq
with open('file.txt', 'r') as f:
    f.readline()  # Birinci sətiri oxuyub atmaq
    lst2 = list(map(int, f.readline().split()))

# 5-ə bölünməyən ədədlərin siyahısını və cəmini hesablamaq
not_divisible_by_5 = [x for x in lst2 if x % 5 != 0]
sum_not_divisible_by_5 = sum(not_divisible_by_5)

# Nəticələri yeni fayla yazmaq
with open('new_file.txt', 'w') as f:
    f.write(' '.join(map(str, not_divisible_by_5)) + '\n')
    f.write(str(sum_not_divisible_by_5))

print('5-ə bölünməyən ədədlər:', not_divisible_by_5)
print('Cəmi:', sum_not_divisible_by_5)
