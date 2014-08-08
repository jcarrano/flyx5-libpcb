#  csvmerge.py
#
#  Copyright 2014 Juan I Carrano <juan@carrano.com.ar>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
"""
CSVMerge
========

This program attempts to resolve a merge conflict between csv files
"""

import csv
from collections import Counter

MARKERS = {'LOCAL_MARK': "<<<<<<< local",
            'MID_MARK':"=======",
            'OTHER_MARK': ">>>>>>> other"
            }

def ismarker(row):
    try:
        return row[0] in MARKERS.values()
    except IndexError:
        return False

def main():
    import sys

    try:
        fn = sys.argv[1]
    except IndexError:
        raise RuntimeError("You must supply a filename")

    with open(fn) as f:
        reader = csv.reader(f)
        rows = (tuple(row) for row in reader if not ismarker(row))
        header = next(rows)
        srows = set(rows)
        srows.discard(header)
    # now the file is closed

    names = (r[0] for r in srows if len(r) > 0)
    print("\n".join("Item: %s repeated %d times"%i for i
                                        in Counter(names).items() if i[1]>1))

    with open(fn+".merged", "w") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(sorted(srows))

    return 0

if __name__ == '__main__':
    main()
