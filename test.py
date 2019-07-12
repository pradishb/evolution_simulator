import os
import glob

for example in glob.glob("examples/*.py")[10:]:
    file_name = os.path.basename(example).split(".")[0]
    print("Starting module %s" % file_name)
    os.system("pipenv run python -m examples.%s" % file_name)
