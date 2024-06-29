date = input("Enter the date (YYYY-MM-DD) : ")
rate_mood = int(input("How would you rate your mood today from 1 to 10 : "))
write_in = input("Enter your thoughts this day : ") + "\n"
with open(f"../textfile_b_example/{date}.txt", "w") as f:
    f.write(write_in)
