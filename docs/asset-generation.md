# Asset generation stage

## Command
```bash
python -m pip install -r requirements.txt
python scripts/generate_assets.py content/drafts/<draft-record>.json
```

## Output contract
Assets are written to `content/assets/<content-id>/`, with an `asset-manifest.json`.

| Format | Generated files | Completion note |
|---|---|---|
| carousel | ordered `slide-XX.png` files | At least 2 slide entries required |
| story | `story-XX.png` frames | At least 1 frame required; add native poll stickers in Instagram |
| founder_post | `cover.png` and outline text | Human review required |
| reel | `cover.png` and `reel-script.txt` | **Incomplete** until a rendered MP4 is supplied and checked |

## Guardrails
- No network/API call is needed to render PNGs.
- Palette and companion mark are provisional placeholders; use approved brand assets when available.
- Generated assets are not automatically approved or published.
- Keep personal health information out of content and visuals.
- Do not mark a Reel ready based only on a script or cover.
