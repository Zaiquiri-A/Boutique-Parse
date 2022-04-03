
#function to find the indeces of all instances of a substring in a string
def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)


#opens text file into python script
with open ('3-26 Boutique Sales.txt', 'r') as f:
    
    #stores the files lines into a variable
    lines = f.readlines()
    
    #closes the text file
    f.close()
    
#print(lines)
#print(lines[0])

#sets the dollar total to 0
total = 0

#initializes empty lists for item name and count, then combines them into a 2d list
iName = []
iCount = []
items = [iName,iCount]

#iterates through each line to collect the dollar amounts
for x in lines:
    #print(x)
    #print(x[0])
    
    #if the line doesn't star with a $, we skip that line
    if x[0] != '$':
        continue
    
    #Sets the starting character location of the dollar amount (assumed to be 1 since $ is the first character of applicable lines)
    start = 1
    
    #print(len(x))
    
    #Checks for a space after the first dollar amount character, takes care of single digit amounts (<10)
    if x[start+1] == ' ':
    
        #print( int(x[start]))
        
        #converts to integer and adds dollar amount into the total
        total = total + int(x[start])
        
    #Takes care of 2 digit amounts (10 through 99)
    else:
        #print(x[start])
        
        #sets number to the first character of the dollar amount
        number = x[start]
        #print(number)
        
        #appends the second character of the dollar amount to the first
        number += x[start+1]
        #print(number)
        
        #Converts number to an integer and add it into the total
        total = total + int(number)
    
    #find all instances of (
    parenthOpen = list(find_all(x, '('))
    #print(parenthOpen)
    
    #find all instaces of )
    parenthClose = list(find_all(x, ')'))
    #print(parenthClose)
    
    #Sets the list index to 0 for iterating through the list of located parenthesis
    listIndex = 0
    #print('len(parenthOpen) = ' + str(len(parenthOpen)))

    #Iterates through the list of found parenthesis
    while listIndex < len(parenthOpen):
        
        #print('listIndex = ' + str(listIndex))
        #print(x[parenthOpen[listIndex] + 1].isdigit())
        
        #Determines whether the character iside the parenthesis is a digit or a letter
        if x[parenthOpen[listIndex]+1].isdigit():
            #print('digit')

            #finds number of characters in digit (assumed to be less than 3)
            #single digit case
            if x[parenthOpen[listIndex]+2] == ')':
               
                #store the count for passing into function
                itemCount = int(x[parenthOpen[listIndex]+1])
                
                # prep string for passing item name into function.
                string = ''
                # 4 is number of characters from '(' where text starts (assuming one space after ')').
                n = 4
                # gather text by appending characters to string until you see comma delimeter
                while x[parenthOpen[listIndex]+n] != ',':
                    string.append(x[parenthOpen[listIndex]+n])
                    n += 1
                
                #pass string into a function to check if it has already been added to the list of items and add to the count.
            #double digit case
            else:
                #store the count for passing into function
                itemCount = int(x[parenthOpen[listIndex]+1:parenthOpen[listIndex]+3])
                
    
       # else:
            #print('alpha')
        
        listIndex += 1
        
    
    

#Displays total dollar amount
print('Total Sales: $' + str(total))

