# Creation Unit (Topic 10)

Source material and planning for the "Doctrine of Creation vs Evolutionism" slide decks. The deck plan is in [Creation.Slides.Structure.md](Creation.Slides.Structure.md).

## Folders

| Folder | Contents |
|--------|----------|
| `Craig/` | William Lane Craig, Defenders Series 4 transcripts (converted from the reasonablefaith.org PDFs): `Craig.Creation.01-24` (creatio ex nihilo, conservation, providence, miracles, angels and demons), `Craig.Excursus.01-30` (Genesis 1–11 interpretations, mytho-history, origin of life, evolution), `Craig.Man.12-19` (historical Adam) |
| `Sources/` | External articles – YEC and ID (CMI, AiG, ICR, Discovery Institute, STR) plus opposing views (RTB, BioLogos), in `Genesis/`, `Physics/`, `Chemistry/`, `Biology/`. See [Sources/README.md](Sources/README.md) |
| `Notes/Series2/` | Ingmar's notes and outlines from teaching Craig's Defenders Series 2 (docx → md, with `media/`) |
| `Notes/GodScience/` | Ingmar's "God vs/via Science" course (`Course.00-12`), the 2004 "God and Science" lessons (`Lesson.1-9`), and single-topic decks (`Topic.*`) |
| `Notes/CreationSuperConference/` | Talks from the 2011 and 2017 Creation Super Conferences |
| `Notes/Ingmar/` | Ingmar's own write-ups (Hugh Ross review, Day-Age questions, Noah's Flood, Satan's origin, science and faith) |
| `Notes/Talks/` | Other speakers (Calvin Smith, David Garcia) |
| `Notes/Pptx/` | Decks from `C:/_/me/bible/PPTX` |

The originals of all converted notes remain in `C:/_/me/bible/Defenders`, `C:/_/me/bible/GodScience`, `C:/_/me/bible/PPTX`, and `C:/_/me/bible/Creation Super Conference`.

## Genesis Interpretations Chart

`docs/Creation/pics/GenesisInterpretations.svg` is generated – do not edit it by hand. Edit and run the generator:

```
python tools/genesis-interpretations-chart.py
```

- The script lays the chart out on a grid: one font size, one box line width, parallel box lines a fixed distance apart, and a fixed gap between text and box lines.
- Each box uses one main HuBiSa hue at standard saturation (`ColorHuBiSa.cs`, `RgbGridInit()`): day = 24h Green, day ≠ 24h Red, Accurate Science Blue, Obsolete Science Cyan, Young Earth Yellow, Old Earth Orange, Literal Magenta, Figurative Purple; text Gray.
- Footnote markers are full-size superscripts: `*` compatible with evolution and old age fossils, `+` old age fossils only, `†` no death before the fall, `‡` historical Adam not affirmed, `?` day length left open.
- The script writes a text version to the temp folder, then Inkscape (`--export-text-to-path`) outlines the text into the published SVG, so it looks the same in every browser without the Calibri font installed.
