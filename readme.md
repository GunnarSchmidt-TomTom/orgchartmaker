# What is it?
This is a tool to create an org-chart from a ;-delimited CSV table like Worday will export. The expected input format is
'''
Unique Identifier;Name;Reports To;Line Detail 1;Line Detail 2;Organization Name
'''

It requires python3, pydot and treelib
It can output either an ascii-tree representation of the org-chart (option --ascii) or renders into an image (out.png), using graphviz.

Call
'''
python3 orgchart.py --help
'''
for all options and help.