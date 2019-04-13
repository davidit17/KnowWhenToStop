import random
import os


def logo():
  print("""
                                      __                                 _ 
   __ _  __ _ _ __ ___   ___    ___  / _|   __ _  ___   ___   __ _  ___ | |
  / _` |/ _` | '_ ` _ \ / _ \  / _ \| |_   / _` |/ _ \ / _ \ / _` |/ _ \| |
 | (_| | (_| | | | | | |  __/ | (_) |  _| | (_| | (_) | (_) | (_| | (_) | |
  \__, |\__,_|_| |_| |_|\___|  \___/|_|    \__, |\___/ \___/ \__, |\___/|_|
  |___/                                    |___/             |___/                                
        """)


def instructions():
  print(""" There are n slips with different positive numbers.\n The numbers range from 1 to a number the size of a googol (1 followed by a hundred 0s).\n These slips are turned face down and shuffled over the top of a table.\n One at a time you turn the slips face up.\n The aim is to stop turning when you come to the number that you guess to be the largest of the series.\n You cannot go back and pick a previously turned slip.\n If you turn over all the slips,then of course you must pick the last one turned
    """)


def startend():
  print("""press 1 to get new number or 0 to choose the current number""")                              


def youlose():
  print("""
                 .              
  . . ,-. . .    |  ,-. ,-. ,-. 
  | | | | | |    |  | | `-. |-' 
  `-| `-' `-^    `' `-' `-' `-' 
  /|                           
  `-'                        
    """)


def youwon():
  print("""
  . . ,-. . .    . , , ,-. ,-. 
  | | | | | |    |/|/  | | | | 
  `-| `-' `-^    ' '   `-' ' ' 
  /|                          
  `-'                   
  """)


def end():
  os.system('clear')
  logo()
  print("n : {}".format(n))
  print ("optimal stopping euler : {}".format(int(-(-n // 2.71))))
  print ("=====")
  print ("----")
  print ('\n'.join([ str(slip) for slip in Slips[0:n] ]))
  print("\n")
  print(f"your number is : {Slips[i-1]}")
  print(f"maximal number is : {max(Slips)}")
  if (Slips[i-1]==max(Slips)):
  #if (all (Slips[i-1] >= x for x in Slips)):
    youwon()
  else : 
    youlose()


logo()
n = int(input("choose number n: "))
Slips = [random.randrange(1, n*10) for _ in range(n)]


for i in range(1,n+1):
  os.system('clear')
  logo()
  instructions()
  print("n : {}".format(n))
  print ("optimal stopping euler : {}".format(int(-(-n // 2.71))))
  print ("=====")
  print ('\n'.join([ str(slip) for slip in Slips[0:i] ]))
  print(f"\033[F\033[{len(str(Slips[i-1]))+2}G <-your number")
  print ("=====")
  startend()
  act = int(input("====\n"))
  if act == 0:
    end()
    break


end()
