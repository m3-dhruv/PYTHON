# format method
name = "Dhruv"
country = "India"
letter = "Hey my name is {1} and I am from {0}"
print(letter.format(country, name))


# F- string (better way to formate a string)
print(f"Hey my name is {name} and I am from {country}")

print(type(letter))
# to print string as it is  
print(f"Hey my name is {{name}} and I am from {{country}}")