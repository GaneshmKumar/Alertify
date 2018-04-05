from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name = "Alertify",
    version = 1.0,
    description = "A Notification Alert System",
    author = "Ganesh Kumar M",
    author_email = "ganeshkumarm.1996@gmail.com",
    license = "MIT",
    url = "https://github.com/GaneshmKumar/Alertify",
    packages = ["alertify"],
    entry_points={
        'console_scripts':[
            'alertify = alertify.alertify:main'
            ]
        },
    long_description=readme(),
)
