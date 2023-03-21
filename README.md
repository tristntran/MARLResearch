# MARL Research Folder

## Purpose of this Repo
This repository documents the progress I have made in developing research working towards Multi Agent Reinforcement learning.
## Table of Contents
## Setting Up the Repo

Ensure that you have Docker, VSCode, and the Docker VSCode extension enabled.

Clone this project from GitHub and open the repo in VSCode. If Docker is installed in your computer you will be able to build and reproduce all of the functions.

If you get a module not found error, try running this line of code in your Terminal

`export PYTHONPATH=$PYTHONPATH:./src`

To view tensorboard run the code and run this command in the CLI
`tensorboard --logdir <<logfilename>>`

example:
`tensorboard --logdir ./healthcare/`