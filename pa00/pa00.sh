#!/usr/bin/env bash
# -*- coding: utf-8 -*-
# The first line is a shebang.
# The python3 part could be bash, zsh, ruby, whatever
# There are many ways to do a shebang, this is the best!

INPUT=`cat $1`
>$2
NUM=$(echo $INPUT | sed 's/[^0-9]*//g')
REPEAT=$(echo $INPUT | sed 's/[^a-z A-Z]*//g')

for (( i=1; i<=$NUM; i++ ))
do
    echo $REPEAT >> $2
done