#!/bin/bash

cd ~/monkeystypingfuriously
python main.py
git checkout gh-pages
git checkout master -- _sentences
git add _sentences
git commit -m "Adding '_sentences' directory from 'master' branch."
git push
git checkout master
