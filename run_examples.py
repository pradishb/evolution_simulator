import glob
import os

for file_name in glob.glob("examples/*.py"):
    base_name = os.path.splitext(os.path.basename(file_name))[0]

    os.system("pipenv run python -m examples.{}".format(base_name))
