shopping_lists = []
shopping_lists.extend(["яблоко", "молоко", "хлеб", "яйца", "сок", ])
print(shopping_lists)
for shopping_list in shopping_lists:
    print(shopping_list)
shopping_lists.remove("молоко")
print(shopping_lists)
shopping_lists[0] = "банан"
print(shopping_lists)
len(shopping_lists)
print(len(shopping_lists))
