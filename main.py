import random as rd
import matplotlib.pyplot as plt

import constants as cst


def nCompute(height:int)->int:
    """Compute how many grains will fall"""
    if height > 1:
        return int((height + 2.00) / 2 * rd.random()) + 1     # 1 < nb_fallen_grains < height / 2 + 2
    return 0

def initialization(nb_stacks:int)->list:
    """Create the list of nb_stack stacks"""
    return [0] * (nb_stacks + 1)

def refresh(stacks:list, nb_lost:int)->list:
    """Refresh the automaton: grains can fall from a stack to another"""
    nb_stacks = len(stacks)
    for i in range(1, nb_stacks):
        nb_fallen_grains = nCompute(stacks[i - 1] - stacks[i])     # Choose randomly the number of fallen grains
        stacks[i - 1] -= nb_fallen_grains
        if i == nb_stacks - 1:     # If the grains disapear on the right
            nb_lost += nb_fallen_grains
        else:
            stacks[i] += nb_fallen_grains
    return stacks, nb_lost


if __name__ == "__main__":
    nb_lost = 0
    height = int(input("Number of stacks: "))     # You can try 100
    assert(height > 0)
    stacks = initialization(height)
    stacks[0] = 1

    while nb_lost < cst.MAX_LOST_GRAINS:
        nb_added_grains = 0
        while nb_added_grains < cst.MAX_GRAINS_PER_LOOP:     # I add one grain every cst.MAX_GRAINS_PER_LOOP until cst.MAX_LOST_GRAINS grains lost
            nb_lost = refresh(stacks, nb_lost)[1]
            nb_added_grains += 1
        stacks[0] += 1
    
    x_height = []
    y_nb_stacks = []

    for x in range(0, height):     # The last stack is always empty
        for y in range(1, stacks[x] + 1):
            x_height.append(x)
            y_nb_stacks.append(y)
    
    plt.figure("Cellular Automaton")
    plt.grid(color = "black", linestyle = "-", linewidth = 0.1)
    plt.axis("equal")
    plt.scatter(x_height, y_nb_stacks, color = "yellow", marker = ".", linewidths = 0.01)
    plt.title("Sand Stack Simulation")
    plt.xlabel("Stack n°")
    plt.ylabel("Number of grains")
    plt.show()