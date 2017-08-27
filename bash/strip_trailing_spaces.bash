#!/bin/bash
cd "$(dirname "$0")"
git grep -I --name-only -z -e '' | xargs -0 sed -i 's/[ \t]\+\(\r\?\)$/\1/'
