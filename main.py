import os
from glob import glob
from framework.framework import main
from environment.environment import Environment


def create_directories():
    if not os.path.exists("data"):
        os.makedirs("data")
    if not os.path.exists("data/vertices"):
        os.makedirs("data/vertices")
    if not os.path.exists("data/edges"):
        os.makedirs("data/edges")


if __name__ == "__main__":
    create_directories()
    main(Environment)
