#!/bin/bash
. /opt/conda/etc/profile.d/conda.sh
conda activate privacyidea
gunicorn --chdir /opt/conda/envs/privacyidea --config /opt/conda/envs/privacyidea/gunicorn.py --daemon wsgi:app
