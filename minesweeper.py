
import pyautogui, time, os, logging, sys, random, copy
import numpy as np
import m_board
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')
#logging.disable(logging.DEBUG) # uncomment to block debug log messages

b1 = m_board.Board()
squares = []
def main():
    logging.debug('Program Started. Press Ctrl-C to abort at any time.')
    logging.debug('To interrupt mouse movement, move mouse to upper left corner.')
    getGameRegion()

def imPath(filename):
    return os.path.join('images', filename)

def getGameRegion():


    # identify the top-left corner
    logging.debug('Finding game region...')

    region = pyautogui.locateOnScreen('Smile.png',grayscale=False, confidence=0.4)
    if region is None:
        raise Exception('Could not find game on screen. Is the game visible?')

    # calculate the region of the entire game
    topRightX = region[0] # left + width
    topRightY = region[1] # top
    scanXStart = topRightX - 80
    scanYStart = topRightY + 40
    scanXEnd = scanXStart + 170
    scanYEnd = scanYStart + 200
    
    global b1
    global squares

    Blanks = pyautogui.locateAllOnScreen('Blank.png',region=(scanXStart,scanYStart,scanXEnd,scanYEnd),grayscale=False,confidence=0.8)
    squares = list(Blanks)
    Brd = [0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0]
    nd_a = np.array(Brd)
    B = np.reshape(nd_a, (-1, 9))
    Sq32 = squares[32]
    pyautogui.click(x=Sq32.left+5, y=Sq32.top+5)
    #pyautogui.click(230,227)  
    count = 0
    Ones = pyautogui.locateAllOnScreen('One.png',region=(scanXStart,scanYStart,scanXEnd,scanYEnd),grayscale=False, confidence=0.9)
    Twos = pyautogui.locateAllOnScreen('Two.png',region=(scanXStart,scanYStart,scanXEnd,scanYEnd),grayscale=False, confidence=0.8)
    Threes = pyautogui.locateAllOnScreen('Three.png',region=(scanXStart,scanYStart,scanXEnd,scanYEnd),grayscale=False, confidence=0.9)
    Fours = pyautogui.locateAllOnScreen('Four.png',region=(scanXStart,scanYStart,scanXEnd,scanYEnd),grayscale=False, confidence=0.9)
    Blanks = pyautogui.locateAllOnScreen('Blank.png',region=(scanXStart,scanYStart,scanXEnd,scanYEnd),grayscale=False,confidence=0.8)
    total_bombs = 10
    total_flags = 0
    num_tries = 0
    while(not(total_bombs == total_flags)):
        print("*********\n*\n*\n********\n",total_flags,"-------- ",total_bombs)
        scan_board(Brd,Ones,Twos,Threes,Fours,Blanks,scanXStart,scanYStart,scanXEnd,scanYEnd)
        num_tries += 1
        
        something_flagged = True
        while (something_flagged):
            something_flagged = False
            for i in range(0, 9):
                for j in range(0, 9):
                    num_adj_bombs = b1.grid[i][j]
                    unknown_blocks = b1.count_uknown_blocks(i,j)
                    num_adj_flags = b1.count_flags(i,j)
                    print("TESTING: ", i,", ",j)
                    if(unknown_blocks == num_adj_bombs - num_adj_flags):
                        print("***************** TEST PASSED ******************")
                        b1.print()
                        neighbors = b1.get_neighbors(i,j)
                        print(neighbors)
                        for n in neighbors:
                            k , l = n
                            if b1.grid[k][l] == 9:
                                pyautogui.rightClick(x=squares[k * 9 + l].left+5, y=squares[k * 9 + j].top+5)
                                something_clicked = True
                                total_flags += 1
                                b1.grid[k][l] = -1

        for i in range(0, 9):
            for j in range(0, 9):
                num_adj_bombs = b1.grid[i][j]
                unknown_blocks = b1.count_uknown_blocks(i,j)
                num_adj_flags = b1.count_flags(i,j)      
                if(num_adj_flags == num_adj_bombs and not(num_adj_bombs == 0)):
                    neighbors = b1.get_neighbors(i,j)
                    for n in neighbors:
                        k , l = n
                        if b1.grid[k][l] == 9:
                                pyautogui.click(x=squares[k * 9 + l].left+5, y=squares[k * 9 + l].top+5)
        scan_board(Brd,Ones,Twos,Threes,Fours,Blanks,scanXStart,scanYStart,scanXEnd,scanYEnd)
        

       
