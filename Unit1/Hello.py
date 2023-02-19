# Exercise 2: Hello
# (9 Lines)
# Write a program that asks the user to enter his or her name. The program should
# respond with a message that says hello to the user, using his or her name.



name = str(input("Enter Your Name :"))

pri = " ".join([x.capitalize() for x in name.split()])
print(f"Hello {pri}, Welcome!")