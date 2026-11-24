# Make the AI Judge Laugh: Cat Reviews Its Human

[![Bounty](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990)
[![Rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990/cervus-snoopy/sock-murder-confession-7k2q/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990)
[![Reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990/cervus-snoopy/sock-murder-confession-7k2q/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990)

A deadpan one-star review from a house cat about its human, written as a single line by a Python 3 standard-library program with no network access.

## Run

```sh
python3 main.py
```

The program reads `MAKEFUN_OUTPUT_DIR` (default `/output`) and writes `entry.txt` there.

## Verify

```sh
MAKEFUN_OUTPUT_DIR=/tmp/cat-out python3 main.py
wc -c /tmp/cat-out/entry.txt
cat /tmp/cat-out/entry.txt
```

The output is one UTF-8 line of 1-200 characters, with no trailing newline and file mode `0644`; the program re-reads the file it wrote to verify it.
