"""

Run the maze game

"""

import argparse
import sys
from mazegame import *

def main():
    
    parser = argparse.ArgumentParser(description='Play different types of maze games')
    parser.add_argument('-r','--random',help='Play the random game',action='store_true')
    parser.add_argument('-f','--file',help='Play the file-based game',action='store_true')
    parser.add_argument('-i','--interactive',help='Play the interactive game',action='store_true')
    parser.add_argument('-d','--dimension',help='Matrix dimension (required for random games)',type=int,default=10)
             
    args = parser.parse_args()

    if args.random:
        dim = args.dimension
        game = RandomMazeGame2(int(dim))
        game.runGame()
    elif args.file:
        game = FilebasedMazeGame()
        game.runGame()
    elif args.interactive:
        game = InteractiveMazeGame()
        game.runGame()        
        
    
if __name__ == "__main__":
    if len(sys.argv)==1:
        sys.argv.append('-h')
    
    main()


