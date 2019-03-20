# fives no sevens new
# riles

acceptable = "1234567890"
redo = ""

while redo.lower() != "n":
    start = ""
    end = ""
    while not start:
        start = input("ENTER STARTING VALUE: ")
        start = start.lower()
        for char in start:
            if char not in acceptable:
                start = start.replace(char, "")

    while not end:
        end = input("ENTER ENDING VALUE: ")
        end = end.lower()
        for char in end:
            if char not in acceptable:
                end = end.replace(char, "")

    init = start

    end = int(end)
    start = int(start)

    while start <= end:
        if start % 5 == 0:
            if start % 7 != 0:  # no sevens allowed
                print(start, end=" ")
        start += 1
    acc = ["y", "n"]

    redo = input("Redo? (y/n): ")

    while redo.lower() not in acc:
        print("No, enter something that actually makes sense.")
        redo = input("\nRedo? (y/n): ")

input("\n\nHit enter.")
