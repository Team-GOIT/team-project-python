from setuptools import setup, find_packages

setup(
    name="AssistantProjGOIT",
    version="1.0",
    description='Assistant bot which can write to change data',
    url='https://github.com/Team-GOIT/team-project-python',
    author='Karine Morozova, Valerie Matviichuk, Anton Olienykov, Oleksandr G, Yakymovych Roman',
    author_email='k.morozova@tiomarkets.com, lera.matviichuk01@gmail.com, olieinykov@gmail.com, roma.yakimovich@yahoo.com, ',
    packages=find_packages(),
    setup_requires=['prettytable'],
    install_requires=['prettytable', 'prompt-toolkit', 'twilio']
)
