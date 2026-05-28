# RAG Metadata

Use this schema for clips worth saving as reusable seeds.

## Required Fields

```json
{
  "id": "flagship_data_shock_001",
  "asset_type": "flagship_clip",
  "quality_tier": "hero",
  "title": "Data Shock",
  "description": "A big metric impacts the frame and drives a chart reveal.",
  "scenario": "data_shock",
  "scene_job": ["hook", "data_story"],
  "content_type": ["data", "text", "chart"],
  "motion_patterns": ["data_hit", "badge_snap", "chart_tear"],
  "visual_register": ["broadcast", "data_terminal"],
  "aspect_ratio": "16:9",
  "canvas_size": "1280x720",
  "responsive": {
    "mode": "single-ratio",
    "supported_ratios": ["16:9"],
    "layout_rules": ["title left anchored", "metric centered", "chart scales to parent"],
    "breakpoints": [],
    "safe_areas": ["title", "final_lockup"]
  },
  "tempo": "explosive",
  "energy_level": 5,
  "text_split": "block",
  "editable_params": ["headline", "metric", "delta", "accent_color", "duration", "aspect_ratio", "image_source"],
  "input_requirements": {
    "supports_chinese": true,
    "requires_data": true,
    "requires_image": false
  },
  "quality_score": {
    "impact": 5,
    "motion": 4,
    "focus": 5,
    "style": 4,
    "reusability": 5,
    "memorability": 5
  },
  "anti_tags": ["luxury_slow", "dense_paragraph"],
  "source_path": "clips-lab/flagship-motion-clips/02-data-shock/index.html",
  "preview_video": "clips-lab/flagship-motion-clips/02-data-shock/02-data-shock.mp4"
}
```

## Retrieval Rules

Use metadata in this order:

1. Hard-filter by `scenario`, `content_type`, `input_requirements`, and `anti_tags`.
2. Vector-search over `title`, `description`, `motion_patterns`, and `visual_register`.
3. Rerank by `quality_tier`, `quality_score`, and `reusability`.
4. Prefer hero-tier seeds for first drafts.
5. Use lower-tier assets only when they match rare constraints.

## Scenario Values

- `product_launch`
- `data_shock`
- `breaking_explainer`
- `concept_metaphor`
- `brand_drop`
- `app_feature`
- `cta_outro`
- `transition`

## Motion Pattern Values

- `kinetic_type_hit`
- `text_block_flash`
- `product_summon`
- `shape_burst`
- `broadcast_stinger`
- `slash_wipe`
- `mask_slice`
- `smear_transition`
- `data_hit`
- `chart_tear`
- `network_emergence`
- `ui_assembly`
- `interaction_pulse`
- `match_cut`
- `final_lockup`

## Quality Tier

- `hero`: high-quality seed; use as primary reference.
- `usable`: practical but not visually exceptional.
- `experimental`: interesting but risky.
- `reject`: keep only as anti-example.
