setx = {"green", "blue"}
sety = {"blue", "yellow"}
print("Original set elements: ")
print(setx)
print(sety)
print("\nIntersection of two said sets: ")
setz = setx.intersection(sety)
print(setz)

#Finding Union
setz = setx.union(sety)
print(setz)

#Finding difference
setz = setx.difference(sety)
print(setz)

#Finding symmetric difference
setz = setx.symmetric_difference(sety)
print(setz)