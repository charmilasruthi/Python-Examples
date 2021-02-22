import random
def gameWin(comp,you):
   '''If two values are equa, declare TIE!'''
   if (comp == you):
      return None
   ''' Check all posibilities when computer chose 's' '''
   elif (comp == 's'):
      if (you == 'w'):
         return False
      elif (you =='g'):
         return True
      
    ''' Check all posibilities when computer chose 'w' '''  
   elif (comp == 'w'):
      if (you == 'g'):
         return False
      elif (you =='s'):
         return True

   ''' Check all posibilities when computer chose 'g' '''
   elif (comp == 'g'):
      if (you == 's'):
         return False
      elif (you =='w'):
         return True
c =0
u =0
for i in range (1,4):
   print("Comp choose: Snack(s), Gun(g), Water(w)")
   randNo = random.randint(1,3)
   if randNo == 1:
      comp = "s"
   if randNo == 2:
      comp = "g"
   if randNo == 3:
      comp = "w"
      
   you = input("You choose: Snack(s), Gun(g), Water(w)")

   a = gameWin(comp, you)
   print(f"Computer choose : {comp}")
   print(f"You choose: {you}")
   if a == None:
      print("Round is tie!")
   elif a:
      print("You won the round!")
      u = u+1
   else:
      print("computer won the round!")
      c = c+1
   print("you got "+ str(u) +" points")
   print("computer got "+ str(c) +" points")
   print()
   print()
if c>u:
   print("Computer won!")
elif c <u :
   print("You won!")
else:
   print("TIE!")
