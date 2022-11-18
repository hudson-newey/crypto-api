#!/bin/bash
# installs a local virtual environment
initilize_python_virtual_environment() {
    # check what python version to use
    which python3;
    USE_PYTHON3=0;
    if [ $? -eq 0 ]; then
        USE_PYTHON3=1;
    else
        which python;
        if [ $? -eq 0 ]; then
            USE_PYTHON3=0;
        else
            echo "Error: Neither Python2 or Python3 found in PATH";
            exit;
        fi
    fi

    # create the python virtual environment
    if [ $USE_PYTHON3 -eq 1 ]; then
        python3 -m venv ./venv/;
    else
        python -m venv ./venv/;
    fi
    source ./venv/bin/activate;

    # install requirements.txt
    if [ -f ./requirements.txt ]; then
        if [ $USE_PYTHON3 -eq 1 ]; then
            pip3 install -r ./requirements.txt;
        else
            pip install -r ./requirements.txt;
        fi
    else
        echo "Creating empty requirements.txt";
        touch requirements.txt;
    fi
}

# call activate() to initilize & install python3 virtual environment
activate_python() {
    if [ ! -d ./venv/ ]; then
        initilize_python_virtual_environment;
    else
        source ./venv/bin/activate;
    fi
}

# call this at the end of your program to deactivate the python3 virtual environment
deactivate_python() {
    deactivate;

    if [ -d ./venv/ ]; then
        rm -r ./venv/;
    fi
}

init_environment() {
  if [ ! -f ./.gitignore ]; then
    echo "Creating Python .gitignore";
    wget https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore -O .gitignore;
  fi
}

main() {
  if [ "$(id -u)" -eq 0 ]; then
    echo -e "\e[93m[WARNING] Python is running as Root!\e[39m";
  fi

  init_environment;

  activate_python;

  python3 ./src/main.py;

  deactivate_python;
}

main;

