#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import json
import logging

SCRIPT_PATH = os.path.dirname(__file__)
results = []

logging.basicConfig(level = logging.DEBUG)

for parent, dirnames, filenames in os.walk(os.path.join(SCRIPT_PATH, 'code')):
    logging.debug('parent = %s, dirnames = %s, filenames = %s' % (parent, dirnames, filenames))
    for filename in filenames:
        file_ext = os.path.splitext(filename)
        if file_ext[1] in {'.html', '.htm'}:
            file_path = os.path.join(parent, filename)
            logging.info('file_path = %s' % (file_path))
            results.append({
                    'file_path': file_path
                })

with open('demo_files.json', 'w') as f:
    f.write(json.dumps(results, indent = 2))
