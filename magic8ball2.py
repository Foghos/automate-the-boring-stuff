import random


messages = ["It is certain",
            "It is decidedly so",
            "Yes, definitely",
            "Reply hazy try again",
            "Ask again Later",
            "Concentrate and ask again",
            "My reply is no",
            "Outlook not so good",
            "Very doubtful"
            ]
while True:
    print("Ask me a question. ")
    input()
    print(messages[random.randint(0, len(messages) - 1)])

