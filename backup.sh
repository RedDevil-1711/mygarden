#!/bin/bash
cd ~/mygarden_project
git add .
git commit -m "Automatic backup on $(date)"
git push
