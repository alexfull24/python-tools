import random

def gen():
  
  fetch = input("LOOP COUNT: ")
  i = int(fetch) - 1 

      while 0 < i < fetch:
        return random.randint(1, 100)
        
