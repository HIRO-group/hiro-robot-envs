from hiro_robot_envs.envs.ant_envs.create_maze_env import create_maze_env
import gym
from gym.envs.registration import register

register(
        id='antEnv-v0',
        entry_point='hiro_robot_envs.envs:EnvWithGoal',
        max_episode_steps=1000,
        kwargs={'base_env': create_maze_env('AntMaze'),
                'env_name': 'AntMaze'},
)


# --------------------------- #
def getList():
    btenvs = ['- ' + spec.id for spec in gym.envs.registry.all() if spec.id.find('iCub')>=0]
    return btenvs

getList()
