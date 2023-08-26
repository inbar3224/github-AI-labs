# Inbar Lev Tov 316327246
# Gal Gibly 315093435
# Note that the assignment was done with python version 3.11.0


from Parameters import *
from CoEvolution import *


def main():
    # get parameters
    popS, genS, vectorS = getParameters()

    # create environment
    coevolution = CoEvolution(popS, genS, vectorS)
    maxNetworkFitness, maxVectorFitness, numOfComparators = coevolution.evolution()

    for generation in range(genS):
        print(f"Generation {generation + 1}:")

        print(f"Best vector fitness: {maxVectorFitness[generation]}")
        vectorI = coevolution.vectorP[np.argmax(maxVectorFitness[generation])]
        print(f"The vector itself: {vectorI.vector}")

        print(f"Best sorting network fitness: {maxNetworkFitness[generation]}")
        networkI = coevolution.networkP[np.argmax(maxNetworkFitness[generation])]
        print(f"The network itself: ")
        for i in range(networkI.numOfComparators):
            print(networkI.comparators[i], end = ', ')
        print()

        print(f"Best number of comparators: {numOfComparators[generation]}")
        print()

    # Plotting fitness scores
    plt.plot(range(genS), maxNetworkFitness, label='Network Fitness')
    plt.plot(range(genS), maxVectorFitness, label='Vector Fitness')
    plt.xlabel('Generation')
    plt.ylabel('Fitness')
    plt.title('Fitness Scores over Generations')
    plt.legend()
    plt.show()

    coevolution.networkP[0].draw()


if __name__ == "__main__":
    main()