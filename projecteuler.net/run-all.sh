#!/bin/sh

export PYTHONPATH=$PYTHONPATH:./libs

ls problem_*py | xargs -n1 python
