#!/bin/bash

# This script trains agents on each environment.
# Run this in a conda env with all deps installed.
PYTHONPATH="../multiagent-particle-envs":$PYTHONPATH
export SUPPRESS_MA_PROMPT=1

# Network architecture: 2 layer MLP
# Number of training episodes: 25000
NUM_UNITS=128
NUM_EPISODES=25000
function run_exp() {
    if [[ $EXP_TYPE == "baseline" ]]; then
        PP=""
    else
        PP="--preprocess"
    fi
    python train.py --scenario $EXP_NAME --exp-name "$EXP_TYPE"_"$EXP_NAME" --save-dir temp/policies/"$EXP_TYPE"_"$EXP_NAME" --num-adversaries $NUM_ADV --num-units $NUM_UNITS --num-episodes $NUM_EPISODES $PP
}

# Cooperative navigation
EXP_NAME="simple_spread"
NUM_ADV=0
EXP_TYPE="baseline"
run_exp
EXP_TYPE="preprocessed"
run_exp

# Predator-prey
EXP_NAME="simple_tag"
NUM_ADV=3
EXP_TYPE="baseline"
run_exp
EXP_TYPE="preprocessed"
run_exp

# Physical deception
EXP_NAME="simple_adversary"
NUM_ADV=1
EXP_TYPE="baseline"
run_exp
EXP_TYPE="preprocessed"
run_exp