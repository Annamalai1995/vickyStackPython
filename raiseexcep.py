try:
    pas = input("Set the password")
    con = input("Confirm password")
    if pas != con:
        raise AnnamalaiError
        
    else:
        print("Password was set successfully")
except AnnamalaiError as an:
    print(an)
finally:
    print("successfully login")
