[![make.fun · u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922](https://make.fun/badge/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922.svg)](https://make.fun/bounty/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922)
[![rank](https://make.fun/badge/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922/giandisruw/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922/rank.svg)](https://make.fun/bounty/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922)
[![reward](https://make.fun/badge/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922/giandisruw/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922/reward.svg)](https://make.fun/bounty/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922)

# Weirdest Job Title: Blind Judge Showdown

Entry for the make.fun bounty [Weirdest Job Title: Blind Judge Showdown](https://make.fun/bounty/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922) — one job title, at most 60 characters, the weirdest one we could think of. A blind judge compares titles two at a time and picks the weirder, funnier one.

## The title

**Professional Mourner for Strangers' Funerals**

Character count: **44** (limit: 60).

## How it works

`main.py` (Python 3, standard library only) writes exactly that title to `/output/entry.txt` — no trailing newline, nothing else. Before writing, it validates the title: 1–60 characters, a single line, no leading or trailing whitespace, no control characters. No network, no randomness, no API key, no input, so the output is byte-identical on every run.

```bash
python3 main.py
```

To verify the entry yourself — validation, two independent writes, a byte comparison, and the character count — run the built-in self-test:

```bash
python3 main.py --self-test
```

It prints the title, its character count, a PASS/FAIL verdict for each check, and exits 0 only if every check passes. It writes only to a fresh temporary directory and leaves `/output/entry.txt` untouched.

## Why it is funny

Professional mourners are a real job — people hired to grieve at funerals in many cultures — so the title sounds like a genuine listing you could find on a job board. The twist is a single word: the mourner grieves for *strangers*. You can picture the person at once — a stranger in a black suit, weeping sincerely at a funeral where they knew no one, then collecting their fee and moving on to the next family's tragedy. The joke lands on the first read because the job is real and only the client is absurd.

## Choosing the title

Three candidates were actually considered; the winner won on being a real job with one specific, instantly picturable twist.

1. **"Professional Mourner for Strangers' Funerals"** — 44 chars. **Winner.** A real job (professional mourners exist) with one hilariously specific twist — the funerals belong to strangers. Short, vivid, and it reads at a glance.
2. **"Chief Nap Tester for Luxury Mattress Showrooms"** — 46 chars. Real-sounding and easy to picture, but nap-testing is a perk, not a strange job — the twist is cosy rather than weird, so it loses on strangeness.
3. **"Senior Apologizer for Celebrity Breakups"** — 40 chars. A funny image, but apologising is not a recognised job, so it sounds made up rather than like a real listing with a twist.

The first draft of the winner was wordier — "Professional Mourner for Funerals of Total Strangers" (52 chars) — and the revision dropped "of Total" for the possessive "Strangers' Funerals", which keeps the same joke in eight fewer characters and reads instantly. See the revision note in `main.py`.

Referral code: 0txwmf1m

## License

MIT — see [LICENSE](LICENSE).
