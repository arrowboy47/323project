# Browser × Search Engine Response-Time Experiment

Group final project for STAT 323 (design of experiments). A 3×3 factorial experiment measuring how fast a search query returns across **browsers** (Firefox, Chrome, Edge) and **search engines** (Google, Bing, DuckDuckGo), with treatment order randomized in R and timing automated with Selenium.

## How it works

1. **Randomization** (`randomassignment.R`) — builds the full 3×3 treatment grid, 4 replications each, shuffles run order, writes `data/order.csv`.
2. **Data collection** (`datacollection.py`) — reads the randomized run order, launches each browser via Selenium WebDriver, submits the query "statistics" to the assigned engine, and records wall-clock search time to `data/search_times.csv`. `test.py` is the interactive single-trial version used while developing the harness.
3. **Analysis** — two-factor ANOVA on the collected times (write-up in `docs/`).

## Repo layout

```
randomassignment.R    # treatment randomization → data/order.csv
datacollection.py     # automated Selenium timing runs
test.py               # manual single-trial harness
data/                 # run order + collected response times
docs/                 # design protocol + report template
project.Rproj         # RStudio project
```

## Running

```bash
pip install selenium   # plus browser drivers (geckodriver/chromedriver/edgedriver) on PATH
Rscript randomassignment.R
python3 datacollection.py
```
