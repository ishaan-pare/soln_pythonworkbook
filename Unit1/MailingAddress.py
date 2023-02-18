# Exercise 1: Mailing Address
# (Solved—9 Lines)
# Create a program that displays your name and complete mailing address formatted in
# the manner that you would usually see it on the outside of an envelope. Your program
# does not need to read any input from the user.

name = "Ishaan Pare"
h_no = 20
street = "Bada Pariwar"
loc = "Gurukul Kangri University"
pin = 249404
area = "Kankhal"
city = "Haridwar"
state = "Uttrakhand"
country = "India"

print(f"{name}")
print(f"{h_no}, {street}, \n{loc}, \n{area},{city} \n{state}, {country}, ({pin})")