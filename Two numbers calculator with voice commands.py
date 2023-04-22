import pyttsx3

engine = pyttsx3.init()
engine.say("Welcome to 2 digit calculator designed by Manmegh")
print("Welcome to 2 digit calculator designed by - Manmegh")
engine.runAndWait()

engine.say("Enter first Number : ")
engine.runAndWait()
a = int(input("First Number : "))
engine.say("Enter second Number : ")
engine.runAndWait()
b = int(input("Second Number : "))


print("Enter 1 for Addition")
engine.say("Enter 1 for Addition")
engine.runAndWait()
print("Enter 2 for Subtraction")
engine.say("Enter 2 for Subtraction")
engine.runAndWait()
print("Enter 3 for Multipication")
engine.say("Enter 3 for Multipication")
engine.runAndWait()
print("Enter 4 for Division")
engine.say("Enter 4 for Division")
engine.runAndWait()



engine.say("Enter Choice between 1 to 4 : ")
engine.runAndWait()
Cal = int(input("Choice between 1 to 4 : "))



if Cal == 1:
      add = a+b
      print("The addition of 2 number is :" , add)
      engine.say("The addition of 2 number is ")
      engine.say(add)
      engine.runAndWait()

elif Cal == 2:
      sub = a-b
      print("The subtraction of 2 number is :" , sub)
      engine.say("The subtraction of 2 number is ")
      engine.say(sub)
      engine.runAndWait()

elif Cal == 3:
      mul = a*b
      print("The multipication of 2 number is :" , mul)
      engine.say("The multipication of 2 number is ")
      engine.say(mul)
      engine.runAndWait()

elif Cal == 4:
      div = a/b
      print("The division of 2 number is :" , div)
      engine.say("The division of 2 number is ")
      engine.say(div)
      engine.runAndWait()

else:
      print("Please select correct option")
      engine.say("Please select correct option")
      engine.runAndWait()
      
      
