[app]

# Titre de l'application
title = ControleAid

# Nom du package
package.name = controleaid

# Domaine du package
package.domain = org.controleaid

# Dossier source
source.dir = .

# Extensions de fichiers à inclure
source.include_exts = py,png,jpg,kv,atlas,xlsx

# Version
version = 1.0

# Requirements - CORRECTION: versions compatibles ARM + ordre important
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow,openpyxl

# Orientation
orientation = portrait

# ---------------------------------------------
# Android
# ---------------------------------------------

fullscreen = 1

# Permissions
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# API cible
android.api = 33

# API minimum (Android 7.0+)
android.minapi = 24

# CORRECTION: NDK 25b est la version stable supportée par Buildozer
android.ndk = 25b

# Stockage privé
android.private_storage = True

# Architecture ARM 64-bit
android.archs = arm64-v8a

# Sauvegarde autorisée
android.allow_backup = True

# ---------------------------------------------
# Buildozer
# ---------------------------------------------

[buildozer]

log_level = 2
warn_on_root = 1
