phonebook = {}
while True:
    print('1)Stats ' '2)Add ' '3)Delete ' '4)List ' '5)Show  ' '6)Close ')
    input_user = input('Choose a command:')

    if input_user == "Stats":
        print(format(len(phonebook)))

    elif input_user == "Add":
        key = input('Enter name:')
        if phonebook.get(key) is not None:
            print('This name already exists, please choose another name!!!')
        else:
            value = input('Enter number:')
            phonebook[key] = value


    elif input_user == "Delete":
        input_hello = input('Enter name:')
        if input_hello in phonebook:
            del phonebook[input_hello]
        else:
            print("Error")

    elif input_user == "List":
        print(phonebook.keys())

    elif input_user == "Show":
        input_hello = input('Enter name:')
        if input_hello in phonebook:
            print(phonebook.get(input_hello))

    elif input_user == "Close":
        print('End of program')
        break
