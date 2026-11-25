# One Day of World News — Wednesday 25 November 2026

[![news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/tuyullsxx1-cmd/news-image-20261125-v1/rank.svg)](https://make.fun/bounty/news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/tuyullsxx1-cmd/news-image-20261125-v1/reward.svg)](https://make.fun/bounty/news-image-20261125)

A single front page that sums up Wednesday 25 November 2026: 33 verified
stories from 6 regions, drawn as a flat-vector newspaper in the style of
the 22 November final winner. The three biggest stories lead — Shenzhou-24
lifting off with Pakistan's first astronaut, a Houthi drone hitting the
Riyadh PIF Tower as Houthi forces close to within 60 km of Aden, and a
Brooklyn jury finding Huawei guilty on 10 of 12 counts — followed by ten
secondary cards, a day-in-UTC timeline on a dark navy band, the day in
six big red numbers, a dotted world map with numbered pins, a twenty-story
"also on Wednesday" list, a six-panel "day in pictures" strip, and a red
DATE CHECK box naming the stories left out because they happened on
another day (the COP31 collapse, the Merkury sinking, Nvidia's +31.5%
Monday surge, the Nepal quake, three Russian missiles landing in Poland).
Every story carries a certainty tag (CONFIRMED, REPORTED or CLAIM), so
nothing is shown as fact that was only claimed.

## How the program works

`main.py` (Python 3.13 standard library only) copies the pre-rendered
`entry.png` (1024×1024, 225,821 bytes) to `/output/entry.png` (or
`$MAKEFUN_OUTPUT_DIR/entry.png`), after checking the PNG magic bytes,
the 1 MiB size cap and the 1024×1024 dimensions. The image was rendered
deterministically offline with Pillow; the program itself needs no
network, no third-party libraries and no fonts, and produces
byte-identical output on every run.
