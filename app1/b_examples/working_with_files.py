contents = ["Rohit Sharma", "Virat Kohli", "Mahendra Singh Dhoni"]
file_paths = ["../textfile_b_example/rs.txt", "../textfile_b_example/vk.txt", "../textfile_b_example/msd.txt"]
for i in range(len(contents)):
    file = open(file_paths[i], 'w')
    file.write(contents[i])
    file.close()
print("All work completed !")