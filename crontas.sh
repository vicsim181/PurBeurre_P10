#!/bin/bash

set -o allexport
source /home/vicsim/PurBeurre_P10/.env
set +o allexport

/home/vicsim/PurBeurre_P10/virenv/bin/python3 /home/vicsim/PurBeurre_P10/manage.py db_feed --settings=pur_beurre.settings.production