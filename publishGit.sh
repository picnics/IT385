#!/bin/bash
#script publish changes to github

get pull
git add .
git commit -m "$*"
git push
