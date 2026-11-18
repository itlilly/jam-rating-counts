# Jam Rating Counts

How many ratings each entry in the Unity Game Jam 2026 has received: mean, median, mode, a distribution chart, and a search to look up any game.

Site: https://itlilly.github.io/jam-rating-counts/

Star scores are hidden by itch.io until voting ends, so this only counts ratings. The numbers come from the jam's public entries list (`https://itch.io/jam/419871/entries.json`) and are rebuilt about once an hour by a GitHub Action.

Unofficial; not affiliated with Unity or itch.io.

## Build it yourself
`python3 build.py` fetches the list and writes `site/index.html`.
