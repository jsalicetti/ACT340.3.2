myString = 'You learn more from failure than from success.'

newString = myString[0] + myString[4] + myString[-1]

newNewString = newString.replace(".", "!")

new_str= "“WHEN YOU Change your thougHts, remember to ALSO change your world.”"

lowerStr = new_str.lower()

upperStr = new_str.upper()



print(upperStr)
print(lowerStr)

print(newNewString)

new_str= "There are no traffic jams along the extra mile."

print(new_str.startswith("Z"))
print(new_str.startswith("t"))
print(new_str.index("j"))


a = new_str.count("t")
b = new_str.count("o")
print("The letter 't' appears {} times and the letter 'o' appears {} times.".format(a,b))

print(f"The letter 't' appears {a} times and the letter 'o' appears {b} times.")

greeting= "Good Morning!"
print(int(len(greeting)))

alphabet= "abcdefghijklmnopqrstuvwxyz"

print(alphabet.isalpha())

learning = "Learning is fun!"
print(learning.find("y"))
# print(learning.index("y"))

count_string= "Twinkle twinkle little star, how I wonder what you are"

all_freq = {}

for i in count_string:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

print("Count for all characters in count_strings is: " + str(all_freq))