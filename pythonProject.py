import time

strg = "This is my first Python Project!" 
word_count = len(strg.split())

def createbox():
    print("/////"*30)
    print()
    print('Type the phrase provided below as fast as possible & with accuracy') 
    print()

while True:  
    t0 = time.time()
    createbox()
    print(strg,'\n')
    inputText = input()
    t1 = time.time()
    lengthOfInput = len(inputText.split())
    accuracy = len(set(inputText.split()) & set(strg.split())) 
    accuracy = (accuracy/word_count)
    timeTaken = (t1 - t0)

    wordsperminute = (lengthOfInput/timeTaken)*60
    
    print('Total words \t :' ,lengthOfInput)
    print('Time used \t :',round(timeTaken,2),'seconds')
    print('Your accuracy rate is\t :',round(accuracy,3)*100,'%') 
    print('Speed is \t :' , round(wordsperminute,2),'words per minute') 
    while True:
        print("Do you want to retry? (Yes/No): ",end='')
        ch=input().lower()
        if ch == "yes":
            break  
        elif ch == "no":
            print('Thank you for testing my project :)') 
            time.sleep(1.5) 
            break  
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")  
            continue  

    if ch == "no":
        break
