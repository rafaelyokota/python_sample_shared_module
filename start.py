# from base.foo.bar import foo 
# print("Start")
# b = foo()




#!/usr/bin/env python3

import sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-p', '--process', type=str, required=True)
args = parser.parse_args()

processName = args.process

if processName == "foo":
    from projects.project1.start import foo
elif processName == "bar":
    from projects.project2.start import foo2
    
else:
    print("invalida process", flush=True)
    sys.exit(1)
    