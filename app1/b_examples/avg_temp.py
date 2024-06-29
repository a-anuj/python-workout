def get_fileinfo():
    with open("../textfile_b_example/temperature.txt", "r") as f:
        value_list = f.readlines()[1:]
    new_list = [float(i) for i in value_list]
    return new_list


print("The average temperature is : ", sum(get_fileinfo()) / len(get_fileinfo()))
