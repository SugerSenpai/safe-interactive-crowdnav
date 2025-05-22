from setuptools import setup

setup(
    name='sicnav',
    version='0.0.1',
    python_requires='==3.8.13',
    packages=[
        'sicnav',
        'sicnav.policy',
        'sicnav.utils',
        'sicnav.utils.mpc_utils',
        'sicnav.utils.PythonRobotics',
        'sicnav.configs',
        'crowd_sim_plus',
        'crowd_sim_plus.envs',
        'crowd_sim_plus.envs.policy',
        'crowd_sim_plus.envs.utils',
        'RL_nav'
    ],
    package_data={
        'sicnav': [
            'configs/*.config'
        ]
    },
    install_requires=[
        'setuptools==65.5.0',
        'pip==21',
        'wheel==0.38.0',
        # 'numpy',
        # 'scipy',
        # 'torch==1.13.1',
        # 'torchvision==0.14.1',
        # 'stable-baselines3==1.7.0',
        # 'pandas'
    ],
    # extras_require={
    #     'test': [
    #         'pylint',
    #         'pytest',
    #     ],
    # },
)