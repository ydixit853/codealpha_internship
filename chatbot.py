# Name    : Yash Dixit
# Task    : Task 4 - Basic Chatbot
# Topic   : Rule-Based Chatbot using Python
# Concepts: if elif, functions, loops, input output

# my chatbot project
# i made this chatbot that replies to basic messages

def get_response(msg):
    msg = msg.lower().strip()

    # greetings
    if msg in ["hello", "hi", "hey", "howdy"]:
        return "Hi! How can I help you?"

    elif msg in ["how are you", "how are you?", "how r you", "you good?"]:
        return "I'm fine thanks! What about you?"

    elif msg in ["i'm fine", "i am fine", "i'm good", "good", "fine", "great", "i'm okay", "okay"]:
        return "That's good to hear!"

    elif msg in ["what's your name", "what is your name", "who are you", "your name"]:
        return "I'm a simple chatbot made in Python!"

    elif msg in ["who made you", "who created you", "who built you"]:
        return "I was made by Yash Dixit using Python :)"

    elif msg in ["how old are you", "what's your age", "your age"]:
        return "I don't have an age, I'm just a program lol"

    # help
    elif msg in ["help", "what can you do", "what do you do", "commands"]:
        return ("Here's what you can type:\n"
                "  hello, how are you, what's your name\n"
                "  joke, fun fact, motivate me\n"
                "  good morning, good night\n"
                "  i'm sad, i'm happy, i'm bored\n"
                "  time, date, weather\n"
                "  bye")

    # jokes and fun
    elif msg in ["joke", "tell me a joke", "say something funny", "make me laugh"]:
        return "Why don't scientists trust atoms? Because they make up everything!"

    elif msg in ["fun fact", "tell me a fun fact", "give me a fact", "fact"]:
        return "Fun fact: Honey never expires. They found 3000 year old honey in Egypt and it was still fine!"

    elif msg in ["tell me a story", "story", "tell a story"]:
        return "Once there was a little Python program. It learned to talk and made everyone happy. The end!"

    elif msg in ["sing a song", "sing for me", "sing something"]:
        return "La la la... I don't really know songs but here you go :)"

    # feelings
    elif msg in ["i'm sad", "i am sad", "i feel sad", "i'm upset", "i'm not okay", "i feel bad"]:
        return "Aww don't be sad :( things will get better, I promise!"

    elif msg in ["i'm happy", "i am happy", "i feel great", "i'm excited", "i feel happy"]:
        return "Yay! That makes me happy too :D"

    elif msg in ["i'm bored", "i am bored", "bored", "nothing to do", "so bored"]:
        return "Ask me a joke or a fun fact, maybe that helps!"

    elif msg in ["i'm angry", "i am angry", "i'm mad", "i feel angry"]:
        return "Take a deep breath, it will be okay!"

    elif msg in ["i'm tired", "i am tired", "i feel tired", "so tired"]:
        return "Get some rest! Sleep is important :)"

    elif msg in ["i'm scared", "i am scared", "i feel scared", "i'm nervous"]:
        return "It's okay to feel that way. You got this!"

    # motivation
    elif msg in ["motivate me", "inspire me", "i need motivation", "give me a quote", "quote"]:
        return "Keep going! Every expert was once a beginner."

    # greetings by time
    elif msg in ["good morning", "morning", "good morning!"]:
        return "Good morning! Hope you have a great day :)"

    elif msg in ["good night", "night", "good night!", "goodnight"]:
        return "Good night! Sleep well :)"

    elif msg in ["good afternoon", "afternoon"]:
        return "Good afternoon! Hope your day is going well."

    elif msg in ["good evening", "evening"]:
        return "Good evening! How was your day?"

    # bot questions
    elif msg in ["are you a robot", "are you a bot", "are you human", "are you real"]:
        return "Yes I'm a bot! But I try to be helpful :)"

    elif msg in ["can you think", "do you think", "are you intelligent", "are you smart"]:
        return "I just match your input to my answers, so not really lol"

    elif msg in ["do you sleep", "do you rest", "are you tired"]:
        return "Nope, I don't sleep. I'm always here!"

    elif msg in ["what's your hobby", "your hobby", "what do you like to do", "do you have hobbies"]:
        return "My hobby is answering your questions haha"

    # favorites
    elif msg in ["what's your favorite color", "favorite color", "your favourite color"]:
        return "I like blue! Like the Python logo."

    elif msg in ["what's your favorite food", "favorite food", "do you eat", "your favourite food"]:
        return "I wish I could eat! Maybe pizza if I could."

    elif msg in ["what's your favorite movie", "favorite movie", "your favourite movie"]:
        return "Maybe The Matrix, it's about code and stuff!"

    elif msg in ["what's your favorite song", "favorite music", "do you like music", "your favourite song"]:
        return "I like all kinds of music! What about you?"

    # time and date
    elif msg in ["what time is it", "what's the time", "time", "current time"]:
        from datetime import datetime
        now = datetime.now().strftime("%I:%M %p")
        return "Current time is " + now

    elif msg in ["what's today's date", "date", "today's date", "what's the date"]:
        from datetime import datetime
        today = datetime.now().strftime("%B %d, %Y")
        return "Today is " + today

    # weather
    elif msg in ["how's the weather", "what's the weather", "weather today", "weather"]:
        return "I can't check weather right now but hope it's nice outside!"

    # thanks
    elif msg in ["thanks", "thank you", "thank you!", "thanks!", "thx"]:
        return "No problem! :)"

    # compliments
    elif msg in ["you're awesome", "you are great", "good bot", "nice bot", "you're smart", "you're cool"]:
        return "Thanks haha, you're cool too!"

    # apology
    elif msg in ["sorry", "i'm sorry", "my bad", "i apologize"]:
        return "It's okay don't worry about it!"

    # help me
    elif msg in ["can you help me", "i need help", "please help", "help me"]:
        return "Sure! Type 'help' to see what I can do."

    # bye
    elif msg in ["bye", "goodbye", "see you", "exit", "quit", "see ya", "cya"]:
        return "Bye! See you later :)"

    # no match
    else:
        return "Hmm I didn't get that. Type 'help' to see what I can do."


def main():
    print("-----------------------------")
    print("     My Python Chatbot")
    print("     by Yash Dixit")
    print("  type 'bye' to exit")
    print("-----------------------------")

    while True:
        user_input = input("\nYou: ").strip()

        if not user_input:
            print("Bot: Say something!")
            continue

        reply = get_response(user_input)
        print("Bot:", reply)

        if user_input.lower().strip() in ["bye", "goodbye", "see you", "exit", "quit", "see ya", "cya"]:
            break


main()