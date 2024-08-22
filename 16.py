quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["1. Berlin", "2. Madrid", "3. Paris", "4. Rome"],
        "correct_answer": 3
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "options": ["1. Charles Dickens", "2. William Shakespeare", "3. Mark Twain", "4. J.K. Rowling"],
        "correct_answer": 2
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["1. Earth", "2. Jupiter", "3. Mars", "4. Saturn"],
        "correct_answer": 2
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["1. Oxygen", "2. Gold", "3. Silver", "4. Hydrogen"],
        "correct_answer": 1
    },
]

def quiz():
    for i in quiz_data:
        print("\n",i["question"])
        for i in i["options"]:
            print(i)

            ans = input("Enter the answer:")
            if answer == item["correct_answer"]:
             print("Correct!")
             score += 1
            else:
             print("Wrong answer!")

quiz()
