#!/usr/bin/bash

if [[ ! -d "docs" ]];then
    echo "docs not exists, clone project start ..."
    git clone https://github.com/LanSeTianYe/Notes.git docs
    echo "docs not exists, clone project end ..."
fi

echo "pull docs start ..."
cd docs && git pull
echo "pull docs end ..."
cd .. && mkdocs build




