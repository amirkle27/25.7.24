#a#
print (" a ".center(50,"*"))
print(" fun-day ".strip())
#b#
print (" b ".center(50,"*"))
print("hello".isalpha())
#c#
print (" c ".center(50,"*"))
print("777".isdigit())
#d#
print (" d ".center(50,"*"))
print("  ".isspace())
#e#
print (" e ".center(50,"*"))
ninja: list = ['N','I','N','J','A']
print ("".join(ninja))
#f#
print (" f ".center(50,"*"))
print("*".join(ninja))
#g#
print (" g ".center(50,"*"))
print("e" in "hELLo".lower() )
#h#
print (" h ".center(50,"*"))
word: str = str (input("Enter a word: "))
letters = [char.upper() for char in word if char.isalpha()]
print(letters)




