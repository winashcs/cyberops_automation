def pv(password):
    if len(password) < 8:
        print("Your password must contain minimum 8 characters")
    else:
        has_alpha = False
        has_lower = False
        has_upper = False
        has_digit = False
        has_special = False
        for i in password:
            if i.isalpha():
                has_alpha = True
                if i.islower():
                    has_lower = True
                elif i.isupper():
                    has_upper = True
            elif i.isdigit():
                has_digit = True
            elif i in "@_!#$%^&*()<>?/|}{~:][":
                has_special = True
        if not has_alpha:
            print("Your password should contain alphabets")
        elif not has_lower:
            print("Your password should have lowercase")
        elif not has_upper:
            print("Your password should have uppercase")
        elif not has_digit:
            print("Your password should contain digits")
        elif not has_special:
            print("Your password does not have special characters")
        else:
            print("Password successful")

password = input("Enter your password: ")
pv(password)
