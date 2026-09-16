import random

def gen():
  
  fetch = int(input("Iteration frequency: "))
  i = int(fetch) + 1 

      while 0 < fetch < i:
        print(random.randint(1, 100))
        fetch -= 1

gen()
