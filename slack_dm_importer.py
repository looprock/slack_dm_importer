#!/usr/bin/env python
"""Convert a slack history json output to strtings."""
import json
import sys
from slacker import Slacker
from time import sleep

slack = Slacker('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

if len(sys.argv) < 3:
    sys.exit("Usage: %s [export json file] [user]" % (sys.argv[0]))

username = "@%s" % sys.argv[2]

with open(sys.argv[1]) as data_file:
    x = json.load(data_file)

msgs = []
for i in x:
    y = "%s: %s" % (i['date'], i['text'])
    msg = y.encode('utf-8')
    msgs.append(msg)

print msgs

r = reversed(msgs)

print r

for i in r:
    print i
    slack.chat.post_message(username, i, as_user=True)
    sleep(2)
