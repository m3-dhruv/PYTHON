x = "Ironman"
y = " Iron man  "
z = "welcome to python !!!"


print(len(x))   # length of x
print(x.upper())   # uppercase 
print(x.lower())   # lowercase
print(y.strip())   # remove before and after white spaces
print(z.rstrip("!"))   # remove !
print(x.replace("Iron","Loha"))   # replace string
print(x.split(" "))   # split the string at the whitespace
print(z.capitalize())   # uppercase first character
print(x.center(50))   # add 50 spaces
print(x.count("n"))   # count 
print(z.endswith("!!!")) # end with ! then true
print(z.find("to"))  # find to at which index
print(z.index("to"))  # find to at which index
print(x.isalnum())   # A-Z a-z 0-9 = true
print(x.isalnum())   # A-Z a-z = true  (not include 0-9)
print(x.islower())   # lowercharacter then true else false
print(x.isprintable())  # printable values the true
print(x.istitle())    # true if all the first char are capital
print(x.swapcase())  # convert upper to lower and lower to upper
print(z.title())   # first character convert into uppercase