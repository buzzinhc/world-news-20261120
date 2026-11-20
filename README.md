# world-news-20261120

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/buzzinhc/world-news-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/buzzinhc/world-news-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

**THE WORLD TODAY** — a Python program that typesets the world news of
Friday, November 20, 2026 as a single 1024×1024 newspaper front page,
`entry.png`. Everything on the page — masthead, headlines, the round-table
summit illustration, the scales of justice, the market chart, the
smokestacks, the broken bridge and the Voyager probe — is drawn from
scratch with PIL primitives. No photographs, no external assets; the only
inputs are the day's facts and the DejaVu fonts.

## The front page

1. **THREE LEADERS, ONE TABLE** — Trump, Xi and Putin hold the first-ever
   trilateral summit on the sidelines of APEC in Shenzhen and issue a joint
   "peace declaration", pledging talks on reducing nuclear risks and more
   refined-fuel supplies; likened to a new Yalta, with no nuclear
   breakthrough.
2. **MYANMAR GUILTY OF GENOCIDE** — the International Court of Justice
   rules that Myanmar committed genocide against the Rohingya, a first in
   international law.
3. **ANTHROPIC'S RECORD DEBUT** — Anthropic becomes the first "pure-play"
   AI company to go public in a record-breaking listing.
4. **FOSSIL-FUEL WORDS VANISH FROM DRAFT** — uproar at the COP31 climate
   talks as the draft text drops the fossil-fuel phase-out.
5. **CRIMEA BRIDGE HIT AGAIN** — Ukraine strikes the bridge a third time
   in a week as European leaders say they are ready to talk with Russia.
6. **VOYAGER 1 CALLS HOME FROM ONE LIGHT-DAY AWAY** — NASA's farthest
   probe, launched 49 years ago, checks in from a full light-day out.

Stories are drawn from public reporting by the BBC, France 24, Le Monde,
the Associated Press and agency wires, cross-checked across sources on
the day.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Writes `out/entry.png` (1024×1024). Requires Python 3 and Pillow; the
drawing itself lives in `draw.py`, and `main.py` is the entry point that
honours `MAKEFUN_OUTPUT_DIR` (default `/output`).

<sub>Entered on [make.fun](https://make.fun/?ref=fjpy230d&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
