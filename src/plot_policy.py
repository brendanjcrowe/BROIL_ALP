import matplotlib.pyplot as plt
import numpy as np


def plot_policy(pi, state_space, feature_1_name = "Feature 1", feature_2_name = "Feature 2"):
    # there must be the same number of actions in pi as there are states in our state space
    assert len(pi) == len(state_space)

    # this only works for states with two features
    assert len(pi) > 0
    assert len(state_space[0]) == 2

    phi_0 = set([state[0] for state in state_space])
    phi_1 = set([state[1] for state in state_space])

    data = np.zeros((len(phi_0), len(phi_1)))

    for state, action in zip(state_space, pi):
        data[state[0]][state[1]] = action

    fig = plt.figure()
    ax = fig.add_subplot(111)
    action_colormap = plt.get_cmap('RdBu', max(pi)-min(pi)+1)
    cax = ax.matshow(data, cmap=action_colormap)
    fig.colorbar(cax)

    plt.xlabel(feature_2_name)
    plt.ylabel(feature_1_name)

    plt.show()


def main():
    OPEN = 0
    CLOSED = 1
    state_space = [(0, OPEN), (0, CLOSED), (1, OPEN), (1, CLOSED), (2, OPEN), (2, CLOSED), (3, OPEN), (3, CLOSED)]
    pi = [0, 0, 1, 0, 1, 1, 0, 0]

    plot_policy(pi, state_space, "Case Count", "Closed?")


if __name__ == '__main__':
    main()
