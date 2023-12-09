#!/bin/bash

# This script plots the learning curve of the agent rewards in the following files
# Current working directory should be
# the plots are saved to the current working directory

PYPATH="learning_curve/"

function plt_learning_curves(){
    python3 graph_learning_curve.py $PYPATH$PKL_FILE
}

PKL_FILE="baseline_simple_adversary_agrewards.pkl"
plt_learning_curves

PKL_FILE="baseline_simple_adversary_rewards.pkl"
plt_learning_curves

PKL_FILE="baseline_simple_spread_agrewards.pkl"
plt_learning_curves

PKL_FILE="baseline_simple_spread_rewards.pkl"
plt_learning_curves

PKL_FILE="baseline_simple_crypto_agrewards.pkl"
plt_learning_curves

PKL_FILE="baseline_simple_crypto_rewards.pkl"
plt_learning_curves

PKL_FILE="baseline_simple_tag_agrewards.pkl"
plt_learning_curves

PKL_FILE="baseline_simple_tag_rewards.pkl"
plt_learning_curves

