import random,sys, platform, os
door=(0,0)
dragon=(0,0)
gamer=(0,0)
gride=[]
gride_size=2
valid_moves=[]
gameover=False
find_door=False
def draw_gride(size,show_dragon=False):
    "draw game gride"
    print("",end="")
    for i in range(0,size):
        print(" ___",end="")
    print("")
    for i in range(0,size):
        for j in range(0,size):
            if gride[i][j]==gamer and not show_dragon:
                print("|_x_",end="")
            elif show_dragon and gride[i][j]==dragon:
                print("|_g_",end="")
            elif show_dragon and gride[i][j]==door:
                print("|_d_",end="")
            else:
                print("|___",end="")
        print("|")
        
 
def create_gride(size):
    x=[]
    
    for i in range(size):
        y=[]
        for j in range(size):
            y.append((i,j))
        x.append(y)
    return x

def find_valid_moves():
    global valid_moves
    valid_moves.clear()
    if gamer[0]-1>=0:
        valid_moves.append("up")
    if gamer[0]+1<gride_size:
        valid_moves.append("down")
    if gamer[1]-1>=0:
        valid_moves.append("left")
    if gamer[1]+1<gride_size:
        valid_moves.append("right")
def clear_screen():
    if platform.system() == 'Linux':
        os.system('clear')
    elif platform.system() == 'Windows':
            os.system('cls')
    else:
        print('Clear screen is not working.')
def move_gammer(command):
    global gamer
    global gameover
    global find_door
    
    if(command=="up"):
        gamer=(gamer[0]-1,gamer[1])
    if(command=="down"):
        gamer=(gamer[0]+1,gamer[1])
    if(command=="right"):
        gamer=(gamer[0],gamer[1]+1)
    if(command=="left"):
        gamer=(gamer[0],gamer[1]-1)

    if gamer==dragon:
        gameover=True
    if gamer==door:
        find_door=True
    
def main():
    
    global dragon
    global door
    global gamer
    global gride
    global gride_size

    while True:
        try:
            gride_size=int(input("enter grid size: "))
            break
        except ValueError:
            clear_screen()
            print("enter number only!!!")
    gride=create_gride(gride_size)
    while (dragon==door) or (gamer==door) or  (gamer==dragon):
        dragon=gride[random.randrange(len(gride))][random.randrange(len(gride))]
        door=gride[random.randrange(len(gride))][random.randrange(len(gride))]
        gamer=gride[random.randrange(len(gride))][random.randrange(len(gride))]
    
    

    clear_screen()
    find_valid_moves()
    draw_gride(gride_size)
    
    while not gameover and not find_door:
        try:
            command=input("pleas select direction from {}:".format(",".join(valid_moves)))
            print(command)
            if command not in valid_moves:
                raise ValueError
            move_gammer(command)
            clear_screen()
            find_valid_moves()
            draw_gride(gride_size)
            
        except:
            clear_screen()
            draw_gride(gride_size)
            print("select from {}".format(",".join(valid_moves)))
    
    clear_screen()
    draw_gride(gride_size,True)
    if gameover:
        print("your are gameover try later")
    elif find_door:
        print("find door")
    
        

if __name__ == "__main__":
    gride_size=12
    main()
    

    
    