import sys

from crossword import *


class Creator():

    def __init__(self, crossword, heuristic):
        '''
        initializes new crossword to inherit from crossword class
        also initializes domain for each variable
        '''
        self.crossword = crossword
        self.heuristic = heuristic
        self.domains = {}
        for var in self.crossword.variables:
            self.domains[var] = self.crossword.words.copy()
    def is_domain_consistent(self):
        '''
        enforces node consistency by looking at length of words
        '''
        for variable in self.domains:
            for word in set(self.domains[variable]):
                if len(word) != variable.length: self.domains[variable].remove(word)


    def revise(self, x, y):
        '''
        This is the revise algorithm similar to the algorithm on page 79 in notes
        determines if arc x is consistent with y
        '''
        removed = False
        i, j = self.crossword.overlaps[x, y]

        for word1 in set(self.domains[x]):
            remove = True
            for word2 in self.domains[y]:
                if word1[i] == word2[j]:
                    remove = False
            if remove:
                self.domains[x].remove(word1)
                removed = True
        return removed


    def pre_process_ac3(self):
            arcs = list()
            for x in self.domains:
                for y in self.crossword.neighbours(x):
                    arcs.append((x, y))
            return arcs


    def ac3(self, arcs = None):
        '''
        This is the arc consistency algorithm
        '''
        while arcs:
            x,y = arcs.pop()
            if self.revise(x,y):
                if not self.domains[x]: return False
                for x_k in self.crossword.neighbours(x) - self.domains[y]:
                    arcs.append((x_k,x))
        return True



    def is_assign_consistent(self, assignment):
        used = set()
        for v in assignment:
            if assignment[v] not in used:
                used.add(assignment[v])
            else:
                return False
            for n in self.crossword.neighbours(v):
                if n in assignment:
                    i, j = self.crossword.overlaps[v, n]
                    if assignment[v][i] != assignment[n][j]: return False
        return True

    def is_solved(self, assignment):
        '''
        Helper function to show whether the crossword is complete 
        '''
        return not bool(self.crossword.variables - set(assignment))

    def select_unassigned_var(self, assignment, heuristic):
        '''
        we select minimum remaining value(mrv) vs the minimum remaining value heuristic (mrv) with the degree heuristic based
        off of the boolean heuristic 
        '''
        if heuristic == True:
            # mrv with dh
            best = None
            for var in self.crossword.variables - set(assignment):
                if (best is None or len(self.domains[var]) < len(self.domains[best]) or len(self.crossword.neighbours(var)) > len(self.crossword.neighbours(best))): # adds degree heuristic
                    best = var
        if heuristic == False:
            #mrv
            best = None
            for var in self.crossword.variables - set(assignment):
                if (best is None or len(self.domains[var]) < len(self.domains[best])): # simple mrv
                    best = var
        return best

    def backtrack(self, assignment):
        '''
        Here we use the backtracking algorithm catered towards the crossword csp
        '''
        if self.is_solved(assignment):
            return assignment
        var = self.select_unassigned_var(assignment, self.heuristic)

        for value in self.domains[var]:
            assignment[var] = value
            if self.is_assign_consistent(assignment):
                result = self.backtrack(assignment)
                if result is not None: return result
            assignment.pop(var)
        return None
    
    def solve(self):
        self.is_domain_consistent()
        arcs = self.pre_process_ac3()
        self.ac3(arcs)
        return self.backtrack(dict())