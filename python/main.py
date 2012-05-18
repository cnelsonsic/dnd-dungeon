
import sys

from jbmaze import JBMaze
from jbmazept import JBMazePt
from jbmazemask import JBMazeMask

def drawAsStructure(image, maze, path, _len, **opts):
    pass

def gdImagePng(image, stdout):
    pass

def gdImageDestroy(image):
    pass

def main(**opts):
    path = JBMazePt()
    _len = 0
    image = None

    print "current seed: %d" % (opts.get('seed'))

    # construct the maze

    maze = JBMaze(opts.get('width'), opts.get('height'), opts.get('depth'), opts.get('seed'), opts.get('randomness'),
                  opts.get('startx'), opts.get('starty'), opts.get('startz'), opts.get('endx'), opts.get('endy'), opts.get('endz'))

    # load the mask

    if opts.get('maskFile')[0] != 0:
        maze.setMask(JBMazeMask(opts.get('maskFile')))

    # generate it
    maze.generate()

    # solve it
    maze.solve(path, _len)

    # sparsify it
    maze.sparsify(opts.get('sparseness'))

    # clear up the deadends by reconnecting them into an existing passage
    maze.clearDeadends(opts.get('deadends'))

    # draw it

    drawAsStructure(image, maze, path, _len, **opts)

    gdImagePng(image, sys.stdout)

    gdImageDestroy(image)
    del maze
    return 0

