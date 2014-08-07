#!/bin/sh
rm -f compiled/*.zip
FILENAME="flxlib-$(hg id -in | sed 'y/ /:/').zip"
7z a "compiled/${FILENAME}" ./compiled/*/*.IntLib
