# Wumpus

from node import Node
from linkedmatrix import LinkedMatrix
import random

# Initalize Variables
hasWeapon = False
isAlive = True
size = 10
X = Y = 0 # determines initial loc
points = 0

# Amount of special tiles present
area = (size ** 2)
pits = int(area * 0.05)
weapons = wumpus = gold = int((area * 0.15))



def construct( size ):
    cnt = cntX = cntY = 0
    global X, Y
    cave = LinkedMatrix(size + 2, size + 2, ".")
    cave.head.value = '#'
    tmpNode = cave.head
    

    # Construct walls
    while cntX <= size:
        tmpNode = tmpNode.east
        tmpNode.value = '#'
        cntX += 1
    while cntY <= size:
        tmpNode = tmpNode.south
        tmpNode.value = '#'
        cntY += 1
    while cntX > 0:
        tmpNode = tmpNode.west
        tmpNode.value = '#'
        cntX -= 1
    while cntY >= 0:
        tmpNode = tmpNode.north
        tmpNode.value = '#'
        cntY -= 1

    # Place entrance
    X = random.randrange(1, size)
    Y = random.randrange(1, size)
    cave[(X, Y)] = '^'
    
    # Place pits
    while cnt < pits:
        cntX = random.randrange(1, size)
        cntY = random.randrange(1, size)
        if cave[ (cntX, cntY) ] == '.':
            cave[(cntX, cntY)] = 'o'
            cnt += 1

    cnt = 0
    
    # Place weapons
    while cnt < weapons:
        cntX = random.randrange(1, size)
        cntY = random.randrange(1, size)
        if cave[ (cntX, cntY) ] == '.':
            cave[(cntX, cntY)] = 'W'
            cnt += 1

    cnt = 0
    # Place gold
    while cnt < gold:
        cntX = random.randrange(1, size)
        cntY = random.randrange(1, size)
        if cave[ (cntX, cntY) ] == '.':
            cave[(cntX, cntY)] = '$'
            cnt += 1

    cnt = 0

    # Place wumpus monsters
    while cnt < wumpus:
        cntX = random.randrange(1, size)
        cntY = random.randrange(1, size)
        if cave[ (cntX, cntY) ] == '.':
            cave[(cntX, cntY)] = 'm'
            cnt += 1

    return cave
    
def startNode():
    currentNode = cave.head
    cnt = 0

    while X > cnt:
        currentNode = currentNode.east
        cnt += 1
    cnt = 0

    while Y > cnt:
        currentNode = currentNode.south
        cnt += 1

    currentNode.explored = True
    currentNode.present = True

    return currentNode

def numPoints():
    if points == 0:
        print "You earned zero points. Maybe being an adventurer isn't your cup of tea... "
    elif points == 1:
        print " You earned 1 point!"
    else:
        print " You earned " + str(points) + ' points!'

def text():
    global currentNode, points, isAlive
    
    if currentNode.value == '^':
        print " You find yourself at the entrance of the cave. "
    
    elif currentNode.value == '.':
        print " An empty room. Dust fills the air. "
        if currentNode.explored == False:
            points += 1
            currentNode.explored = True

    elif currentNode.value == '$':
        print " The room is filled to the brim with gold! "
        if currentNode.explored == False:
            currentNode.explored = True

    elif currentNode.value == 'W':
        if hasWeapon == False:
            print " A steel sword mounts a pedestal in the center of the room. "

        else:
            print " The room is filled to the brim with gold! "
        if currentNode.explored == False:
            currentNode.explored = True
            
    elif currentNode.value == 'm':
        if hasWeapon == False:
            print " You've walked into a Wumpus layer. Weaponless, it eats you whole. "
            print " ***GAME OVER*** "
            numPoints()
            isAlive = False
            return
        else:
            print " You step into a Wumpus layer. It moves to attack, but you dispatch is easily with your sword. "
            if currentNode.explored == False:
                currentNode.explored = True
                points += 10
            currentNode.value = '.'

    elif currentNode.value == 'o':
        print " You feel the dirt at your feet give way. You tumble into a deep pit and the warm embrace of death. "
        print " ***GAME OVER*** "
        numPoints()
        isAlive = False
        return
    # Clue if near Wumpus or Pit
    if currentNode.west.value == 'o':
        print " You hear a howling wind. "
    elif currentNode.north.value == 'o':
        print " You hear a howling wind. "
    elif currentNode.east.value == 'o':
        print " You hear a howling wind. "
    elif currentNode.south.value == 'o':
        print " You hear a howling wind. "

    if currentNode.west.value == 'm':
        print " You smell a foul stench. "
    elif currentNode.north.value == 'm':
        print " You smell a foul stench. "
    elif currentNode.east.value == 'm':
        print " You smell a foul stench. "
    elif currentNode.south.value == 'm':
        print " You smell a foul stench. "

    if hasWeapon:
        weaptxt = "armed and dangerous."
    else:
        weaptxt = "weaponless, feeble, and weak."
    print ' [' + str(points) + " Points Earned] You are " + weaptxt

def main():
    global currentNode, points, hasWeapon, isAlive
    currentNode = startNode()
    while isAlive == True:
        print cave
        text()
        if isAlive == False:
            break
        command = raw_input(" Enter Move (? for help): ")
        print "\n"
        if command == '?':
            print " N -- move north 1 space \n S -- move south 1 space \n" + \
            " W -- move west 1 space \n E -- move east 1 space \n L -- loot either gold or weapon in room \n" + \
            " R -- run out of the cave entrance (ends game) \nX -- hard exit out of came. \n"
        elif command.upper() == 'N':
            if currentNode.north.value != '#':
                currentNode.present = False
                currentNode = currentNode.north
                currentNode.present = True                
            else:
                print "You cannot travel into the wall. \n"
        elif command.upper() == 'S':
            if currentNode.south.value != '#':
                currentNode.present = False
                currentNode = currentNode.south
                currentNode.present = True                
            else:
                print "You cannot travel into the wall. \n"
        elif command.upper() == 'W':
            if currentNode.west.value != '#':
                currentNode.present = False
                currentNode = currentNode.west
                currentNode.present = True                
            else:
                print "You cannot travel into the wall. \n"
        elif command.upper() == 'E':
            if currentNode.east.value != '#':
                currentNode.present = False
                currentNode = currentNode.east
                currentNode.present = True                
            else:
                print "You cannot travel into the wall. \n"
        elif command.upper() == 'L':
            if currentNode.value == 'W':
                if hasWeapon ==False:
                    print " You pick up the blade. It feels cool to the touch. \n"
                    currentNode.value = '.'
                    points += 5
                    hasWeapon = True
                else:
                    print " You loot the room's bountiful treasure into your coffers. \n"
                    points += 5
                    currentNode.value = '.'
            elif currentNode.value == '$':
                print " You loot the room's bountiful treasure into your coffers. \n"
                points += 5
                currentNode.value = '.'
            else:
                print "There is nothing here to loot! "
        elif command.upper() == 'R':
            if currentNode.value == '^':
                print " You exit the Wumpus cave and run to the nearest inn. Your stories captivate all present. "
                print " ***GAME OVER***"
                numPoints()
                break
            else:
                print "You can only leave through the cave entrance!\n "
                
        elif command.upper == 'X':
            break

        else:
            print "Invalid command. Please try again. \n "
                
        
            
    
    


if __name__ == "__main__":
    cave = construct(size)
    main()
    
    
