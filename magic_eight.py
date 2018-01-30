def user_question:
    response = input("What is your question?")
    while response != "quit":
        if response[-1] != '?':
            print("I'm sorry, I can only answer questions")
        response = input("What is your question?")
