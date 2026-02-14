# KEEP LOOKING

147,570 UFO sightings from NUFORC as a rotating radar. The sweep reveals clusters and patterns across North America, 1905-2023.

## Features

- **147,570 sightings**: Complete NUFORC database
- **Radar sweep animation**: Rotating scan reveals sightings
- **Geographic clustering**: Hotspots near population centers
- **Timeline**: 118 years of sightings (1905-2023)
- **Interactive**: Hover for location and date details
- **Decay effect**: Older sightings fade as sweep passes

## Technical Stack

- **D3.js v7**: Geographic projections and data binding
- **Canvas API**: Hardware-accelerated radar effect
- **Vanilla JavaScript**: No frameworks
- **Inter + JetBrains Mono fonts**: Clean monospace aesthetic

## Files

- `index.html` - Complete radar visualization (22KB)
- `data/watchers_data.json` - NUFORC sightings database
- `process_watchers_data.py` - Data pipeline script (5KB)
- `card.png` - Open Graph image (231KB)

## Data Structure

```json
{
  "date": "2023-05-15",
  "latitude": 47.6062,
  "longitude": -122.3321,
  "city": "Seattle",
  "state": "WA",
  "shape": "Triangle",
  "duration": "5 minutes"
}
```

## Processing Pipeline

```bash
python3 process_watchers_data.py
# Converts raw NUFORC data to JSON format
# Geocodes locations to lat/lon coordinates
# Output: data/watchers_data.json
```

## Local Development

```bash
python3 -m http.server 8000
# Visit http://localhost:8000
```

## Data Source

National UFO Reporting Center (NUFORC)
https://nuforc.org/

Database spans 1905-2023 with detailed reports including date, location, shape, duration, and witness descriptions.

## Author

Luke Steuber
https://lukesteuber.com
