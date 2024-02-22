date = input("Enter today's date: ")
mood = input('how do you rate your mood today from 1 to 10? ')
thoughts = input("Let your thoughts flow: \n")

with open(F"C:/Users/tdwiv/Desktop/Python_exercises/Daily-Journal App/journal/{date}.txt","w") as file:
    file.write(f"Mood rating today: {mood}" + 2*'\n')
    file.write(thoughts)
    