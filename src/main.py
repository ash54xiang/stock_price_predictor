import itertools

list1 = [1]
list2 = ["a", "b"]
list3 = [100, 300, 500]

combined_list = itertools.product(list1, list2, list3)
print(f"Product list : {list(combined_list)}")

print("Permutation", list(itertools.permutations(range(1, 4), 2)))
print("Combination", list(itertools.combinations(range(1, 4), 2)))
print("Combination", list(itertools.combinations_with_replacement(range(1, 4), 2)))


def square(x):
    for n in range(x):
        yield n ** 2


gen = square(10)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
