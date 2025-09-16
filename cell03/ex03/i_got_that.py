while True:
    user_input = input("What you gotta say? : ")
    print("I got that! Anything else? : ", end="")

    # Check if user entered STOP (case-sensitive)
    if user_input == "STOP":
        break
