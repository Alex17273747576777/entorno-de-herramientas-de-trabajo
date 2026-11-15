# The Footprint or the Silence — twenty programs born in the last four months: eight that sign, twelve that ask for faith

*Rewritten from zero on Saturday, November 14, 2026. Same measurement day, same twenty repositories as the es-dominicano piece 01; different language, different prose, one shared truth: numbers were pulled live from the GitHub API while this text was being written.*

*La Bandita · Saturday, November 14, 2026 · en-ingles edition · master piece 01 · one text, four platforms (Reddit, X, Discord and Telegram)*

⏱️ *Reading time: about twenty minutes · twenty repositories created between August 1 and October 21, 2026, measured today one by one against the public GitHub API · 466,859 stars among them · eight publish a footprint · twelve do not · zero files hosted here*

*🗺️ Map of this piece*

- What "footprint" means: checksums and signatures next to the binaries
- The uncomfortable finding: stars do not buy footprints (the 281k repo ships no release at all)
- The eight that sign, one by one, with their counts
- The twelve that ask for faith, named without sermon
- The unexpected champion: the youngest repo in the lot signs best
- How every number here was measured, so you can rerun it
- What this piece does not have (and why that is fine)

## ⚡ One page

Twenty open-source programs born in the last four months. Eight ship a footprint with every release — checksums or signatures that let you verify the file you downloaded is the file they uploaded. Twelve do not: they ask for faith. Faith is a bad security model.

The uncomfortable part: footprints have nothing to do with fame. **deepseek-ai/deepseek-harness** holds 281,084 stars and publishes no release with assets at all: there is nothing to sign. At the other end, **xevrion/hatchzip**, 24 days old with 2,905 stars, ships 27 assets and 13 footprint files in its latest release: the best-signed repo in the entire lot. Between the extremes, one practical rule holds: six of the eight signers place sha256 or sha512 sums next to the binary, not buried in a commit.

And today's novelty against the November 9 package: the lot grew from 452,659 to 466,859 stars in five days (+14,200), while the footprint count did not move: still eight and twelve. Fame grows faster than the habit of signing.

## 📇 Cards, one per repository

### 1. xevrion/hatchzip
- Link: github.com/xevrion/hatchzip
- Stars: 2,905
- License: Apache-2.0
- Born: 2026-10-21 (24 days at cutoff)
- Last push: 2026-11-13
- Latest release: v0.1.10 (2026-11-10)
- Release assets: 27
- Footprint: yes — 13 checksum or signature files; best signer in the lot

### 2. Droid-Deck/DroidDeck
- Link: github.com/Droid-Deck/DroidDeck
- Stars: 20,130
- License: GPL-3.0
- Born: 2026-09-24 (51 days)
- Last push: 2026-11-14
- Latest release: 0.7.1 (2026-11-10)
- Release assets: 5
- Footprint: yes — 1 checksum file

### 3. Fei2411/DS-Bot
- Link: github.com/Fei2411/DS-Bot
- Stars: 7,759
- License: Apache-2.0
- Born: 2026-10-07 (38 days)
- Last push: 2026-11-14
- Latest release: v0.3.6 (2026-11-12)
- Release assets: 20
- Footprint: yes — 1 checksum file

### 4. KnifeLemon/Filee
- Link: github.com/KnifeLemon/Filee
- Stars: 27,174
- License: MIT
- Born: 2026-09-29 (46 days)
- Last push: 2026-11-14
- Latest release: v2.4.1 (2026-11-14, cutoff day)
- Release assets: 18
- Footprint: yes — 10 checksum files

### 5. anmolkapil/plexo
- Link: github.com/anmolkapil/plexo
- Stars: 5,724
- License: MIT
- Born: 2026-09-15 (60 days)
- Last push: 2026-11-14
- Latest release: v1.0.0-rc.15 (2026-10-11)
- Release assets: 20
- Footprint: no — twenty assets, zero sums

### 6. deepseek-ai/deepseek-harness
- Link: github.com/deepseek-ai/deepseek-harness
- Stars: 281,084
- License: MIT
- Born: 2026-08-13 (93 days)
- Last push: 2026-11-13
- Latest release: none published
- Release assets: 0
- Footprint: no — no release to sign

### 7. firecrawl/anydoc
- Link: github.com/firecrawl/anydoc
- Stars: 23,544
- License: MIT
- Born: 2026-08-03 (103 days)
- Last push: 2026-11-13
- Latest release: v0.2.4 (2026-08-27, almost three months old)
- Release assets: 15
- Footprint: no

### 8. gauthierpiarrette/highball
- Link: github.com/gauthierpiarrette/highball
- Stars: 2,257
- License: GPL-3.0
- Born: 2026-08-23 (83 days)
- Last push: 2026-11-14
- Latest release: v0.10.26 (2026-11-05)
- Release assets: 2
- Footprint: no

