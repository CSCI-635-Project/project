#!/bin/bash

# This script plots the learning curve of the agent rewards in the following files

PYPATH="new_data_training/"

function plt_learning_curves(){
    python3 graph_learning_curve.py $PYPATH$PKL_FILE
}

PKL_FILE="good_linear_adv_preprocessed_simple_adversary_agrewards.pkl"
plt_learning_curves

PKL_FILE="good_linear_adv_preprocessed_simple_adversary_rewards.pkl"
plt_learning_curves

PKL_FILE="good_linear_adv_preprocessed_simple_tag_agrewards.pkl"
plt_learning_curves

PKL_FILE="good_linear_adv_preprocessed_simple_tag_rewards.pkl"
plt_learning_curves

PKL_FILE="good_preprocessed_adv_linear_simple_adversary_agrewards.pkl	"
plt_learning_curves

PKL_FILE="good_preprocessed_adv_linear_simple_adversary_rewards.pkl"
plt_learning_curves

PKL_FILE="good_preprocessed_adv_linear_simple_tag_agrewards.pkl"
plt_learning_curves

PKL_FILE="good_preprocessed_adv_linear_simple_tag_rewards.pkl"
plt_learning_curves

PKL_FILE="preprocessed_simple_adversary_agrewards.pkl"
plt_learning_curves

PKL_FILE="preprocessed_simple_adversary_rewards.pkl"
plt_learning_curves

PKL_FILE="preprocessed_simple_spread_agrewards.pkl"
plt_learning_curves

PKL_FILE="preprocessed_simple_spread_rewards.pkl"
plt_learning_curves

PKL_FILE="preprocessed_simple_tag_agrewards.pkl"
plt_learning_curves

PKL_FILE="preprocessed_simple_tag_rewards.pkl"
plt_learning_curves
