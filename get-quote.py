import random
def primary():
   print("Keep it logically awesome.")

   print "Hello World!",
   print "My Name is Ed-Vish"

   f = open("quotes.txt")
   quotes = f.readlines()
   f.close()

   last = 13
   rnd = random.randint(0, last)
   print(quotes[rnd])
   
   myStr = ("To leave a message\n press the # key on your phone.")
   print(myStr)

if __name__== "__main__":
  primary()
