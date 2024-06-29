user_input = input("Enter the height in feet inches format : ")


def convert(user_input_local):
    user_list = user_input_local.split(" ")
    feet = float(user_list[0])
    inches = float(user_list[1])
    meter = feet * 0.3048 + inches * 0.0254
    return meter


user_height = convert(user_input)
if user_height > 1:
    print("Eligible to use the slide !")
else:
    print("Sorry not eligible to use the slide :(")
