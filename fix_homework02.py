text = input("Write word or number:")
    if text.isdigit():
      if int(text) % 2 == 0:
        print("This is a number")
        print("Number is even")
    # ===========================================#

      elif int(text) % 2 == 1:
            print("This is a number")
            print("Number is odd")
    # ===========================================#

    else:
        print("This is a word")
        print(len(text))
    # ===========================================#
