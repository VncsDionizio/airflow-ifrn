[app]
title = AirFlow IFRN
package.name = airflowifrn
package.domain = org.ifrn

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,otf

version = 1.0
requirements = python3,kivy,openssl

[buildozer]
log_level = 2

[android]
api = 33
minapi = 21
android.permissions = INTERNET

# ========== CONFIGURAÇÕES ANDROID ==========
[android]
# ✅ ACEITA LICENÇAS AUTOMATICAMENTE
android.accept_sdk_license = True

# ✅ USA VERSÕES COMPATIVEIS
android.sdk = 26
android.ndk = 25b
android.api = 33
android.minapi = 21

# ✅ ARQUITETURA
android.arch = arm64-v8a

# ✅ PERMISSÕES
android.permissions = INTERNET
