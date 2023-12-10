# CS635 Final Project

Our code is derived from the original repository for the paper
[Multi-Agent Actor-Critic for Mixed Cooperative-Competitive Environments](https://arxiv.org/pdf/1706.02275.pdf).
It uses
[Multi-Agent Particle Environments (MPE)](https://github.com/openai/multiagent-particle-envs).
to evaluate changes.
After the updated installation instructions, the rest of this README is almost verbatim from the original source.

In our project, we implemented a permutation invariant architecture to scalably
process observations and actions from multiple agents. The environments we
trained on were `simple_spread`, `simple_tag`, and `simple_adversary`.
- `simple_spread` is a pure cooperative task where agents attempt to cover all
landmarks in the environment without colliding with each other.
- `simple_tag` is a mixed environment where multiple prey must avoid a predator.
- `simple_adversary` is a mixed environment where one team must attempt to cover
the correct landmark which is only visible to them, while the other team must
guess which landmark is the correct landmark and cover it instead.

Our experiments make use of baseline networks, which are 2-layer MLPs with 128
neurons per hidden layer, and permutation invariant networks, which use a
special permutation invariant architecture for processing multiple agent
observations/actions per team. Each permutation invariant block uses 3 1D
convolutional layers with a kernel size of 1 to simulate processing each agent's
observations and actions via an MLP individually. The output of these operations
are then averaged across all agents to produce a single vector per team. Each
"team vector" is concatenated, then passed to the original baseline
architecture. We do not take into account the increased number of parameters
this modification brings.

The experiments were performed on `lovegood`, on a Tesla T4 GPU.

## Quickstart

Navigate to the `experiments` folder in this repository. Then, create the folders `benchmark_files`, `learning_curves`, and `temp/policies`.

```bash
cd experiments
mkdir benchmark_files learning_curves temp temp/policies
```

Next, run `train_agents.sh`. This trains baseline policies and permutation
invariant policies for all environments. For mixed environments (`simple_tag`
and `simple_adversary`), the script will also train in a setting where one team
uses the baseline network architecture, while the other team uses the modified
architecture. This script will take several hours to run.

```bash
./train_agents.sh
```

Once the agents are trained, you'll be able to see trained policies in `temp/policies`.

TODO: Create script to generate benchmark data

## Installation

### Instructions **(UPDATED!)**

Make sure you have conda, then `cd` into this directory and type `conda env create -f environment.yml`.

This will create a new Conda environment called `maddpg` with all the dependencies we need.

Activate it with `conda activate maddpg`.

Afterwards, rename this directory from `project` to `maddpg`. Then, install it with `pip install -e .`.

## Case study: Multi-Agent Particle Environments

We demonstrate here how the code can be used in conjunction with the
[Multi-Agent Particle Environments (MPE)](https://github.com/openai/multiagent-particle-envs).

- Download and install the MPE code [here](https://github.com/openai/multiagent-particle-envs)
by following the `README`.

- Ensure that `multiagent-particle-envs` has been added to your `PYTHONPATH` (e.g. in `~/.bashrc` or `~/.bash_profile`).

- To run the code, `cd` into the `experiments` directory and run `train.py`:

``python train.py --scenario simple``

- You can replace `simple` with any environment in the MPE you'd like to run.

## Command-line options

### Environment options

- `--scenario`: defines which environment in the MPE is to be used (default: `"simple"`)

- `--max-episode-len` maximum length of each episode for the environment (default: `25`)

- `--num-episodes` total number of training episodes (default: `60000`)

- `--num-adversaries`: number of adversaries in the environment (default: `0`)

- `--good-policy`: algorithm used for the 'good' (non adversary) policies in the environment
(default: `"maddpg"`; options: {`"maddpg"`, `"ddpg"`, `"preprocess"` **(NEW!)**})

- `--adv-policy`: algorithm used for the adversary policies in the environment
(default: `"maddpg"`; options: {`"maddpg"`, `"ddpg"`, `"preprocess"` **(NEW!)**})

### Core training parameters

- `--lr`: learning rate (default: `1e-2`)

- `--gamma`: discount factor (default: `0.95`)

- `--batch-size`: batch size (default: `1024`)

- `--num-units`: number of units in the MLP (default: `64`)

- `--preprocess`: whether or not to use our permutation invariant architecture (default: `False`) **(NEW!)**

### Checkpointing

- `--exp-name`: name of the experiment, used as the file name to save all results (default: `None`)

- `--save-dir`: directory where intermediate training results and model will be saved (default: `"/tmp/policy/"`)

- `--save-rate`: model is saved every time this number of episodes has been completed (default: `1000`)

- `--load-dir`: directory where training state and model are loaded from (default: `""`)

### Evaluation

- `--restore`: restores previous training state stored in `load-dir` (or in `save-dir` if no `load-dir`
has been provided), and continues training (default: `False`)

- `--display`: displays to the screen the trained policy stored in `load-dir` (or in `save-dir` if no `load-dir`
has been provided), but does not continue training (default: `False`)

- `--benchmark`: runs benchmarking evaluations on saved policy, saves results to `benchmark-dir` folder (default: `False`)

- `--benchmark-iters`: number of iterations to run benchmarking for (default: `100000`)

- `--benchmark-dir`: directory where benchmarking data is saved (default: `"./benchmark_files/"`)

- `--plots-dir`: directory where training curves are saved (default: `"./learning_curves/"`)

## Code structure

- `./experiments/train.py`: contains code for training MADDPG on the MPE

- `./maddpg/trainer/maddpg.py`: core code for the MADDPG algorithm

- `./maddpg/trainer/replay_buffer.py`: replay buffer code for MADDPG

- `./maddpg/common/distributions.py`: useful distributions used in `maddpg.py`

- `./maddpg/common/tf_util.py`: useful tensorflow functions used in `maddpg.py`