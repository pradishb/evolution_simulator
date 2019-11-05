# Evolution Simulator

## Demo
### GUI
![main_gui](https://github.com/pradishb/evolution_simulator/raw/master/documentation/demo0.png)
### Analytics
![main_gui](https://github.com/pradishb/evolution_simulator/raw/master/documentation/demo1.png)
### CLI
![main_gui](https://github.com/pradishb/evolution_simulator/raw/master/documentation/demo2.png)
## Simulation
![main_gui](https://github.com/pradishb/evolution_simulator/raw/master/documentation/demo3.png)

## Dependencies
- Install box2d-py from https://github.com/openai/box2d-py
- Intall swig from
- Python 3
- Virtualenv
http://www.swig.org/download.html

## Installation
- Create a virtualenv
```
virtualenv --python python3 venv
```
- Activate the virtualenv
- Install the dependencies
```
pip install -r requirements.txt
```

## Executing
For GUI
```
python main.py
```
For faster training, use CLI
```
python cui.py
usage: cui.py [-h] [--load-path LOAD_PATH] [--repeat REPEAT]

Script to train the creatures using cli

optional arguments:
  -h, --help            show this help message and exit
  --load-path LOAD_PATH, -l LOAD_PATH
                        path to the exisiting generations data
  --repeat REPEAT, -r REPEAT
                        number of generations to train
```
