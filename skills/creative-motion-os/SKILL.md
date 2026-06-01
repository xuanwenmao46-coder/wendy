---
name: creative-motion-os
description: Top-level Creative Motion Operating System (CMOS V5). The highest layer in the production stack. Transforms any brief into award-winning design cinema by establishing emotional foundation, creative risk posture, visual density requirements, and anti-AI detection rules BEFORE any design decision is made. Run BEFORE the Aesthetic Governor (Step 4.0). Includes two production tools: PremiumColorReducer (CIELAB-space Swiss/Morandi color enforcement) and AudioSync (millisecond-precise sound-to-animation alignment). Use when output must feel like Pentagram, COLLINS, ManvsMachine, or OFFF Festival — not generic AI video.
dependencies: [aesthetic-governor, flagship-video-director]
---

# Creative Motion Operating System V5

## Position in the Production Stack

CMOS V5 runs at **Step 0** — before the Aesthetic Governor, before any design school selection, before any font or color choice. It is the creative brief that all downstream systems must honor.

```
CMOS V5 (Step 0) ← YOU ARE HERE
↓
Aesthetic Governor (Step 4.0)
↓
aesthetic-layout-direction (Step 4.5)
↓
high-end-video-design → typography-selection → motion-graphic-design → sound-design-for-motion
↓
flagship-video-director (orchestration)
```

## What CMOS V5 Does

CMOS V5 replaces the default AI generation equation:

```
User Input × AI Generation = Output
```

With the Creative Motion OS equation:

```
User Input × Emotion × Creative Risk × Visual Density × CMOS Directors × AI Generation = Output
```

The difference between those two equations is the difference between a generic explainer video and an OFFF Festival opener.

## The CMOS Director Pipeline

Ten director roles run in sequence. Each produces a constraint that all downstream directors must honor.

```
Creative Director → establishes emotional premise and creative risk level
Art Director → translates emotion into visual world
Brand Designer → defines visual identity coherence rules
Typography Designer → makes type the architecture, not the label
Motion Designer → makes motion inevitable, not decorative
Sound Designer → makes sound drive visuals, not accompany them
Data Storytelling Designer → makes information feel alive
Cinematographer → makes every frame work as a held photograph first
Museum Curator → makes information unfold as discovery, not presentation
Anti-AI Detector → continuously rejects templated, generated, or safe output
```

## Full Specification

Read [CMOS-V5.md](CMOS-V5.md) for the complete creative brief, reference system, visual density engine, color narrative system, motion psychology, and final quality test.

## Production Tools

Two executable tools ship with this skill:

- **[tools/premium_color_reducer.py](tools/premium_color_reducer.py)** — Intercepts any AI-generated color and enforces it into a Swiss/Morandi premium palette using CIELAB Delta E distance. No scikit-image required.
- **[tools/audio_sync.py](tools/audio_sync.py)** — Detects audio peak frame and generates an FFmpeg command to align it with animation start time at millisecond precision. Requires only FFmpeg and numpy.

See [TOOL-GUIDE.md](TOOL-GUIDE.md) for usage.

## References

- Full creative spec: [CMOS-V5.md](CMOS-V5.md)
- Tool usage: [TOOL-GUIDE.md](TOOL-GUIDE.md)
- Next layer: [`aesthetic-governor/SKILL.md`](../aesthetic-governor/SKILL.md)
- Production orchestration: [`flagship-video-director/SKILL.md`](../flagship-video-director/SKILL.md)
