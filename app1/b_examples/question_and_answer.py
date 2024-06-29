import json

with open("../textfile_b_example/q_a.json", "r") as file:
    data = file.read()

questions = json.loads(data)

score = 0
for question in questions:
    print(question["question-text"])
    for index, options in enumerate(question["alternatives"]):
        print(index + 1, " - ", options)
    user_input = int(input("Enter the correct option number : "))
    question["user-choice"] = user_input
    if user_input == question["correct-answer"]:
        score += 1

for index, item in enumerate(questions):
    if item["correct-answer"] == item["user-choice"]:
        result = "Correct Answer"
        score += 1
    else:
        result = "Wrong Answer"
    print(f"{index + 1} - {result} Your choice : {item['user-choice']} Correct Answer : {item['correct-answer']} ")

print("Your final Score : ", score)
