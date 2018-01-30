import random
answers = ["It is certain","It is decidedly so", "Without a doubt", "Yes definitely", "You may reply on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes","Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]

def user_question():
    response = input("What is your question?")
    while response != "quit":
        if response[-1] != '?':
            print("I'm sorry, I can only answer questions")
        else:
            print(random.choice(answers))
        response = input("What is your question?")




user_question()
