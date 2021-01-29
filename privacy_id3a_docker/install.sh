#!/bin/bash
conda update -n base -c defaults conda
conda init bash
conda create -n privacyidea python=3.7
. /opt/conda/etc/profile.d/conda.sh
conda activate privacyidea
pip install privacyidea gunicorn
pip install -r /opt/conda/envs/privacyidea/lib/privacyidea/requirements.txt
pi-manage create_enckey
pi-manage create_audit_keys
pi-manage createdb
pi-manage db stamp head -d /opt/conda/envs/privacyidea/lib/privacyidea/migrations
pi-manage admin add admin -e admin@localhost -p Pa55w0rd
conda deactivate