### 9. guillermolg00/morphicons
- Link: github.com/guillermolg00/morphicons
- Stars: 3,185
- License: MIT
- Born: 2026-08-01 (105 days, oldest in the lot)
- Last push: 2026-11-14
- Latest release: v2.0.2 (2026-10-24)
- Release assets: 0
- Footprint: no — source-only releases

### 10. kota-zo/myspoti
- Link: github.com/kota-zo/myspoti
- Stars: 2,121
- License: GPL-3.0
- Born: 2026-10-14 (31 days)
- Last push: 2026-11-12
- Latest release: v2.4.1 (2026-11-12)
- Release assets: 4
- Footprint: no

### 11. ly05010419/MacNativeGames
- Link: github.com/ly05010419/MacNativeGames
- Stars: 7,814
- License: MIT
- Born: 2026-10-17 (28 days)
- Last push: 2026-11-14
- Latest release: v2026.10.25 (2026-10-25)
- Release assets: 0
- Footprint: no

### 12. miqdadbadjuber/anti-slop
- Link: github.com/miqdadbadjuber/anti-slop
- Stars: 9,223
- License: MIT
- Born: 2026-08-07 (99 days)
- Last push: 2026-11-13
- Latest release: v3.2.30 (2026-11-13)
- Release assets: 0
- Footprint: no — code-only release

### 13. net-merge/net-merge
- Link: github.com/net-merge/net-merge
- Stars: 3,123
- License: MIT
- Born: 2026-10-12 (33 days)
- Last push: 2026-11-09
- Latest release: v0.3.7 (2026-11-09)
- Release assets: 59 — most assets in the lot
- Footprint: no — 59 assets and not one sum: volume is not care

### 14. omlahore/RemoveMacAI
- Link: github.com/omlahore/RemoveMacAI
- Stars: 6,097
- License: MIT
- Born: 2026-09-29 (46 days)
- Last push: 2026-11-14
- Latest release: v1.2.0 (2026-11-14, cutoff day)
- Release assets: 4
- Footprint: yes — 2 checksum files

### 15. robbietilton/Compositor
- Link: github.com/robbietilton/Compositor
- Stars: 18,666
- License: MIT
- Born: 2026-09-16 (59 days)
- Last push: 2026-11-08
- Latest release: v1.6.6 (2026-11-08)
- Release assets: 1
- Footprint: no

### 16. seedds/nxnative
- Link: github.com/seedds/nxnative
- Stars: 15,501
- License: MIT
- Born: 2026-10-13 (32 days)
- Last push: 2026-11-14
- Latest release: none published
- Release assets: 0
- Footprint: no

### 17. shaongitbd/doory
- Link: github.com/shaongitbd/doory
- Stars: 2,731
- License: not identified by GitHub (NOASSERTION): read its LICENSE before using it in someone else's project
- Born: 2026-10-10 (35 days)
- Last push: 2026-11-14
- Latest release: v0.3.1 (2026-11-09)
- Release assets: 0
- Footprint: no

### 18. sonorahq/sonora
- Link: github.com/sonorahq/sonora
- Stars: 2,817
- License: GPL-3.0
- Born: 2026-08-03 (103 days)
- Last push: 2026-11-14
- Latest release: v0.49.1 (2026-11-13)
- Release assets: 15
- Footprint: yes — 1 checksum file

### 19. tangency-labs/solidcraft
- Link: github.com/tangency-labs/solidcraft
- Stars: 16,315
- License: Apache-2.0
- Born: 2026-10-07 (38 days)
- Last push: 2026-11-14
- Latest release: v0.42.0 (2026-11-14, cutoff day)
- Release assets: 49
- Footprint: yes — 1 checksum file

### 20. zai-org/ZCode
- Link: github.com/zai-org/ZCode
- Stars: 8,689
- License: Apache-2.0
- Born: 2026-09-20 (55 days)
- Last push: 2026-11-13
- Latest release: v3.17.2 (2026-11-04)
- Release assets: 7
- Footprint: yes — 1 checksum file

## ❓ Questions this piece answers

- How many of the twenty publish a footprint with their releases? Eight.
- Which one signs best? hatchzip: 13 footprint files across 27 assets.
- Does the most-starred repo sign? No: deepseek-harness (281,084 ★) ships no release.
- Do many assets imply care? No: net-merge ships 59 assets and zero sums.
- How many released on cutoff day itself? Three: Filee, RemoveMacAI, solidcraft.
- Any repo with no identifiable license? One: doory (NOASSERTION).
- What is new against the November 9 package? +14,200 stars in five days; footprint unchanged: 8 and 12.

## 📊 Table of the twenty

