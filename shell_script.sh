#!/bin/bash

cd "$(dirname "${BASH_SOURCE[0]}")"
python3 -m venv env
source env/bin/activate
pip3 install -r energyproj/requirements.txt
python3 energyproj/final_mac.py
