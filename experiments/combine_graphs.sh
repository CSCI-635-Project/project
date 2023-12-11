#!/bin/bash

# This script plots the learning curve of the agent rewards in the following files

BASEPATH="learning_curve/"
NEWPATH="new_data_training/"

function plt_learning_curves(){
    python3 graph_learning_curve_combined.py $BASEPATH$BASE_FILE $NEWPATH$LINEAR_FILE $NEWPATH$PREPROCESSED_FILE
}

BASE_FILE="baseline_simple_adversary_rewards.pkl"
LINEAR_FILE="good_linear_adv_preprocessed_simple_adversary_rewards.pkl"
PREPROCESSED_FILE="preprocessed_simple_adversary_rewards.pkl"

plt_learning_curves

BASE_FILE="baseline_simple_adversary_agrewards.pkl"
LINEAR_FILE="good_linear_adv_preprocessed_simple_adversary_agrewards.pkl"
PREPROCESSED_FILE="preprocessed_simple_adversary_agrewards.pkl"

plt_learning_curves

BASE_FILE="baseline_simple_tag_rewards.pkl"
LINEAR_FILE="good_linear_adv_preprocessed_simple_tag_rewards.pkl"
PREPROCESSED_FILE="preprocessed_simple_tag_rewards.pkl"

plt_learning_curves

BASE_FILE="baseline_simple_tag_agrewards.pkl"
LINEAR_FILE="good_linear_adv_preprocessed_simple_tag_agrewards.pkl"
PREPROCESSED_FILE="preprocessed_simple_tag_agrewards.pkl"

plt_learning_curves
