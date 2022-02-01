import random

print("Ask your question")

question = input()
question = random.randint(0, 20)

if question == 1:
    print("It is certain.")

elif question == 2:
    print("As I see it, yes.")

elif question == 3:
    print("Reply hazy, try again.")

elif question == 4:
    print("Don`t count on it.")

elif question == 5:
    print("It is decidedly so.")

elif question == 6:
    print("Most likely.")

elif question == 7:
    print("Ask again later.")

elif question == 8:
    print("My reply is no.")

elif question == 9:
    print("Without a doubt.")

elif question == 10:
    print("Outlook good.")

elif question == 11:
    print("Better not tell you now")

elif question == 12:
    print("My sources say no.")

elif question == 13:
    print("Yes definitely.")

elif question == 14:
    print("Yes.")

elif question == 15:
    print("Cannot predict now.")

elif question == 16:
    print("Outlook not so good.")

elif question == 17:
    print("You may rely on it.")

elif question == 18:
    print("Signs point to yes.")

elif question == 19:
    print("Concentrate and ask again.")

else:
    print("Very doubtful.")