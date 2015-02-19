# -*- coding: utf-8 -*-
def results(fields, original_query):
    addr = ""
    taddr = ""
    if len(fields):
        addr = fields["~addr"]
        taddr = "do "+addr
    return {
        "title": "Napisz wiadomość {0}".format(taddr),
        "run_args": [addr]
    }

def run(addr):
    import os
    os.system('open mailto:"{0}"'.format(addr))
