#!/bin/bash
set +ue
set -x
nice -19 ./diff.py db/db1.csv db/db2.csv