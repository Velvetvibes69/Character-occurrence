#Take input of a word 
string= input("Enter a word: ")
#Take input of a charecter
char= input("Enter your own chatecter ")
i=0
count=0
#Loop will to find the occerence of charecter
while(i < len(string)): #string operation

    if (string[i] == char): #condition 1
        count= count+1
    i= i+1
#Display the result
print("The total number of times ",char, "has occured:",count)