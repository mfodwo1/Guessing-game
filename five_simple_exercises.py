#Personal Information:
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
state = input("Enter your state: ")

if age < 18:
    print("You are not an adult.")
elif age > 65:
    print("You are a senior citizen.")
else:
    print("You are an adult.")

personal_info = name + ", " + str(age) + ", " + city + ", " + state
print("Your personal information is: " + personal_info)


#Number Game:
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    print("The first number is greater.")
elif num2 > num1:
    print("The second number is greater.")
else:
    print("Both numbers are equal.")

result = num1 * num2
if result % 2 == 0:
    print("The result is even.")
else:
    print("The result is odd.")

#Letter Classifier:
letter = input("Enter a character: ")

if letter.isdigit():
    print("The character is a digit.")
elif letter.islower():
    print("The character is a lowercase letter.")
elif letter.isupper():
    print("The character is an uppercase letter.")
else:
    print("The character is a special character.")

#Palindrome Checker:
word = input("Enter a word: ").lower()

if word == word[::-1]:
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")

#Grade Calculator:
score = int(input("Enter your score: "))

if score >= 90 and score <= 100:
    print("You got an A.")
elif score >= 80 and score <= 89:
    print("You got a B.")
elif score >= 70 and score <= 79:
    print("You got a C.")
elif score >= 60 and score <= 69:
    print("You got a D.")
else:
    print("You got an F.")

new_score = score + 10
if new_score >= 0 and new_score <= 100:
    print("The new score is in the range.")
else:
    print("The new score is out of the range.")