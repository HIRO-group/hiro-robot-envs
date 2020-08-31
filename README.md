# hiro-robot-envs

A collection of robotic environments (which inherit from gym.Env) for reinforcement learning algorithms.

This repository is a Python package that allows you to use the environments within this repo.

Examples are coming soon!


## Quick Start

* Note - requires at least Python 3.5 or above.

Before installing this package, you will need to install Mujoco,
which requires some extra steps. You can check them out [here](https://github.com/openai/mujoco-py#install-mujoco).

```sh
git clone https://github.com/HIRO-group/hiro-robot-envs
cd hiro-robot-envs
pip3 install .
```

## Example

After installing the package, here's an example of using the
ant environment.

```python
from hiro_robot_envs.envs import AntEnvWithGoal
from hiro_robot_envs.envs import create_maze_env

env = AntEnvWithGoal(create_maze_env('AntMaze'), 'AntMaze')
```
