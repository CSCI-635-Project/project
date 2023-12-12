import sys
import pickle
import matplotlib.pyplot as plt
import numpy as np


def main():

    rewards_fname = sys.argv[1]
    rewards_file = open(rewards_fname, "rb")
    rewards = pickle.load(rewards_file)
    reward_arry = np.array(rewards)

    pre_simple_fname = sys.argv[2]
    pre_simple_file = open(pre_simple_fname, "rb")
    pre_simple = pickle.load(pre_simple_file)
    simple_arry = np.array(pre_simple)


    NUM_EPISODES=25000

    xpoints_rewrds = []
    ep_offset = 0
    for i in range(NUM_EPISODES+1):
        if ep_offset < NUM_EPISODES:
            ep_offset += NUM_EPISODES/len(rewards)
            if ep_offset <= NUM_EPISODES:
                xpoints_rewrds.append(ep_offset)

    title = rewards_fname.replace("learning_curve/", "")
    title = title.replace(".pkl", "")

    graph_title = "Training Curve for " + title
    plt.title(graph_title)
    plt.xlabel("Number of Episodes")
    plt.ylabel("Agent Rewards")
    plt.plot(xpoints_rewrds, reward_arry, label="Baseline")
    plt.plot(xpoints_rewrds, simple_arry, label="Preprocessed Simple")
    plt.legend()
    out_fig_name = title + "_training_curve"
    plt.savefig(out_fig_name)
    plt.close()


main()
