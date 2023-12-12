#!/bin/bash

# This script plots the learning curve of the agent rewards in the following files

BASEPATH="learning_curve/"
NEWPATH="updated_data/"

function plt_learning_curves_single(){
    python3 graph_learning_curve_sinlge.py $BASEPATH$BASE_FILE $NEWPATH$SIMPLE_FILE
}

function plt_learning_curves_single_ag(){
    python3 learning_curve_ag_spread.py $BASEPATH$BASE_FILE $NEWPATH$SIMPLE_FILE
}

BASE_FILE="baseline_simple_spread_rewards.pkl "
SIMPLE_FILE="preprocessed_simple_spread_rewards.pkl"

plt_learning_curves_single

BASE_FILE="baseline_simple_spread_agrewards.pkl "
SIMPLE_FILE="preprocessed_simple_spread_agrewards.pkl"

plt_learning_curves_single_ag
