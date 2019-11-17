specialChar = ["!", "@", "#", "$", "%", "&"]

inputString = input("Enter word: ")

for i in range(0, len(specialChar)):
    inputString = inputString.replace(specialChar[i], "")

print(inputString)
