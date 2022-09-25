print('''
                                                      _________
_____________________________________________________|  __  __ |____________
                                      ___----'// \   | '-. '-. |
                                ___---      //   \   | `-' `-' |
                          ___---          //____  \  |  Left   |
                    ___---              // /____\ \  |  Right  |
              ___---                  /// |==__==| \ |_________|
        ___---                      ///   ~||~~||~ \     | |
  ___---                          ////     '        \    | |
--                              ////     //         \    | |
O'Neil                        ////                   \   | |
''')
print("Welcome to Home Treasure .")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

roads = input(
    "Choose the path you want to reach the destination ( Left or Right) ?\n")
road = roads.lower()

if road == "left":
    print('''
        _______________________________________________   
     / __                   __                   __  \ 
     ||  |_________________|__|_________________|  | |     
     ||_/                                        \_| |
     |  |                                         |  |
     |  |                                         |  |
     |  |    /^\                                  |  |
     |  |   /   \                                 |  |
     |  |  /_____\                                |  |
     |  |                                         |  |
     |  |                                         |  |   
     |  |                                         |  |   
     | _| c=================================D     |_ |   
     || \ _______________________________________/ | |   
     ||__|                 |__|                 |__| |
     \_______________________________________________/
  ''')
    pools = input("In your eyes, you see pool you choose ( Swim or Jump ) ?\n")
    pool = pools.lower()
    if pool == "swim":
        print('''
       ______________
|\ ___________ /|
| |  _ _ _ _  | |
| | | | | | | | |
| | |-+-+-+-| | |
| | |-+-+=+%| | |
| | |_|_|_|_| | |
| |    ___    | |
| |   [___] ()| |

| |         ||| |
| |         ()| |
| |           | |
| |           | |
| |           | |
|_|___________|_|  
    ''')
        doors = input(
            "Now you stand in front the dor, u have 3 choose number the door (22,42, and 11) ?\n"
        )
        door = int(doors)
        if door == 42:
            print("You Win!.")
        elif door == 11:
            print("Burned by fire.Game Over!.")
        else:
            print("Game Over")
    else:
        print("Fall into a hole. Game Over.")
else:
    print("Fall into a hole. Game Over.")
