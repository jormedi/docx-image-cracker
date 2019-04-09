#!/bin/sh
source ./venv/bin/activate
python docx-image-extractor
python docx-image-extractor/ImageCombiner.py
tar -cf result.zip docx-image-extractor/images/out
