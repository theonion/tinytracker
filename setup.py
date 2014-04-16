from distutils.core import setup

setup(
    name="TinyTracker",
    version="1.0.0",
    description="A small pixel tracker built in python, and designed to send data to carbon.",
    author="Chris Sinchok",
    author_email="csinchok@theonion.com",
    packages=["tinytracker"],
    install_requires=[
        "gevent >= 1.0"
    ]
)
