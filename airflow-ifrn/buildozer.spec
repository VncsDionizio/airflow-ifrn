[app]
title = AirFlow IFRN
package.name = airflowifrn
package.domain = ifrn.edu.br

source.dir = .
source.include_exts = py, png, jpg, kv, atlas, ttf, otf

version = 1.0
requirements = python3, kivy, openssl

[buildozer]
log_level = 2

[android]
api = 33
minapi = 21
android.permissions = INTERNET
