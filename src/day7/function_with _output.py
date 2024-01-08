def my_function():
    return 3 * 2


myresult = my_function()
print(myresult)

def format_name(f_name,l_name):
    if f_name == "" or l_name == "":
        return "you didn't provide valid input"
    formatted_f_name = f_name.title()  # .title() is used for  make the first char of string in upercase
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

print(format_name(input("What is your first name?\n"),input("what is your last name?\n")))

