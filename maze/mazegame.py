"""

Different types of Maze game classes

"""

from mazefactory import MazeFactory, MazeReader
from solver import MazeSolver

class MazeGame(object):

    def __init__(self, w=0, h=0):
        self._start = (0,0)
        self._end = (0,0)
        
    def createMaze(self):
        return None

    def getStartEndPoints(self, maze):
        return None
    
    def runGame(self):

        maze = self.createMaze()
        if not maze:
            return None
        
        print(maze)
        self.getStartEndPoints(maze)
        
        # Dump it to maze.txt
        # open('maze.txt','w').write(str(maze))
        maze.save()
        
        solver = MazeSolver(maze)

        open ('maze_pts.txt','w').write(str(self._start) + ' ' + str(self._end) + '\n')
        solver.setStartPoint(self._start)
        solver.setEndPoint(self._end)
        solver.solve()

class InteractiveMazeGame(MazeGame):

    def createMaze(self):
        f = MazeFactory()
        return f.makeMaze()

    def getStartEndPoints(self, maze):

        while True:
            try:
                pt1 = raw_input('Enter starting point: ')
                x,y = pt1.split()
                self._start = (int(x), int(y))
                maze.validatePoint(self._start)
                break
            except:
                pass

        while True:
            try:
                pt2 = raw_input('Enter ending point: ')
                x,y = pt2.split()
                self._end = (int(x), int(y))        
                maze.validatePoint(self._end)
                break
            except:
                pass        
        
class FilebasedMazeGame(MazeGame):

    def createMaze(self):
        f = MazeFactory()
        return f.makeMaze(MazeReader.FILE)

    def getStartEndPoints(self, maze):

        filename = raw_input('Enter points file: ').strip()
        try:
            line = open(filename).readlines()[0].strip()
            l = line.split(')')
            self._start = eval(l[0].strip() + ')')
            self._end = eval(l[1].strip() + ')')
        except (OSError, IOError, Exception) as e:
            print(e)
            sys.exit(0)
        
class RandomMazeGame(MazeGame):

    def __init__(self, w=0, h=0):
        super(RandomMazeGame, self).__init__(w, h)
        self._dimension = w
        
    def createMaze(self):
        f = MazeFactory()
        return f.makeRandomMaze(self._dimension)    

    def getStartEndPoints(self, maze):

        pt1, pt2 = (0,0), (0,0)
        while pt1 == pt2:
            pt1 = maze.getRandomStartPoint()
            pt2 = maze.getRandomEndPoint()

        self._start = pt1
        self._end = pt2

class RandomMazeGame2(RandomMazeGame):
    """ Random maze game with distant points """

    def getStartEndPoints(self, maze):

        pt1, pt2 = (0,0), (0,0)
        flag = True
        while flag:
            pt1 = maze.getRandomStartPoint()
            pt2 = maze.getRandomEndPoint()
            # Try till points are at least
            # half maze apart
            xdist = maze.calcXDistance(pt1, pt2)
            ydist = maze.calcYDistance(pt1, pt2)            
            if xdist>=float(maze.getWidth())/2.0 or \
               ydist>=float(maze.getHeight())/2.0:
                flag = False
            
        self._start = pt1
        self._end = pt2    