def scan_board(Brd,Ones,Twos,Threes,Fours,Blanks,scanXStart,scanYStart,scanXEnd,scanYEnd):
    global squares
    Ones = pyautogui.locateAllOnScreen('One.png',region=(scanXStart,scanYStart,scanXEnd,scanYEnd),grayscale=False, confidence=0.9)
    Twos = pyautogui.locateAllOnScreen('Two.png',region=(scanXStart,scanYStart,scanXEnd,scanYEnd),grayscale=False, confidence=0.8)
    Threes = pyautogui.locateAllOnScreen('Three.png',region=(scanXStart,scanYStart,scanXEnd,scanYEnd),grayscale=False, confidence=0.9)
    Fours = pyautogui.locateAllOnScreen('Four.png',region=(scanXStart,scanYStart,scanXEnd,scanYEnd),grayscale=False, confidence=0.9)
    Blanks = pyautogui.locateAllOnScreen('Blank.png',region=(scanXStart,scanYStart,scanXEnd,scanYEnd),grayscale=False,confidence=0.8)
    ones = list(Ones)
    twos = list(Twos)
    threes = list(Threes)
    fours = list(Fours)
    blanks = list(Blanks)
    print("Number of ones found: ",len(ones))
    print("Number of twos found: ",len(twos))
    print("Number of threes found: ",len(threes))
    print("Number of fours found: ",len(fours))
    print("Number of blanks found: ",len(blanks))
    for i in range(81):
        if(Brd[i] == -1):
            pass
        else:
            Brd[i] = 0

    for i in range(81):
        for one in ones:
            x = one.left + 5
            y = one.top + 5
            #print("Coordinate of current 1: ",x," and ,",y)
            if (x > squares[i].left and x < squares[i].left + 20 and y > squares[i].top and y < squares[i].top + 20):
                Brd[i] = 1
        for two in twos:
            x = two.left + 5
            y = two.top + 5
            #print("Coordinate of current 1: ",x," and ,",y)
            if (x > squares[i].left and x < squares[i].left + 20 and y > squares[i].top and y < squares[i].top + 20):
                Brd[i] = 2
        for three in threes:
            x = three.left + 5
            y = three.top + 5
            #print("Coordinate of current 1: ",x," and ,",y)
            if (x > squares[i].left and x < squares[i].left + 20 and y > squares[i].top and y < squares[i].top + 20):
                Brd[i] = 3
        for four in fours:
            x = three.left + 5
            y = three.top + 5
            #print("Coordinate of current 1: ",x," and ,",y)
            if (x > squares[i].left and x < squares[i].left + 20 and y > squares[i].top and y < squares[i].top + 20):
                Brd[i] = 4
        for blank in blanks:
            x = blank.left + 5
            y = blank.top + 5
        #print("Coordinate of current 1: ",x," and ,",y)
            if (x > squares[i].left and x < squares[i].left + 20 and y > squares[i].top and y < squares[i].top + 20):
                Brd[i] = 9

        b1.update_grid(Brd)
        b1.print()
        print(Brd[0:9])
        print(Brd[9:18])
        print(Brd[18:27]) 
        print(Brd[27:36]) 
        print(Brd[36:45]) 
        print(Brd[45:54]) 
        print(Brd[54:63]) 
        print(Brd[63:72]) 
        print(Brd[72:81]) 
main()