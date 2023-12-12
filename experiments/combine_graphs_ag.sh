#!/bin/bash

# This script plots the learning curve of the agent rewards in the following files

BASEPATH="learning_curve/"
NEWPATH="updated_data/"

function plt_learning_curves(){
    python3 learning_curve_ag.py $BASEPATH$BASE_FILE $NEWPATH$LINEAR_FILE $NEWPATH$PREPROCESSED_FILE $NEWPATH$SIMPLE_FILE
}

function plt_learning_curves_tag(){
    python3 tag_ag_graph.py $BASEPATH$BASE_FILE $NEWPATH$LINEAR_FILE $NEWPATH$PREPROCESSED_FILE $NEWPATH$SIMPLE_FILE
}

BASE_FILE="baseline_simple_adversary_agrewards.pkl"
LINEAR_FILE="good_linear_adv_preprocessed_simple_adversary_agrewards.pkl"
PREPROCESSED_FILE="good_preprocessed_adv_linear_simple_adversary_agrewards.pkl "
SIMPLE_FILE="preprocessed_simple_adversary_agrewards.pkl"

plt_learning_curves


BASE_FILE="baseline_simple_tag_agrewards.pkl"
LINEAR_FILE="good_linear_adv_preprocessed_simple_tag_agrewards.pkl"
PREPROCESSED_FILE="good_preprocessed_adv_linear_simple_tag_agrewards.pkl "
SIMPLE_FILE="preprocessed_simple_tag_agrewards.pkl"

plt_learning_curves_tag

