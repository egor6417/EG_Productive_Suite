print ("Please input the # of books you've read this year") 
BooksAlready=int(input())
print ("Please input the # of weeks that have already passed this year") 
WeeksAlready=int(input())
x=(78/52)
c=x*WeeksAlready-BooksAlready
if (BooksAlready/WeeksAlready)>x:
  print ("You're on point, go have some fun!")
else:
  print ("Go read, you piece of uneducated crap")
  print ("You have")
  print (c)
  print ("books left to read this week to get on point")
