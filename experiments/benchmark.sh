#!/bin/bash

# This script generates benchmark data for all settings.
# Run this in a conda env with all deps installed.
PYTHONPATH="../multiagent-particle-envs":$PYTHONPATH
export SUPPRESS_MA_PROMPT=1

# Network architecture: 2 layer MLP
NUM_UNITS=128
function run_benchmark() {
    if [[ $EXP_TYPE == "preprocessed" ]]; then
        PP="--preprocess"
    else
        PP=""
    fi
    python train.py --scenario $EXP_NAME --exp-name "$EXP_TYPE"_"$EXP_NAME" --benchmark --benchmark-iters 100000 --load-dir temp/policies/"$EXP_TYPE"_"$EXP_NAME" --num-adversaries $NUM_ADV --num-units $NUM_UNITS $PP --good-policy $GOOD_POLICY --adv-policy $ADV_POLICY
}

# Cooperative navigation
GOOD_POLICY="maddpg"
ADV_POLICY="maddpg"
EXP_NAME="simple_spread"
NUM_ADV=0

EXP_TYPE="baseline"
run_benchmark

EXP_TYPE="preprocessed"
run_benchmark

# Predator-prey
GOOD_POLICY="maddpg"
ADV_POLICY="maddpg"
EXP_NAME="simple_tag"
NUM_ADV=3

EXP_TYPE="baseline"
run_benchmark

EXP_TYPE="preprocessed"
run_benchmark

EXP_TYPE="good_preprocessed_adv_linear"
GOOD_POLICY="preprocess"
ADV_POLICY="maddpg"
run_benchmark

EXP_TYPE="good_linear_adv_preprocessed"
GOOD_POLICY="maddpg"
ADV_POLICY="preprocess"
run_benchmark

# Physical deception
GOOD_POLICY="maddpg"
ADV_POLICY="maddpg"
EXP_NAME="simple_adversary"
NUM_ADV=1

EXP_TYPE="baseline"
run_benchmark

EXP_TYPE="preprocessed"
run_benchmark

EXP_TYPE="good_preprocessed_adv_linear"
GOOD_POLICY="preprocess"
ADV_POLICY="maddpg"
run_benchmark

EXP_TYPE="good_linear_adv_preprocessed"
GOOD_POLICY="maddpg"
ADV_POLICY="preprocess"
run_benchmark