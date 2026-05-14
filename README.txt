# sketchAI

AI sketch-generation assistant combining speech capture, text processing, Hugging Face image generation, and UI display.

## What It Does

- Captures speech and converts it into text.
- Processes prompts for image/sketch generation.
- Generates sketch-style image outputs.
- Displays generated results through a lightweight UI flow.

## Tech

Python, Hugging Face, speech-to-text, image generation, prompt processing.

## Repository Map

- `speech_capture.py`, `speech_to_text.py` - voice input pipeline.
- `text_processing.py`, `text_analysis.py` - prompt preparation.
- `generate_sketch.py`, `generate_face_sketch.py`, `image_generator.py` - generation logic.
- `ui_display.py`, `main.py` - app flow.

## Setup Note

Set `HUGGINGFACE_API_TOKEN` in your environment before using Hugging Face features. Do not commit API keys or tokens.

## Status

Prototype AI assistant.
