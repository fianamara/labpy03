maxsimal = 0
while True:
    a = int(input("Masukan bilangan = "))
    if maxsimal < a:
        maxsimal = a
    if a == 0:
        break
print("Bilangan Terbesarnya Adalah = ", maxsimal)
