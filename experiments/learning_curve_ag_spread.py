import sys
import pickle
import matplotlib.pyplot as plt
import numpy as np


def main():

    rewards_fname = sys.argv[1]
    rewards_file = open(rewards_fname, "rb")
    rewards = pickle.load(rewards_file)

    rewards_per_agent = []
    for x in range(0,len(rewards)-2,3):
        reward1 = rewards[x]
        reward2 = rewards[x+1]
        reward3 = rewards[x+2]
        temp = [reward1, reward2, reward3]
        rewards_per_agent.append(temp)


    pre_simple_fname = sys.argv[2]
    pre_simple_file = open(pre_simple_fname, "rb")
    pre_simple = pickle.load(pre_simple_file)

    simple_per_agent = []
    for x in range(0,len(pre_simple)-1,3):
        simple1 = pre_simple[x]
        simple2 = pre_simple[x+1]
        simple3 = pre_simple[x+2]
        temp = [simple1, simple2, simple3]
        simple_per_agent.append(temp)

    NUM_EPISODES=25000

# get adversaries
    adversary_baseline = []
    for current_list in rewards_per_agent:
        cur_adversary = current_list[0]
        adversary_baseline.append(cur_adversary)
    reward_arry = np.array(adversary_baseline)

    simple_adversary= []
    for current_list in simple_per_agent:
        cur_adversary = current_list[0]
        simple_adversary.append(cur_adversary)
    simple_arry = np.array(simple_adversary)

# get one agent
    agent_baseline = []
    for current_list in rewards_per_agent:
        cur_adversary = current_list[2]
        agent_baseline.append(cur_adversary)
    reward_arry_agent = np.array(agent_baseline)

    simple_agent = []
    for current_list in simple_per_agent:
        cur_adversary = current_list[2]
        simple_agent.append(cur_adversary)
    simple_arry_agent = np.array(simple_agent)

    xpoints_rewrds = []
    ep_offset = 0
    for i in range(NUM_EPISODES+1):
        if ep_offset < NUM_EPISODES:
            ep_offset += NUM_EPISODES/len(rewards_per_agent)
            if ep_offset <= NUM_EPISODES:
                xpoints_rewrds.append(ep_offset)

    title = rewards_fname.replace("learning_curve/", "")
    title = title.replace(".pkl", "")
    title = title.replace("baseline_", "")
    #title = "simple_tag"

    '''graph_title = "Adversary Learning Curve for " + title
    plt.title(graph_title)
    plt.xlabel("Number of Episodes")
    plt.ylabel("Adversary Rewards")
    plt.plot(xpoints_rewrds, reward_arry, label="Baseline")
    plt.plot(xpoints_rewrds, simple_arry, label="Preprocessed Simple")
    plt.legend()
    out_fig_name = "adversary_" + title + "_learning_curve"
    plt.savefig(out_fig_name)
    plt.close()'''

    graph_title = "Agent Learning Curve for " + title
    plt.title(graph_title)
    plt.xlabel("Number of Episodes")
    plt.ylabel("Agent Rewards")
    plt.plot(xpoints_rewrds, reward_arry_agent, label="Baseline")
    plt.plot(xpoints_rewrds, simple_arry_agent, label="Preprocessed Simple")
    plt.legend()
    out_fig_name = "agent_" + title + "_learning_curve"
    plt.savefig(out_fig_name)
    plt.close()


main()
