#inporting libraries
import textblob
from textblob import TextBlob as tb
import tweepy











#start
print("...Sentiment Analysis using Python...")
print(" ")

#types
print("Press 1 for analysis from already set text")
print("Press 2 for analysis from user input")



#choice
choice=input()

#1st case
if(choice=="1"):
    feedback1="Suncity is very good place"
    print("input is : ",feedback1)
    blob1=tb(feedback1)
    print("Sentiment Result is : ",blob1.sentiment)
    print(" ")


#2nd case
if(choice=="2"):
    print("Enter Feedback (Line or Paragraph) : ")
    feedback2=input()
    print("input is : ",feedback2)
    blob2=tb(feedback2)
    print("Sentiment Result is : ",blob2.sentiment)
    print(" ")
    

    

            
        
    

    
    

