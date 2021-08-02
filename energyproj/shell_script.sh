#!/bin/bash

cd "$(dirname "${BASH_SOURCE[0]}")"
chmod +x shell_script
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
python3 final_mac.py
