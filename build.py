#!/usr/bin/env python3
"""Fetch the jam's public entries list from itch.io and build site/index.html."""
import datetime, json, pathlib, sys, urllib.request

JAM_ID = 419871          # Unity Game Jam 2026
HOME_GAME_ID = 5358375   # the game shown before anyone searches
URL = f"https://itch.io/jam/{JAM_ID}/entries.json"

root = pathlib.Path(__file__).parent
req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0 (jam-rating-counts)"})
with urllib.request.urlopen(req, timeout=60) as r:
    d = json.load(r)

games = d["jam_games"]
if len(games) < 100:
    sys.exit(f"only {len(games)} entries returned; not publishing")

rows = [[g["game"]["title"], g["game"]["user"]["name"], g["game"]["url"],
         g.get("rating_count", 0), g.get("coolness", 0), g["game"]["id"]] for g in games]
data = (json.dumps(rows, ensure_ascii=False, separators=(",", ":"))
        .replace("<", "\\u003c").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029"))
when = datetime.datetime.fromtimestamp(d["generated_on"], datetime.timezone.utc)
asof = f"{when.day} {when:%B %Y, %H:%M} UTC"

html = ((root / "template.html").read_text(encoding="utf-8")
        .replace("__ASOF__", asof).replace("__HOME__", str(HOME_GAME_ID)).replace("__DATA__", data))
out = root / "site"
out.mkdir(exist_ok=True)
(out / "index.html").write_text(html, encoding="utf-8")
print(f"{len(rows)} entries, as of {asof}")
