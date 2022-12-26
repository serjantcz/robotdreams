x = input("Write something:")
for a in x:
        if x.isdigit():
            if int(x) % 2 == 0:
                print("This is a number")
                print("Number is even")

            else:
                print("This is a number")
                print("Number is odd")

        elif x.isalpha():
            if x.islower():
                print("This is a letter")
                print("This is a lowercase letter")
            else:
                print("This is a letter")
                print("This is uppercase letter")
        else:
            print("This is a character")

a = input("Press (q):")
while a == "q":
    import time
    while True:
        time.sleep(4.2)
        print("I love Python")














