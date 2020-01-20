#!/usr/bin/env sh

RC_FILE=${PWD}/.pylintrc
BASE=${PWD}/django_rest_template

cd "${BASE}" || exit
pylint "--msg-template='{abspath}:{line:5d}:{column}: {msg_id}: {msg} ({symbol})'" --output-format=colorized "${BASE}" --rcfile="${RC_FILE}"
cd ..
