'''Sets'''

S1 = set({1, 10, 67, 78, 89})
print(S1)

len(S1)
print(S1.remove(1))
print(S1.clear())
print(S1.union({1,89}))

S2 = set({678,90,89,78})
# print(S2.pop())
print(S1.intersection({1, 10}))
