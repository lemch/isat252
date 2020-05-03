for lizzbuzz in range(51):
    if lizzbuzz % 3 == 0 and lizzbuzz % 5 == 0:
        print("lizzbuzz")
        continue
    elif lizzbuzz % 3 == 0:
        print("lizz")
        continue
    elif lizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(lizzbuzz)