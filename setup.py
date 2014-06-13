from distutils.core import setup

setup(
    name="TinyTracker",
    version="1.0.4",
    description="A small pixel tracker built in python, and designed to send data to carbon.",
    author="Chris Sinchok",
    author_email="csinchok@theonion.com",
    packages=["tinytracker"],
    install_requires=[
        "gevent >= 1.0"
    ],
    url="https://github.com/theonion/tinytracker"
)
