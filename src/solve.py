# process 50 mazes with all variations of the algorithm
import os
import fnmatch
import glob
import sys
import bisect
import multiprocessing


def filebrowser(ext=""):
    return [f for f in glob.glob(f"*{ext}")]


def solveMaze(command):
    os.system(command)
    print("this command: ", command, " is done")


if __name__ == "__main__":
    print("Lets solve some mazes \n")
    # solve with forward A*
    # large and small g
    # solve with backward A*
    # solve with adaptive A*

    # get all maze names and cycle through them
    #command = "Python pathfinding.py "+ maze + "m " + "s"
    # os.system(command)

    #x = filebrowser(".txt")
    # print(x)

    # get a list of every file in given path
    backTrackerMazes = os.listdir("./arrs/backTrackerMazes")
    mazes = []
    for f in backTrackerMazes:  # only adds maze files to the list of mazes we will run
        if fnmatch.fnmatch(f, "*.txt"):
            bisect.insort(mazes, f)
    print(mazes)

    # user running mac or windows
    if sys.argv[1] == 'm':
        system = ' m'
    if sys.argv[1] == 'w':
        system = ' w'

    reports = ['largeG_report.txt', 'smallG_report.txt',
               'backwards_report.txt', 'adaptive_report.txt']  # files to write reports to
    algorithms = [' l ', ' s ', ' b ', ' a ']

    for x in reports:  # clears any data that is in the reports
        open(x, 'w')

    multiprocessing.freeze_support()
    num_proc = os.cpu_count()
    pool = multiprocessing.Pool(processes=num_proc)
    commands = []
    # execute all mazes for all algorithms
# for i in range(4):  # execute all algorithms
    missingMazes = ['88.txt', '89.txt', '90.txt']
    for maze in missingMazes:  # executes all backtracker mazes
        print("Python pathfinding.py " + maze +
              system + algorithms[1] + reports[1])
        command = "Python pathfinding.py " + maze + \
            system + algorithms[1] + reports[1]
        commands.append(command)
        # os.system(command)

    pool.map(solveMaze, commands)
    pool.close()
    pool.join()

    # demo mode vs report mode
