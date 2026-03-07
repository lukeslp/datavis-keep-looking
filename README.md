# Keep Looking

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Live Site](https://img.shields.io/badge/live-dr.eamer.dev-brightgreen)](https://dr.eamer.dev/datavis/poems/keep-looking/)

147,570 UFO sightings from the National UFO Reporting Center (NUFORC), plotted on a radar screen. The sweep rotates continuously, illuminating reports and then letting them fade — the same way a real radar trace decays.

## What it does

Each dot on the radar is a sighting from the NUFORC database, 1905–2023. Distance from the center encodes year — inner rings are older, outer rings are more recent. The rotating sweep line hits each point and briefly lights it up. Hover to see the date, location, shape, size, and reported speed.

The encoding is literal: the visualization works like a radar because the subject matter is the kind of thing you'd see on a radar.

- **Shape** is encoded as a glyph at high zoom (light, disk, triangle, fireball, sphere, circle, other)
- **Speed** affects animation behavior — instant sightings jitter chaotically, slow ones drift, long-duration ones orbit slightly
- **Size** controls dot radius (small/medium/large)
- Zoom in up to 10x to pick apart dense clusters; drag to pan

## Controls

| Input | Action |
|-------|--------|
| Mouse move | Highlight nearest sighting |
| Scroll wheel | Zoom in/out (0.8x–10x) |
| Click + drag | Pan |
| Pinch | Zoom (mobile) |
| Touch + drag | Pan (mobile) |
| Tap | Toggle UI lock |

## Stack

- D3.js v7 for data loading and layout math
- Canvas API for the radar rendering loop
- Inter + JetBrains Mono for the monospace readout aesthetic
- No frameworks, no build step

## Files

```
keep-looking/
├── index.html                  # Full radar visualization
├── data/
│   └── watchers_data.json      # 147,570 NUFORC sightings
├── process_watchers_data.py    # Data cleaning pipeline
└── card.png                    # 1200x630 Open Graph image
```

## Data

Source: [National UFO Reporting Center (NUFORC)](https://nuforc.org/)

The dataset spans 1905–2023 and includes date, time, location, shape, duration, and witness descriptions. `process_watchers_data.py` cleans and converts the raw NUFORC export to the JSON format the visualization expects.

## Running locally

```bash
python3 -m http.server 8000
# open http://localhost:8000
```

## Author

Luke Steuber — [lukesteuber.com](https://lukesteuber.com) — [@lukesteuber.com](https://bsky.app/profile/lukesteuber.com) on Bluesky

Part of the [data poems collection](https://dr.eamer.dev/datavis/poems/) at dr.eamer.dev.

## License

MIT
