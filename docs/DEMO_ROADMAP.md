# Demo Upgrade Roadmap

Goal: turn sketchAI into a safe, hosted voice/text-to-sketch demo that does not require reviewers to configure secrets.

## Current State

- GitHub Pages surface is live.
- README.md now frames the project, architecture, and setup path.
- The repo includes speech, prompt processing, generation, and UI components.

## Highest-Impact Improvements

| Priority | Upgrade | Recruiter value |
| --- | --- | --- |
| P0 | Add a Hugging Face Spaces or Gradio demo with typed prompt input. | Makes the product testable. |
| P0 | Add fallback sample outputs so the demo works without paid/API access. | Prevents broken demos. |
| P1 | Add `examples/` with generated sketches and prompts. | Makes output quality visible. |
| P1 | Add `.env.example` documenting `HUGGINGFACE_API_TOKEN`. | Shows secret hygiene. |
| P2 | Add voice transcript mode after text prompt mode is stable. | Preserves the multimodal vision without demo fragility. |

## Suggested Demo Shape

- Gradio app with text prompt input first.
- Optional voice transcript input as a second tab.
- Output: generated image, cleaned prompt, model/provider notes.

## Definition Of Done

- Reviewer can generate or inspect at least three example sketches.
- No secrets are committed.
- README includes a screenshot and hosted demo link.
