#!/usr/bin/env python

import os
import shutil
import sys

theme_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

node_modules_path = os.path.join(theme_path, 'node_modules')
static_path = os.path.join(theme_path, 'static')
static_js_path = os.path.join(static_path, 'js')
static_css_path = os.path.join(static_path, 'css')

if not os.path.isdir(node_modules_path):
    print("The node_modules directory isn't there you need to run npm first.")
    sys.exit(1)

# Copy jQuery
jquery_files = ['jquery.js', 'jquery.min.js', 'jquery.min.map']
jquery_path = os.path.join(node_modules_path, 'jquery', 'dist')

for f in jquery_files:
    src = os.path.join(jquery_path, f)
    dest = os.path.join(static_js_path, f)
    shutil.copy(src, dest)

# Material Design Lite
mdl_js_files = ['material.js', 'material.min.js', 'material.min.js.map']
mdl_js_path = os.path.join(node_modules_path, 'material-design-lite', 'dist')
for f in mdl_js_files:
    src = os.path.join(mdl_js_path, f)
    dest = os.path.join(static_js_path, f)
    shutil.copy(src, dest)

mdl_css_files = [
    'material-grid.css',
    'material-grid.min.css',
    'material.css',
    'material.min.css',
    'material.min.css.map'
]
mdl_css_path = os.path.join(node_modules_path, 'material-design-lite', 'dist')
for f in mdl_css_files:
    src = os.path.join(mdl_css_path, f)
    dest = os.path.join(static_css_path, f)
    shutil.copy(src, dest)
