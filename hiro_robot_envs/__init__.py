import gym
from gym.envs.registration import register

register(
        id='iCubReach-v0',
        entry_point='pybullet_robot_envs.envs:iCubReachGymEnv',
        max_episode_steps=1000,
        kwargs={ 'use_IK':1,
                 'control_arm': 'l',
                 'control_orientation': 0,
                 'obj_pose_rnd_std': 0,
                 'max_steps': 1000,
                 'renders': True},
)


# --------------------------- #
def getList():
    btenvs = ['- ' + spec.id for spec in gym.envs.registry.all() if spec.id.find('iCub')>=0]
    return btenvs

getList()