| repository | ★ | license | latest release | assets | footprint |
|---|--:|---|---|--:|---|
| xevrion/hatchzip | 2,905 | Apache-2.0 | v0.1.10 | 27 | yes (13) |
| Droid-Deck/DroidDeck | 20,130 | GPL-3.0 | 0.7.1 | 5 | yes (1) |
| Fei2411/DS-Bot | 7,759 | Apache-2.0 | v0.3.6 | 20 | yes (1) |
| KnifeLemon/Filee | 27,174 | MIT | v2.4.1 | 18 | yes (10) |
| anmolkapil/plexo | 5,724 | MIT | v1.0.0-rc.15 | 20 | no |
| deepseek-ai/deepseek-harness | 281,084 | MIT | none | 0 | no |
| firecrawl/anydoc | 23,544 | MIT | v0.2.4 | 15 | no |
| gauthierpiarrette/highball | 2,257 | GPL-3.0 | v0.10.26 | 2 | no |
| guillermolg00/morphicons | 3,185 | MIT | v2.0.2 | 0 | no |
| kota-zo/myspoti | 2,121 | GPL-3.0 | v2.4.1 | 4 | no |
| ly05010419/MacNativeGames | 7,814 | MIT | v2026.10.25 | 0 | no |
| miqdadbadjuber/anti-slop | 9,223 | MIT | v3.2.30 | 0 | no |
| net-merge/net-merge | 3,123 | MIT | v0.3.7 | 59 | no |
| omlahore/RemoveMacAI | 6,097 | MIT | v1.2.0 | 4 | yes (2) |
| robbietilton/Compositor | 18,666 | MIT | v1.6.6 | 1 | no |
| seedds/nxnative | 15,501 | MIT | none | 0 | no |
| shaongitbd/doory | 2,731 | NOASSERTION | v0.3.1 | 0 | no |
| sonorahq/sonora | 2,817 | GPL-3.0 | v0.49.1 | 15 | yes (1) |
| tangency-labs/solidcraft | 16,315 | Apache-2.0 | v0.42.0 | 49 | yes (1) |
| zai-org/ZCode | 8,689 | Apache-2.0 | v3.17.2 | 7 | yes (1) |

## 📖 Glossary

- **Footprint:** checksum files (sha256, sha512) or signatures (.asc, .sig) published next to release assets.
- **Asset:** binary or package uploaded to a GitHub release, separate from source code.
- **Release:** a versioned, dated delivery; without it, users download "whatever is there today".
- **Push:** last change received by the repository; it tells you whether the project breathes.
- **SPDX license:** standard license identifier; NOASSERTION means GitHub could not identify one.
- **Star:** another user's interest marker; not a download, not usage, not trust.
- **GitHub public API:** the query interface behind every number here; basic endpoints need no key, we used our own token to avoid rate limits.
- **Band:** allowed body length for a piece per docs/bandas.json (6,000-45,000 characters).

## 🔗 Links

- github.com/xevrion/hatchzip/releases — the best-signed release in the lot
- github.com/deepseek-ai/deepseek-harness — 281k stars, zero releases
- api.github.com/repos/{owner}/{repo} — the exact query behind every figure
- docs/bandas.json inside this repository — the band this piece respects

## 🎭 Meme of the piece

*Suggested image: a notary holding a stamp in front of two identical boxes; one wears a label reading "sha256: …", the other a sticky note reading "trust me, bro".* Caption: "Eight sign. Twelve ask for faith. Faith is not an algorithm."

## ⏱️ How and when this was measured

Saturday 2026-11-14, between 23:25 and 23:26 Santo Domingo time (UTC-4), against the public GitHub API: `GET /repos/{owner}/{repo}` for stars, license, creation and last push; `GET /repos/{owner}/{repo}/releases/latest` for release, assets and footprint (names containing .sha256, .sha512, sha256sums, checksums, .asc, .sig or .md5). No cache, no memory, no copy of the previous piece: today's measurement is the source. The star total (466,859) and the counts (8/12) come from those twenty records, not from rounding.

## 📜 License of this piece

CC BY-SA 4.0: copy, remix and share citing La Bandita and sharing alike. The twenty repositories keep their own licenses, listed in their cards.

## ✍️ Signature and closing

— La Bandita · en-ingles bandita · master piece 01, rewritten 2026-11-14.
*Closing line: if a program does not sign what it ships, it is not selling you software — it is asking you for an act of faith with a password.*

*💓 La Bandita informa. Lo que no se midió, aquí no se escribe.*

## 🗓️ Dated notes

- 2026-11-14: piece rewritten from zero under the language-based structure (en-ingles) with per-platform derivations (Reddit, X, Discord, Telegram); fresh measurement of the whole lot; deltas against Nov 9 noted in "One page".
- 2026-11-09: previous package (Facebook-dominicano-ES); remains history in `_ARCHIVO-HISTORICO/_reemplazadas/` once the owner approves the archive.
