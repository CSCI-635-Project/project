import sys
import pickle
import matplotlib.pyplot as plt
import numpy as np


def main():

    rewards_fname = sys.argv[1]
    rewards_file = open(rewards_fname, "rb")
    rewards = pickle.load(rewards_file)

    rewards_per_agent = []
    for x in range(0,len(rewards)-3,4):
        reward1 = rewards[x]
        reward2 = rewards[x+1]
        reward3 = rewards[x+2]
        reward4 = rewards[x+3]
        temp = [reward1, reward2, reward3, reward4]
        rewards_per_agent.append(temp)

    linear_fname = sys.argv[2]
    linear_file = open(linear_fname, "rb")
    linear = pickle.load(linear_file)

    linear_per_agent = []
    for x in range(0,len(linear)-3,4):
        linear1 = linear[x]
        linear2 = linear[x+1]
        linear3 = linear[x+2]
        linear4 = linear[x+3]
        temp = [linear1, linear2,linear3, linear4]
        linear_per_agent.append(temp)

    preprocessed_fname = sys.argv[3]
    preprocessed_file = open(preprocessed_fname, "rb")
    preprocessed = pickle.load(preprocessed_file)

    preproc_per_agent = []
    for x in range(0,len(preprocessed)-3,4):
        preproc1 = preprocessed[x]
        preproc2 = preprocessed[x+1]
        preproc3 = preprocessed[x+2]
        preproc4 = preprocessed[x+3]
        temp = [preproc1, preproc2, preproc3, preproc4]
        preproc_per_agent.append(temp)

    pre_simple_fname = sys.argv[4]
    pre_simple_file = open(pre_simple_fname, "rb")
    pre_simple = pickle.load(pre_simple_file)

    simple_per_agent = []
    for x in range(0,len(pre_simple)-3,4):
        simple1 = pre_simple[x]
        simple2 = pre_simple[x+1]
        simple3 = pre_simple[x+2]
        simple4 = pre_simple[x+3]
        temp = [simple1, simple2, simple3]
        simple_per_agent.append(temp)

    NUM_EPISODES=25000

# get adversaries
    adversary_baseline = []
    for current_list in rewards_per_agent:
        cur_adversary = current_list[0]
        adversary_baseline.append(cur_adversary)
    reward_arry = np.array(adversary_baseline)

    linear_adversary = []
    for current_list in linear_per_agent:
        cur_adversary = current_list[0]
        linear_adversary.append(cur_adversary)
    linear_arry = np.array(linear_adversary)

    preproc_adversary= []
    for current_list in preproc_per_agent:
        cur_adversary = current_list[0]
        preproc_adversary.append(cur_adversary)
    preprocessed_arry = np.array(preproc_adversary)

    simple_adversary= []
    for current_list in simple_per_agent:
        cur_adversary = current_list[0]
        simple_adversary.append(cur_adversary)
    simple_arry = np.array(simple_adversary)

# get one agent
    agent_baseline = []
    for current_list in rewards_per_agent:
        cur_adversary = current_list[3]
        agent_baseline.append(cur_adversary)
    reward_arry_agent = np.array(agent_baseline)

    linear_agent = []
    for current_list in linear_per_agent:
        cur_adversary = current_list[3]
        linear_agent.append(cur_adversary)
    linear_arry_agent = np.array(linear_agent)

    preproc_agent = []
    for current_list in preproc_per_agent:
        cur_adversary = current_list[3]
        preproc_agent.append(cur_adversary)
    preprocessed_arry_agent = np.array(preproc_agent)

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

    graph_title = "Adversary Learning Curve for " + title
    plt.title(graph_title)
    plt.xlabel("Number of Episodes")
    plt.ylabel("Adversary Rewards")
    plt.plot(xpoints_rewrds, reward_arry, label="Baseline")
    plt.plot(xpoints_rewrds, preprocessed_arry, label="Good Preprocessed")
    plt.plot(xpoints_rewrds, linear_arry, label="Good Linear Adv")
    plt.plot(xpoints_rewrds, simple_arry, label="Preprocessed Simple")
    plt.legend()
    out_fig_name = "adversary_" + title + "_learning_curve"
    plt.savefig(out_fig_name)
    plt.close()

    graph_title = "Agent Learning Curve for " + title
    plt.title(graph_title)
    plt.xlabel("Number of Episodes")
    plt.ylabel("Agent Rewards")
    plt.plot(xpoints_rewrds, reward_arry_agent, label="Baseline")
    plt.plot(xpoints_rewrds, preprocessed_arry_agent, label="Good Preprocessed")
    plt.plot(xpoints_rewrds, linear_arry_agent, label="Good Linear Adv")
    plt.plot(xpoints_rewrds, simple_arry_agent, label="Preprocessed Simple")
    plt.legend()
    out_fig_name = "agent_" + title + "_learning_curve"
    plt.savefig(out_fig_name)
    plt.close()


main()
