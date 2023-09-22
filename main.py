from crossword import *
from creator import *
import os
import time
import matplotlib.pyplot as plt
import numpy as np
import time


class PlotResults:
    """
    Class to plot the results. 
    """
    def plot_results(self, data1, data2, label1, label2, filename):
        """
        This method receives two lists of data point (data1 and data2) and plots
        a scatter plot with the information. The lists store statistics about individual search 
        problems such as the number of nodes a search algorithm needs to expand to solve the problem.

        The function assumes that data1 and data2 have the same size. 

        label1 and label2 are the labels of the axes of the scatter plot. 
        
        filename is the name of the file in which the plot will be saved.
        """
        _, ax = plt.subplots()
        ax.scatter(data1, data2, s=100, c="g", alpha=0.5, cmap=plt.cm.coolwarm, zorder=10)
    
        lims = [
        np.min([ax.get_xlim(), ax.get_ylim()]),  # min of both axes
        np.max([ax.get_xlim(), ax.get_ylim()]),  # max of both axes
        ]
    
        ax.plot(lims, lims, 'k-', alpha=0.75, zorder=0)
        ax.set_aspect('equal')
        ax.set_xlim(lims)
        ax.set_ylim(lims)
        plt.xlabel(label1)
        plt.ylabel(label2)
        plt.grid()
        plt.savefig(filename)

def main():
    running_times_mrv = []
    running_times_wodh = []
    for i in range(1, len(os.listdir('puzzles/'))+1):
        f1 = "puzzles/p" + str(i) + ".txt"
        if i == 11:
            f2 = "words/p" + str(i) + "_words.txt"
        else:
            f2 = "words/test_file.txt"

        crossword_mrv = Crossword(f1, f2)
        # for mrv heuristic
        start = time.perf_counter()
        creation = Creator(crossword_mrv, True)
        assignment = creation.solve()
        assert assignment != None, "failed crossword"
        running_times_mrv.append(time.perf_counter() - start)
        
        print("MRV DONE PUZZLE", i)

        crossword_fa = Crossword(f1, f2)
        # for FA heuristic
        start = time.perf_counter()
        creation = Creator(crossword_fa, False)
        assignment = creation.solve()
        assert assignment != None, "failed crossword"
        running_times_wodh.append(time.perf_counter() - start)
        print("FA DONE PUZZLE", i)

    print(running_times_mrv)
    print(running_times_wodh)
    plotter = PlotResults()
    plotter.plot_results(running_times_mrv, running_times_wodh,
    "Running Time Backtracking (MRV with DH)",
    "Running Time Backtracking (MRV without DH)", "running_time")


if __name__ == "__main__":
    main()