#!/usr/bin/env python3
import fileinput
import re

# TODO: write a real tokenizer
# https://docs.python.org/3/library/re.html#writing-a-tokenizer

codemode = False
breakmode = False
nosyntaxmode = False

module_keywords = [r'\b(eqtype)\b',
                   r'\b(functor)\b',
                   r'\b(include)\b',
                   r'\b(sharing)\b',
                   r'\b(sig)\b',
                   r'\b(signature)\b',
                   r'\b(struct)\b',
                   r'\b(structure)\b',
                   r'\b(where)\b']

keywords = [r'\b(abstype)\b',
            r'\b(andalso)\b',
            r'\b(as)\b',
            r'\b(case)\b',
            r'\b(datatype)\b',
            r'\b(do)\b',
            r'\b(else)\b',
            r'\b(end)\b',
            r'\b(exception)\b',
            r'\b(fn)\b',
            r'\b(fun)\b',
            r'\b(handle)\b',
            r'\b(if)\b',
            r'\b(in)\b',
            r'\b(infix)\b',
            r'\b(infixr)\b',
            r'\b(let)\b',
            r'\b(local)\b',
            r'\b(nonfix)\b',
            r'\b(not)\b',
            r'\b(of)\b',
            r'\b(op)\b',
            r'\b(open)\b',
            r'\b(orelse)\b',
            r'\b(raise)\b',
            r'\b(rec)\b',
            r'\b(then)\b',
            r'\b(type)\b',
            r'\b(val)\b',
            r'\b(with)\b',
            r'\b(withtype)\b',
            r'\b(while)\b']

sml_types = [r'\b(bool)\b',
             r'\b(char)\b',
             r'\b(int)\b',
             r'\b(real)\b',
             r'\b(string)\b',
             r'\b(unit)\b']
             
sml_constants = [r'\b(false)\b',
                 r'\b(true)\b']

pretty_print_rule = [(r'\b(o)\b', r'$\circ$')]

comment_start = re.compile("(\(\*)")
comment_end = re.compile("(\*\))")

def make_comment(line):
    line = re.sub(comment_start, r"\\SMLcomment{\1", line)
    line = re.sub(comment_end, r"\1}", line)
    return line

for line in fileinput.input():
    line = line[:-1] # remove \n

    if "nwendcode" in line:
        codemode = False

    if codemode:
        line = make_comment(line)
        for kw in keywords:
            line = re.sub(kw, r"\\SMLkwd{\1}", line)
        for mkw in module_keywords:
            line = re.sub(mkw, r"\\SMLkwd{\1}", line)
        for tp in sml_types:
            line = re.sub(tp, r"\\SMLtype{\1}", line)
        for c in sml_constants:
            line = re.sub(c, r"\\SMLconst{\1}", line)
        

    if "nwenddeflinemarkup" in line:
        codemode = True

    print(line)