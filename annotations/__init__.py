"""Editorial annotations for Magnifica Humanitas, one module per language.

Each ``<lang>.py`` exposes ``ANNOTATIONS``: a list of
``{"p", "after", "occurrence", "note"}`` entries. ``build.load_annotations(lang)``
imports the matching module (``annotations.en``, ``annotations.it``, …).
"""
