print("Welcome to my quiz game!")
playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
    
    
print("Ok! Let's play : D")
score = 0 

response = input("What is the largest planet in our solar system? ")
if response == "Jupiter":
    print("Correct!")
    score += 1 #sau putem sa scriem score = score + 1 
else: 
    print("Incorrect!")
 
    
response = input("What is the chemical symbol for water? ")
if response == "H2O":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")
 
    
response = input("How many sides does a triangle have? ")
if response == "Three":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")
 
    
response = input("Who painted the Mona Lisa? ")
if response == "Leonardo da Vinci":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")
 
     
response = input("What is the capital of Norway? ")
if response == "Oslo":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")
    
print("You got " + str(score) + " questions correct!")
print("You got " + str((score/5) * 100) + "%.")