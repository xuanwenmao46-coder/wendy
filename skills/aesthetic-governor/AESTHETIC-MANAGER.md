---
name: aesthetic-manager
description: Style profile registry for the AI video production system. Maps named real-world aesthetic anchors — designers, photographers, studios, brands — to precise, actionable video production parameters. Returns specific font families, tracking values, color constraints, motion parameters, and forbidden moves instead of adjectives. Any director in the system can load a named profile and receive an unambiguous production specification.
---

# Aesthetic Manager

## Purpose

The AestheticManager is the style profile registry for the video production system. It exists because adjectives fail.

When a user says "premium", every AI model in the pipeline defaults to black background, cyan glow, gradient text, and Inter Bold — every time. When a user says "Peter Lindbergh feeling", that phrase carries 40 years of specific decisions: 35mm grain on Tri-X 400, raking natural light that leaves half the face in shadow, zero retouching on skin, models standing not posing, 1:1 or 16:9 compositions with massive empty sky or wall, and a complete absence of color. Those decisions are incompatible with cyan glow. The AestheticManager encodes the difference.

Every profile is anchored on a real named practitioner, studio, or brand whose body of work constrains the output space. The profile translates that body of work into video-native parameters: specific font names (not categories), specific hex values (not palette moods), specific GSAP eases (not "smooth"), specific forbidden moves that would betray the anchor's DNA, and a museum test — a single sentence that defines whether the clip passes or fails on aesthetic grounds.

When a director receives a brief that names an aesthetic reference, they load the corresponding profile from this registry. The profile replaces the vague reference with an actionable specification. Downstream directors — Typography Director, Color Director, Motion Director — receive specific values, not adjectives.

---

## JSON Profile Schema

Every profile in this registry conforms to the following schema. All fields are required. No field may contain "TBD", "varies", or a generic category name in place of a specific value.

```json
{
  "profile_id": "string — snake_case identifier",
  "style_name": "string — human-readable name",
  "school": "one of: Information Architecture | Editorial Minimalist | Motion Experimental | Brutalist Raw | Warm Humanist | Modern Tool",
  "primary_benchmark": "named designer / studio / brand",
  "secondary_benchmarks": ["array of names"],
  "typography": {
    "display_family": "specific font name — not a generic category",
    "display_weight": 400,
    "display_tracking_start": "em value — beginning of dynamic tracking animation",
    "display_tracking_end": "em value — end state of dynamic tracking animation",
    "support_family": "specific font name",
    "support_weight": 400,
    "support_tracking": "em value",
    "alignment": "bottom-left | bottom-right | top-left | center (only when dramatically intentional)",
    "animation_curve": "cubic-bezier(x1, y1, x2, y2)",
    "forbidden_fonts": ["list of font names that would betray the anchor"]
  },
  "color": {
    "palette_mode": "monochrome | duotone | restrained-editorial | bold-poster | warm-neutral | dark-ground",
    "dominant_hex": "hex — present in approximately 70% of frame",
    "supporting_hex": "hex — present in approximately 20% of frame",
    "accent_hex": "hex — present in approximately 10% of frame; use sparingly",
    "film_grain": "none | subtle | medium | pronounced",
    "lut_reference": "descriptive name of LUT character",
    "negative_palette": ["forbidden color moves — specific, not generic"],
    "prompt_injection": "color and texture description for AI image/video generators",
    "negative_prompt_injection": "color and texture description to suppress in AI generators"
  },
  "motion": {
    "energy_level": "1–10",
    "primary_easing": "GSAP ease name or cubic-bezier string",
    "camera_vocabulary": ["array of allowed camera moves"],
    "motion_level": "0–100 — for AI video generator motion intensity parameter",
    "rhythm_profile": "explosive | editorial | luxury | technical | humanist",
    "forbidden_motion": ["list of forbidden motion patterns"]
  },
  "composition": {
    "hero_placement": "rule description",
    "negative_space_target": "percentage as string",
    "composition_rules": ["array of specific rules"],
    "forbidden_compositions": ["list of forbidden arrangements"]
  },
  "texture": {
    "imperfection_level": "none | subtle | medium | pronounced",
    "grain_strength": "0.0–1.0",
    "lens_breathing": true,
    "vignette": "none | subtle | medium"
  },
  "sound": {
    "material_metaphor": "description of the physical material the sound should evoke",
    "forbidden_sounds": ["list of specific forbidden sound types"]
  },
  "museum_test": "single sentence defining what passing looks like for this profile"
}
```

---

## Style Profiles

### 1. peter_lindbergh

```json
{
  "profile_id": "peter_lindbergh",
  "style_name": "Peter Lindbergh",
  "school": "Editorial Minimalist",
  "primary_benchmark": "Peter Lindbergh",
  "secondary_benchmarks": [
    "Helmut Newton (composition severity, not eroticism)",
    "Irving Penn (studio restraint, tonal compression)",
    "Patrick Demarchelier (natural gesture)",
    "Vogue Italia 1988–2002 editorial sensibility"
  ],
  "typography": {
    "display_family": "Didot",
    "display_weight": 400,
    "display_tracking_start": "0.18em",
    "display_tracking_end": "0.28em",
    "support_family": "Helvetica Now Text",
    "support_weight": 300,
    "support_tracking": "0.12em",
    "alignment": "bottom-left",
    "animation_curve": "cubic-bezier(0.25, 0.1, 0.25, 1.0)",
    "forbidden_fonts": [
      "Inter",
      "Roboto",
      "Montserrat",
      "Futura",
      "any rounded grotesque",
      "any variable font with visible axis animation",
      "script or handwritten faces"
    ]
  },
  "color": {
    "palette_mode": "monochrome",
    "dominant_hex": "#1A1A1A",
    "supporting_hex": "#F2F0EC",
    "accent_hex": "#8C8C8C",
    "film_grain": "pronounced",
    "lut_reference": "Kodak Tri-X 400 push-processed — crushed shadows, blown highlights on skin, mid-tone compression that reads silver not gray",
    "negative_palette": [
      "any color at all — this profile is monochrome absolute",
      "warm sepia toning",
      "cool blue-tinted monochrome (must read silver-neutral)",
      "digital clarity or noise-reduction smoothness",
      "HDR shadow recovery",
      "skin retouching or frequency separation"
    ],
    "prompt_injection": "black and white 35mm film photography, Kodak Tri-X grain, raking natural side light, deep shadows unretouched, silver gelatin print quality, high contrast without being harsh, raw skin texture visible, 1990s Vogue Italia editorial",
    "negative_prompt_injection": "color, sepia, teal tone, digital clean, smooth skin, retouched, HDR, cinematic color grade, studio strobe flat lighting, beauty lighting, soft focus"
  },
  "motion": {
    "energy_level": "2",
    "primary_easing": "cubic-bezier(0.25, 0.1, 0.25, 1.0)",
    "camera_vocabulary": [
      "static locked frame — the primary language",
      "very slow imperceptible push: scale 1.00 to 1.02 over 6–8 seconds",
      "single cut between frames — no transition, just cut",
      "slow fade to black between scenes at 1200ms sine.inOut"
    ],
    "motion_level": "8",
    "rhythm_profile": "luxury",
    "forbidden_motion": [
      "camera zoom with visible speed",
      "handheld shake or documentary wobble",
      "kinetic type or text that moves aggressively",
      "particle systems or generative motion",
      "wipe transitions of any kind",
      "color flashes or light leaks",
      "slow-motion at artificial frame rates (60fps+ look)",
      "any motion faster than a human exhale"
    ]
  },
  "composition": {
    "hero_placement": "human subject occupies 50–70% of frame height; placed left-center or center-left; eyes at upper third line; significant empty sky or wall above and behind",
    "negative_space_target": "35–45%",
    "composition_rules": [
      "Subject is always a person — never a product isolated on white",
      "At least one strong directional shadow element in frame",
      "Horizon line, if present, sits at lower third",
      "Clothing and body are read as sculptural form, not as product display",
      "Natural environment props (wind, water, architecture) when present are incidental not staged",
      "A second person in frame must have a real spatial relationship to the first — not a posed tableau"
    ],
    "forbidden_compositions": [
      "Product flat-lay or object isolation on white ground",
      "Symmetrical centered portrait with even fill lighting",
      "Three-subject lineup facing camera",
      "Any composition that looks like it required a stylist's intervention to arrange",
      "Text overlaid on the face or body of the subject"
    ]
  },
  "texture": {
    "imperfection_level": "pronounced",
    "grain_strength": 0.72,
    "lens_breathing": true,
    "vignette": "subtle"
  },
  "sound": {
    "material_metaphor": "The ambient sound of a large studio with a concrete floor — distant ventilation, occasional footstep, the mechanical click of a film camera shutter. Nothing electronic. Nothing mixed or produced.",
    "forbidden_sounds": [
      "music of any kind",
      "electronic or synthesized textures",
      "cinematic swells or risers",
      "UI or product sounds",
      "voiceover or narration unless the subject speaks naturally in frame",
      "any sound that suggests post-production awareness"
    ]
  },
  "museum_test": "A still frame pulled from any moment in the clip should be indistinguishable from a silver gelatin contact sheet print from a 1990s Lindbergh Vogue Italia session — grain present, shadows unretouched, the subject's humanity visible rather than their product role."
}
```

---

### 2. apple_keynote

```json
{
  "profile_id": "apple_keynote",
  "style_name": "Apple Keynote",
  "school": "Editorial Minimalist",
  "primary_benchmark": "Apple Inc. keynote and product film (2007–2023)",
  "secondary_benchmarks": [
    "Hartmut Esslinger / frogdesign (product as pure form)",
    "James Nachtwey (single-image authority)",
    "Dieter Rams (purpose-driven reduction)",
    "Chermayeff & Geismar (wordmark clarity)"
  ],
  "typography": {
    "display_family": "SF Pro Display",
    "display_weight": 200,
    "display_tracking_start": "0.00em",
    "display_tracking_end": "0.02em",
    "support_family": "SF Pro Text",
    "support_weight": 400,
    "support_tracking": "0.00em",
    "alignment": "center",
    "animation_curve": "cubic-bezier(0.4, 0.0, 0.2, 1.0)",
    "forbidden_fonts": [
      "Helvetica Neue (predecessor, now replaced)",
      "any display serif",
      "any condensed grotesque",
      "Myriad Pro",
      "Inter",
      "any font that does not have an Apple license or exact system match",
      "bold weights above 600 in any role"
    ]
  },
  "color": {
    "palette_mode": "dark-ground",
    "dominant_hex": "#000000",
    "supporting_hex": "#1C1C1E",
    "accent_hex": "#FFFFFF",
    "film_grain": "none",
    "lut_reference": "No LUT — pure digital black, no color cast, product photography grade with zero color contamination from environment",
    "negative_palette": [
      "gradient backgrounds of any kind",
      "colored accent on body text",
      "multiple accent colors in the same scene",
      "any background lighter than #1C1C1E in the dark-ground mode",
      "product imagery with colored studio backgrounds",
      "lens flares or light leaks"
    ],
    "prompt_injection": "product photography on pure black infinity cove, single overhead key light creating rim light on device edges, no background reflection, ultra-sharp macro detail on material texture, studio isolation, Apple product film quality",
    "negative_prompt_injection": "gradient background, colored backdrop, environment, people, hands, props, lens flare, light leak, film grain, warm tone, color cast"
  },
  "motion": {
    "energy_level": "3",
    "primary_easing": "cubic-bezier(0.4, 0.0, 0.2, 1.0)",
    "camera_vocabulary": [
      "very slow orbital rotation around product: 0.3°/second",
      "macro push-in to surface detail: scale 1.0 to 1.12 over 4 seconds",
      "vertical descent reveal: product falls into frame from above at constant velocity",
      "hard cut between product angles",
      "title fade-up from 0 opacity: 600ms"
    ],
    "motion_level": "12",
    "rhythm_profile": "luxury",
    "forbidden_motion": [
      "fast cuts under 1.5 seconds",
      "bouncy spring physics on the product object",
      "any motion suggesting urgency or excitement",
      "parallax layers that move at different speeds",
      "kinetic typography with character-by-character stagger",
      "particle systems or generative effects",
      "product vibration or jitter",
      "wipe or dissolve transitions between product angles"
    ]
  },
  "composition": {
    "hero_placement": "single product object centered on pure black ground, occupying 45–60% of frame area; product axis vertical or angled at maximum 15° from vertical; no background detail competing",
    "negative_space_target": "40–55%",
    "composition_rules": [
      "Only one object per frame — never two products simultaneously unless showing a lineup (which is its own scene type)",
      "Product must be large enough that material texture is visible at 720p",
      "Title copy appears only after the product has been on screen for at least 1.5 seconds",
      "Body copy maximum two lines at any moment",
      "Title line maximum four words unless a product name",
      "Final lockup: product + wordmark only — no tagline, no URL, no feature list"
    ],
    "forbidden_compositions": [
      "Feature card grid or comparison table as a primary scene",
      "Human hand holding the product as the hero image (hands are supporting role only)",
      "Multiple text columns in the same frame",
      "Product shown in a lifestyle environment as the opening frame",
      "Any frame that could be paused and mistaken for a competitor's product slide"
    ]
  },
  "texture": {
    "imperfection_level": "none",
    "grain_strength": 0.0,
    "lens_breathing": false,
    "vignette": "subtle"
  },
  "sound": {
    "material_metaphor": "The resonance of a machined aluminum surface being placed on glass — a single pure tone with a clean decay, no reverb room, no ambience. The silence between sounds is as designed as the sounds themselves.",
    "forbidden_sounds": [
      "orchestral or cinematic score during product reveal moments",
      "UI notification sounds",
      "human voice except in dedicated narrative segments",
      "any sound with a dirty or textured tail",
      "bass-heavy electronic music",
      "sound effects that imply the product is doing something it is not doing on screen"
    ]
  },
  "museum_test": "Every word on screen must earn its presence: if removing a word makes the frame worse, the word stays; if removing it makes no difference, it was never needed — and the product, lit on pure black, must look like an object worth the silence the clip has built around it."
}
```

---

### 3. a24_cinematic

```json
{
  "profile_id": "a24_cinematic",
  "style_name": "A24 Cinematic",
  "school": "Editorial Minimalist",
  "primary_benchmark": "A24 Films (2013–present)",
  "secondary_benchmarks": [
    "Roger Deakins (practical light, landscape authority)",
    "Lol Crawley (intimate documentary grammar)",
    "Ari Aster visual tempo (long hold, earned dread/wonder)",
    "Jonny Greenwood / Mica Levi score temperament (texture over theme)"
  ],
  "typography": {
    "display_family": "Canela",
    "display_weight": 300,
    "display_tracking_start": "0.06em",
    "display_tracking_end": "0.12em",
    "support_family": "Freight Text Pro",
    "support_weight": 400,
    "support_tracking": "0.03em",
    "alignment": "bottom-left",
    "animation_curve": "cubic-bezier(0.16, 1.0, 0.3, 1.0)",
    "forbidden_fonts": [
      "Inter",
      "Helvetica in any weight",
      "any grotesque sans as the display face",
      "condensed type of any kind",
      "script or decorative faces",
      "any font that reads as brand or corporate"
    ]
  },
  "color": {
    "palette_mode": "restrained-editorial",
    "dominant_hex": "#2A2318",
    "supporting_hex": "#C4B89A",
    "accent_hex": "#8B7355",
    "film_grain": "medium",
    "lut_reference": "Kodak Vision3 500T desaturated 40% — warm shadows, muted greens, skin tones read as warm parchment, sky desaturates to near-gray, no crushed blacks",
    "negative_palette": [
      "saturated primary colors (red, blue, green) as fills",
      "neon or electric accents of any kind",
      "pure white backgrounds",
      "pure black backgrounds without ambient detail",
      "digital clarity color grade — must feel photochemical",
      "color grading that draws attention to itself"
    ],
    "prompt_injection": "35mm film, Kodak Vision3, muted desaturated palette, practical natural light, golden hour or overcast diffuse, warm shadows, parchment skin tones, real location texture, festival film quality, A24 visual language",
    "negative_prompt_injection": "saturated colors, neon, clean digital grade, studio lighting, white background, pure black, color teal-orange, HDR, oversaturated sky"
  },
  "motion": {
    "energy_level": "3",
    "primary_easing": "cubic-bezier(0.16, 1.0, 0.3, 1.0)",
    "camera_vocabulary": [
      "locked static frame held for 4–8 seconds minimum",
      "very slow handheld drift: imperceptible 2–4px movement per second, never stabilized",
      "slow push-in: scale 1.00 to 1.06 over 5–7 seconds, motivated by dramatic tension",
      "single motivated pan: follows a subject action only, never decorative",
      "match cut between locations on a physical gesture"
    ],
    "motion_level": "15",
    "rhythm_profile": "editorial",
    "forbidden_motion": [
      "fast cuts under 2 seconds on a held scene",
      "drone aerial that reads as establishing shot rather than emotional perspective",
      "any camera move that is not motivated by the scene's dramatic logic",
      "slow-motion at artificial high frame rates",
      "kinetic type or animated typography effects",
      "wipe, swipe, or transition effects",
      "zoom that reads as camera operating rather than lens breathing"
    ]
  },
  "composition": {
    "hero_placement": "human subject at center or slightly off-center; environment given significant weight — minimum 30% of frame is place rather than person; subject never cropped at joints",
    "negative_space_target": "30–50%",
    "composition_rules": [
      "The location must read as a real place, not a set or an AI-generated environment",
      "At least one compositional element that is imperfect — a shadow crossing the wrong place, a background element slightly out of focus but still identifiable",
      "If no person is present, a single object in a real environment: the object is evidence of a person, not a product shot",
      "Practical light source must be visible or clearly implied in frame",
      "Color grade must make the viewer feel weather and time of day",
      "No decorative overlays, texture burns, or graphic elements on the film image"
    ],
    "forbidden_compositions": [
      "Product flat-lay or commercial product isolation",
      "Symmetrical hero centered on a clean colored background",
      "Title text overlaid on the human face",
      "Any frame that resembles a stock photo",
      "Multiple graphic elements competing with the photographic image"
    ]
  },
  "texture": {
    "imperfection_level": "medium",
    "grain_strength": 0.45,
    "lens_breathing": true,
    "vignette": "subtle"
  },
  "sound": {
    "material_metaphor": "The ambient presence of a real place — wind through grass, the acoustic signature of a room, fabric against skin, a distant sound that establishes geography. Sound design replaces score. Silence is a sound choice.",
    "forbidden_sounds": [
      "orchestral swell to signal emotion",
      "musical stinger on a cut",
      "UI or product sounds of any kind",
      "any sound that tells the viewer how to feel rather than where they are",
      "electronic music as a bed",
      "sound that could be mistaken for a trailer"
    ]
  },
  "museum_test": "A still frame taken at any random moment must look like a shot from a real film — specific location, real light, real person or object with weight and history — never a composite, never a prompt output that looks generated, never a frame that could be a stock photo."
}
```

---

### 4. saint_laurent_hedi_era

```json
{
  "profile_id": "saint_laurent_hedi_era",
  "style_name": "Saint Laurent — Hedi Slimane Era",
  "school": "Brutalist Raw",
  "primary_benchmark": "Saint Laurent Paris under Hedi Slimane (2012–2016)",
  "secondary_benchmarks": [
    "Helmut Newton (hard flash, maximum contrast)",
    "David Bailey (unretouched confrontation)",
    "Tom of Finland (graphic body as composition element)",
    "Richard Avedon late career (stark white ground, hard edge)"
  ],
  "typography": {
    "display_family": "Helvetica Now Display",
    "display_weight": 700,
    "display_tracking_start": "0.22em",
    "display_tracking_end": "0.36em",
    "support_family": "Times New Roman",
    "support_weight": 400,
    "support_tracking": "0.08em",
    "alignment": "bottom-left",
    "animation_curve": "cubic-bezier(0.0, 0.0, 0.2, 1.0)",
    "forbidden_fonts": [
      "Inter",
      "Roboto",
      "any humanist grotesque with friendly optical corrections",
      "rounded typefaces of any kind",
      "script or handwritten faces",
      "any font that suggests digital origin rather than print"
    ]
  },
  "color": {
    "palette_mode": "monochrome",
    "dominant_hex": "#000000",
    "supporting_hex": "#FFFFFF",
    "accent_hex": "#1A1A1A",
    "film_grain": "subtle",
    "lut_reference": "Hard flash photography black and white — maximum contrast with slight halation on white areas, skin reads bone-white or near-black with no midtone recovery, shadows crushed to absolute black",
    "negative_palette": [
      "any color whatsoever — this profile permits only black and white",
      "sepia or warm toning of any kind",
      "gray midtones that soften the contrast",
      "gentle or romantic black and white — must be harsh",
      "digital noise versus film grain — must read as flash photography not digital desaturation"
    ],
    "prompt_injection": "hard flash photography, extreme black and white contrast, no midtones, bone-white skin, crushed shadows, Helmut Newton severity, Saint Laurent Paris campaign aesthetic, editorial fashion photography, 35mm flash",
    "negative_prompt_injection": "color, sepia, warm tone, soft lighting, gentle contrast, midtone detail, ambient light, natural light, retouched skin, HDR"
  },
  "motion": {
    "energy_level": "4",
    "primary_easing": "cubic-bezier(0.0, 0.0, 0.2, 1.0)",
    "camera_vocabulary": [
      "locked static frame — the dominant mode",
      "single hard cut with zero transition",
      "extremely slow orbital: 0.1°/second — almost imperceptible",
      "cut to extreme detail: a button, a collar, a hand — held 2 seconds then cut back"
    ],
    "motion_level": "5",
    "rhythm_profile": "editorial",
    "forbidden_motion": [
      "any motion describable as elegant or flowing",
      "crossfades or dissolves",
      "kinetic type or text animation",
      "camera moves motivated by music rather than subject",
      "slow-motion at artificial frame rates",
      "lighting changes or color shifts during a shot",
      "anything that softens the confrontational quality of the image"
    ]
  },
  "composition": {
    "hero_placement": "figure occupies 60–80% of frame height, often cropped at top and bottom to emphasize the body's architectural quality; figure placed center or hard left; maximum 20% negative space around the figure",
    "negative_space_target": "15–25%",
    "composition_rules": [
      "The figure is always standing or in motion — never seated in a domestic way",
      "Clothing reads as architectural construction, not fashion display",
      "Background is pure white or pure black — never a location",
      "Type, when present, sits in the remaining space as a second compositional element equal in weight to the figure",
      "Type at extreme scale: display text minimum 80px at 720p, tracking minimum 0.22em all-caps",
      "The composition must look like it could be printed as a 2-meter billboard without any element looking small"
    ],
    "forbidden_compositions": [
      "Lifestyle or location photography",
      "Product displayed without the body that will wear it",
      "Multiple figures in an emotional scene together",
      "Warm or inviting framing",
      "Any compositional choice that suggests approachability"
    ]
  },
  "texture": {
    "imperfection_level": "subtle",
    "grain_strength": 0.28,
    "lens_breathing": false,
    "vignette": "none"
  },
  "sound": {
    "material_metaphor": "A single guitar note decayed in a very dry room. The sound of leather. A lock engaging. Silence treated as a positive compositional element, not an absence.",
    "forbidden_sounds": [
      "warm or romantic music",
      "electronic pop or fashion show EDM",
      "sound effects that comment on the visuals",
      "voiceover",
      "ambient lifestyle sounds (cafe, street, nature)",
      "any sound that feels inviting or friendly"
    ]
  },
  "museum_test": "The clip must read as a photograph-in-motion — hard, confrontational, black and white, with type that commands the same attention as the figure — as if Hedi Slimane approved every frame as a campaign image before it was animated."
}
```

---

### 5. loewe_editorial

```json
{
  "profile_id": "loewe_editorial",
  "style_name": "Loewe Editorial — Jonathan Anderson Era",
  "school": "Editorial Minimalist",
  "primary_benchmark": "Loewe under Jonathan Anderson (2013–present)",
  "secondary_benchmarks": [
    "Jasper Morrison (object honesty, craft visibility)",
    "Ian Berry / Magnum (documentary texture in still life)",
    "Lucie Rie (ceramic as art object not functional object)",
    "Monocle magazine editorial (serif body, wide margins, restraint)"
  ],
  "typography": {
    "display_family": "Tiempos Headline",
    "display_weight": 400,
    "display_tracking_start": "0.04em",
    "display_tracking_end": "0.10em",
    "support_family": "Suisse Int'l",
    "support_weight": 300,
    "support_tracking": "0.08em",
    "alignment": "bottom-left",
    "animation_curve": "cubic-bezier(0.25, 0.46, 0.45, 0.94)",
    "forbidden_fonts": [
      "Inter",
      "Montserrat",
      "Futura",
      "any geometric grotesque",
      "condensed type in any role",
      "script faces",
      "any display sans that reads as technology rather than craft"
    ]
  },
  "color": {
    "palette_mode": "warm-neutral",
    "dominant_hex": "#F0E8D8",
    "supporting_hex": "#2A2118",
    "accent_hex": "#8C6E4A",
    "film_grain": "subtle",
    "lut_reference": "Warm paper scan — slight warmth in the highlights, shadows read brown not blue-black, the overall impression is a high-quality art book photograph not a commercial product shot",
    "negative_palette": [
      "pure white backgrounds — must be warm off-white",
      "pure black — use warm near-black #2A2118 only",
      "saturated colors of any kind",
      "cool or blue-gray tones",
      "digital product photography cleanliness — must read as photographed not rendered",
      "any color that would look correct in a tech product campaign"
    ],
    "prompt_injection": "object photography on warm paper off-white ground, art book quality, natural raking light from one side, visible craft texture on surface, warm shadow, Loewe editorial quality, Jasper Morrison object honesty, no commercial sheen",
    "negative_prompt_injection": "white seamless background, commercial product photography, CGI render, studio strobe, cold tone, saturated color, tech product aesthetic, lifestyle photography with people"
  },
  "motion": {
    "energy_level": "2",
    "primary_easing": "cubic-bezier(0.25, 0.46, 0.45, 0.94)",
    "camera_vocabulary": [
      "locked static frame — primary mode",
      "very slow pull-back to reveal craft context: scale 1.04 to 1.00 over 6 seconds",
      "single macro push-in to texture detail: scale 1.00 to 1.08 over 5 seconds",
      "hard cut between object and detail — no transition",
      "slow fade between distinct scenes at 1000ms sine.inOut"
    ],
    "motion_level": "6",
    "rhythm_profile": "luxury",
    "forbidden_motion": [
      "kinetic type of any kind",
      "product rotation animation (the object must feel like it has weight and sits)",
      "fast cuts under 2 seconds",
      "any motion that suggests the object is a product to be purchased rather than an art object to be considered",
      "motion blur on the object",
      "camera moves unmotivated by the object's craft quality"
    ]
  },
  "composition": {
    "hero_placement": "single craft object or product on warm paper ground; object occupies 30–45% of frame; generous margin — minimum 15% frame space on every side of the object; object placed slightly left-of-center or right-of-center, never dead center",
    "negative_space_target": "55–65%",
    "composition_rules": [
      "The object must be photographed (or treated as photographed) with visible surface texture — leather grain, ceramic imperfection, woven thread",
      "Natural raking light from one side that creates shadow indicating three-dimensionality",
      "At least one edge of the object must have a soft shadow on the ground",
      "Type is placed in the large negative space area, never over the object",
      "Maximum one line of display type per scene",
      "Support type maximum 30px at 720p — this is not a headline system, it is a caption system"
    ],
    "forbidden_compositions": [
      "Multiple objects on screen simultaneously unless explicitly a collection scene",
      "Object on pure white or pure black background",
      "Product displayed in use or on a body",
      "Text overlaid on the object",
      "Grid of products (catalogue mode)",
      "Any composition that suggests e-commerce rather than gallery"
    ]
  },
  "texture": {
    "imperfection_level": "subtle",
    "grain_strength": 0.22,
    "lens_breathing": true,
    "vignette": "subtle"
  },
  "sound": {
    "material_metaphor": "The physical sound of the material being handled — leather stretching slightly, ceramic on a wooden surface, woven fabric under a finger. These sounds play at low volume as the only accompaniment to the visual.",
    "forbidden_sounds": [
      "music as a bed",
      "cinematic swells",
      "fashion show soundtrack (electronic or orchestral)",
      "voiceover that describes the object",
      "UI or product sounds",
      "any sound that tells the viewer what to think about the object rather than what the object sounds like"
    ]
  },
  "museum_test": "The object in frame must look like it belongs in a museum vitrine — its material quality the subject, not its commercial function — and the margins around it must feel as considered as the object itself."
}
```

---

### 6. linear_modern

```json
{
  "profile_id": "linear_modern",
  "style_name": "Linear Modern",
  "school": "Modern Tool",
  "primary_benchmark": "Linear (linear.app)",
  "secondary_benchmarks": [
    "Vercel (pure black canvas, deployment drama)",
    "Raycast (glass surface, keyboard culture)",
    "Linus Torvalds aesthetic (precision over decoration)",
    "Braun / Dieter Rams (less but better, function as ornament)"
  ],
  "typography": {
    "display_family": "Inter",
    "display_weight": 600,
    "display_tracking_start": "-0.02em",
    "display_tracking_end": "-0.03em",
    "support_family": "JetBrains Mono",
    "support_weight": 400,
    "support_tracking": "0.00em",
    "alignment": "top-left",
    "animation_curve": "cubic-bezier(0.22, 1, 0.36, 1)",
    "forbidden_fonts": [
      "any display serif",
      "Helvetica Neue as a primary face (reads analog not digital)",
      "Poppins or rounded grotesque of any kind",
      "decorative or script faces",
      "Roboto (reads Android/Material, not developer premium)",
      "any font at weight 800 or above"
    ]
  },
  "color": {
    "palette_mode": "dark-ground",
    "dominant_hex": "#16171C",
    "supporting_hex": "#1E1F25",
    "accent_hex": "#5E6AD2",
    "film_grain": "none",
    "lut_reference": "No LUT — pure digital precision; color accuracy over mood; the only warmth is in the near-black ground's slight warm undertone versus pure black",
    "negative_palette": [
      "purple-to-blue gradients as background fills",
      "cyan glow or halo effects",
      "any gradient on typography",
      "warm cream or paper tones (this is not Editorial Minimalist territory)",
      "red as a primary accent (reads alert not brand)",
      "multiple accent colors in the same scene"
    ],
    "prompt_injection": "dark SaaS UI, warm near-black background #16171C, hairline borders, developer tool premium, precise typography, Linear app aesthetic, no gradients, no glow, clean dark surface",
    "negative_prompt_injection": "gradient background, cyan glow, neon accent, warm cream, paper texture, film grain, light leak, purple-blue gradient, glass morphism blur"
  },
  "motion": {
    "energy_level": "6",
    "primary_easing": "cubic-bezier(0.22, 1, 0.36, 1)",
    "camera_vocabulary": [
      "no camera moves — the UI is the camera",
      "panel assembly: elements arrive from y+20px at 350ms cubic-bezier(0.22,1,0.36,1)",
      "product state change: new issue/task appears in the list with a 150ms snap",
      "precise mask reveal: content slides in behind a sharp edge, no feathering",
      "hard cut between scenes — no transition except product state change"
    ],
    "motion_level": "25",
    "rhythm_profile": "technical",
    "forbidden_motion": [
      "bouncy spring physics — snappy yes, bouncy never",
      "particle systems or generative effects",
      "slow dramatic reveals over 600ms",
      "camera zoom or scale applied to the whole canvas",
      "any motion describable as playful or warm",
      "animated gradients",
      "glow pulses or light sweeps"
    ]
  },
  "composition": {
    "hero_placement": "actual product UI occupies 55–70% of frame; UI must be large enough that individual interface elements are legible at 720p; title and supporting copy sit in remaining left or right space",
    "negative_space_target": "20–35%",
    "composition_rules": [
      "The product UI must be performing a visible action in every scene — an issue being created, a sprint loading, a deployment completing",
      "Hairline borders at rgba(255,255,255,0.06) define the panel structure — these are the only visible separators",
      "Keyboard shortcut chips must be visible inside the UI when relevant — they are a content signal, not decoration",
      "Typography hierarchy: one display headline maximum 80px, one support line maximum 28px, no more",
      "Every element on screen must be necessary — the removal test: if removing an element improves or does not change the frame, remove it"
    ],
    "forbidden_compositions": [
      "Abstract or metaphorical imagery replacing the actual product UI",
      "Feature card grids disconnected from the product interface",
      "Human hands or lifestyle photography as the hero",
      "Centered hero with radiating elements (reads generative, not Linear)",
      "Decorative pattern or texture backgrounds"
    ]
  },
  "texture": {
    "imperfection_level": "none",
    "grain_strength": 0.0,
    "lens_breathing": false,
    "vignette": "none"
  },
  "sound": {
    "material_metaphor": "A precisely machined mechanism — a keyboard switch actuating, a database transaction completing, a lock engaging at exactly the right moment. The sound of a well-engineered system working correctly.",
    "forbidden_sounds": [
      "organic sounds (paper, cloth, wood, breath)",
      "cinematic swells or dramatic risers",
      "UI sounds that feel playful or consumer-facing",
      "bass-heavy electronic music as a bed",
      "any sound that would suit a lifestyle or wellness brand",
      "sound that implies drama beyond the product performing its function"
    ]
  },
  "museum_test": "The product UI visible in the clip must be performing a real, legible action — not posed, not decorative — and the total visual system (dark ground, hairline surfaces, precise type) must communicate that the people who built this tool care about the craft of building tools."
}
```

---

### 7. bloomberg_authority

```json
{
  "profile_id": "bloomberg_authority",
  "style_name": "Bloomberg Authority",
  "school": "Information Architecture",
  "primary_benchmark": "Bloomberg Terminal and Bloomberg Television (2010–present)",
  "secondary_benchmarks": [
    "Edward Tufte (maximum data-ink ratio, no chartjunk)",
    "Massimo Vignelli (grid discipline, systematic hierarchy)",
    "Nate Silver / FiveThirtyEight (evidence-first editorial)",
    "Financial Times data journalism team"
  ],
  "typography": {
    "display_family": "IBM Plex Mono",
    "display_weight": 600,
    "display_tracking_start": "0.00em",
    "display_tracking_end": "0.02em",
    "support_family": "IBM Plex Sans",
    "support_weight": 400,
    "support_tracking": "0.04em",
    "alignment": "top-left",
    "animation_curve": "linear",
    "forbidden_fonts": [
      "Inter (too humanist, too SaaS)",
      "any serif in a data role",
      "Helvetica (too clean, lacks data density signal)",
      "any display font that decorates rather than presents",
      "rounded or geometric grotesque",
      "variable fonts with animated axes"
    ]
  },
  "color": {
    "palette_mode": "dark-ground",
    "dominant_hex": "#08111A",
    "supporting_hex": "#111C2E",
    "accent_hex": "#FFA02F",
    "film_grain": "none",
    "lut_reference": "No LUT — pure broadcast signal accuracy; amber-on-navy is the chromatic identity; no warmth, no film, no atmosphere",
    "negative_palette": [
      "cyan or teal accents (reads startup, not terminal)",
      "purple in any role",
      "gradient fills on any surface",
      "warm off-white backgrounds — this is a dark terminal, always",
      "green as a primary accent (reads only as data-positive, never as brand color)",
      "more than one accent color per scene"
    ],
    "prompt_injection": "Bloomberg terminal dark UI, amber on deep navy, monospaced data typography, hairline panel borders, data authority, broadcast financial television, no decoration, maximum data density",
    "negative_prompt_injection": "gradient, glow, warm tone, film grain, soft light, decorative elements, illustration, photography, any color that is not amber or white on dark navy"
  },
  "motion": {
    "energy_level": "4",
    "primary_easing": "linear",
    "camera_vocabulary": [
      "no camera moves — data is the motion",
      "data counter: number increments from start value to end value over 1.2s linear",
      "panel slide-in from right: x+40px to 0, 300ms power3.out",
      "lower-third snap: y-value snaps to position in steps(4) at 80ms",
      "ticker scroll: uniform linear movement at constant velocity"
    ],
    "motion_level": "18",
    "rhythm_profile": "technical",
    "forbidden_motion": [
      "elastic or bouncy motion on any element",
      "particle systems",
      "camera zoom or pan",
      "decorative entry animations (type should arrive, not perform)",
      "motion that slows the viewer's ability to read the data",
      "any effect that reads as 'fancy' rather than 'precise'"
    ]
  },
  "composition": {
    "hero_placement": "primary metric occupies upper-left third with maximum type size 72px; supporting data fills the remaining frame in a multi-pane grid with 1px hairline dividers; no single element owns more than 40% of frame unless it is the single headline metric",
    "negative_space_target": "15–25%",
    "composition_rules": [
      "Every number on screen must have a label — no orphan metrics",
      "Column alignment must be mathematically consistent — numbers align on decimal point",
      "Tabular numerals always — font-variant-numeric: tabular-nums without exception",
      "Panel borders are hairlines at #2A3554 — 1px only, never 2px",
      "Amber #FFA02F is used only for primary metrics and key headlines — never as a background fill",
      "Positive data delta: #00B96B; negative data delta: #F23645 — these are the only additional colors permitted"
    ],
    "forbidden_compositions": [
      "Centered hero layout with decorative framing",
      "Photography or illustration competing with data",
      "Rounded corners on any panel or data container",
      "Gradient fills on panels or charts",
      "More than 6 distinct data points in a single frame",
      "Any decorative element that carries no data value"
    ]
  },
  "texture": {
    "imperfection_level": "none",
    "grain_strength": 0.0,
    "lens_breathing": false,
    "vignette": "none"
  },
  "sound": {
    "material_metaphor": "A trading floor at controlled volume — the dry percussive snap of a transaction confirming, the institutional thud of a major number arriving, the short tick of a data update. Electronics that sound like infrastructure, not consumer products.",
    "forbidden_sounds": [
      "cinematic music of any kind",
      "warm or organic sounds",
      "soft whooshes",
      "any sound that suggests a consumer product",
      "airy risers or emotional swells",
      "silence during data reveals — every metric hit needs a dry percussive confirmation"
    ]
  },
  "museum_test": "Every number visible in the clip must earn its presence — labeled, contextualized, readable in 0.5 seconds — and the total visual system must communicate that the data is the authority, not the design around it."
}
```

---

### 8. naoto_fukasawa_muji

```json
{
  "profile_id": "naoto_fukasawa_muji",
  "style_name": "Naoto Fukasawa / MUJI",
  "school": "Editorial Minimalist",
  "primary_benchmark": "Naoto Fukasawa and Kenya Hara / MUJI design philosophy",
  "secondary_benchmarks": [
    "Dieter Rams (function as the only ornament)",
    "John Pawson (architecture of absence)",
    "Shiro Kuramata (void as material)",
    "MUJI global campaign photography (single object, off-white ground, no copy)"
  ],
  "typography": {
    "display_family": "Helvetica Neue",
    "display_weight": 300,
    "display_tracking_start": "0.14em",
    "display_tracking_end": "0.20em",
    "support_family": "Helvetica Neue",
    "support_weight": 300,
    "support_tracking": "0.10em",
    "alignment": "bottom-left",
    "animation_curve": "cubic-bezier(0.25, 0.1, 0.25, 1.0)",
    "forbidden_fonts": [
      "any display serif",
      "any grotesque with personality or character",
      "Inter (too digital-native, too contemporary)",
      "any variable font with visible axis transitions",
      "bold weights above 400 — this profile is weight-300 throughout",
      "any typeface that would draw attention to itself"
    ]
  },
  "color": {
    "palette_mode": "restrained-editorial",
    "dominant_hex": "#F5F2EC",
    "supporting_hex": "#2C2C2A",
    "accent_hex": "#C8161D",
    "film_grain": "none",
    "lut_reference": "No LUT — pure flat scan of off-white paper stock; the only light is the object's own shadow on the ground; no atmosphere, no warmth manipulation, no color mood",
    "negative_palette": [
      "pure white #FFFFFF — must be warm off-white #F5F2EC or similar",
      "any saturated color in a significant area",
      "warm or ambient atmosphere lighting on the object",
      "the MUJI red #C8161D used as anything larger than a small corner mark or label",
      "gradients of any kind",
      "photographic background that suggests a place"
    ],
    "prompt_injection": "MUJI product photography, warm off-white ground, single object, natural flat diffuse light, no shadow drama, object at 30% of frame, 70% empty ground, no copy, no props, radical emptiness",
    "negative_prompt_injection": "colored background, dramatic lighting, shadow play, multiple objects, props, lifestyle context, people, warm atmosphere, gradient, grain, any color except off-white and the object's own color"
  },
  "motion": {
    "energy_level": "1",
    "primary_easing": "cubic-bezier(0.25, 0.1, 0.25, 1.0)",
    "camera_vocabulary": [
      "locked static frame — the only mode for 90% of the clip",
      "single very slow top-down descent reveal: object settles into frame over 3 seconds as if placed by hand",
      "imperceptible scale: 1.000 to 1.008 over 8 seconds — below the threshold of perceptible zoom",
      "single hard cut to a different angle of the same object — no transition"
    ],
    "motion_level": "3",
    "rhythm_profile": "luxury",
    "forbidden_motion": [
      "any motion that draws attention to itself",
      "object rotation for display purposes",
      "kinetic type or animated typography",
      "any transition effect",
      "camera moves faster than the human eye naturally moves",
      "motion that implies urgency, excitement, or commercial pressure",
      "multiple simultaneous animations"
    ]
  },
  "composition": {
    "hero_placement": "single object occupies maximum 30–35% of frame area; object placed at geometric center or slightly above center; the remaining 65–70% of frame is empty off-white ground; no other element competes",
    "negative_space_target": "65–70%",
    "composition_rules": [
      "One object per frame — absolute, no exceptions",
      "The object must cast a soft, barely-visible shadow that proves it occupies physical space",
      "No copy except a single small label, maximum 18px at 720p, placed bottom-left with generous margin",
      "The object's own material quality is the only visual interest — no light drama, no angle drama",
      "The emptiness is not leftover space — it is the primary design material, carrying as much intention as the object",
      "The frame must work at any scale from a postage stamp to a billboard — the emptiness scales with it"
    ],
    "forbidden_compositions": [
      "Two objects in the same frame",
      "Object touching any edge of the frame",
      "Text anywhere except the small bottom-left label",
      "Any decorative element accompanying the object",
      "Environment or contextual props that suggest use",
      "Lighting that creates dramatic shadow play rather than quiet material revelation"
    ]
  },
  "texture": {
    "imperfection_level": "none",
    "grain_strength": 0.0,
    "lens_breathing": false,
    "vignette": "none"
  },
  "sound": {
    "material_metaphor": "The sound the object would make if you placed it on a table in a quiet room — the brief, clean contact of material on surface, then silence. The silence after this sound is longer than the sound itself.",
    "forbidden_sounds": [
      "music of any kind",
      "ambient atmospheric sound",
      "cinematic processing",
      "voiceover describing the object",
      "any sound implying a place or a story around the object",
      "multiple sound events — maximum one sound per scene, followed by silence"
    ]
  },
  "museum_test": "The object in frame must look so correctly placed in its void that removing it would make the emptiness feel wrong — and the emptiness must feel so deliberately designed that filling it with anything would be a mistake."
}
```

---

## How to Apply a Profile

### Step 1 — Identify the named anchor

When a user says "Peter Lindbergh feeling", "Apple-like", "Linear vibes", or names any designer, photographer, studio, or brand, treat this as a profile load instruction. Do not interpret the reference as a style adjective. Map it to the nearest profile ID in this registry.

If the reference does not match any profile exactly, find the closest `primary_benchmark` or `secondary_benchmarks` match. If the reference is ambiguous between two profiles, ask the user one clarifying question: "Do you mean the photography aesthetic, the typography system, or the motion grammar?"

### Step 2 — Load the profile

The Aesthetic Governor reads the full profile JSON from this registry. It extracts the following parameter blocks and passes them to the relevant downstream directors:

**Passed to Typography Director:**
- `typography.display_family`
- `typography.display_weight`
- `typography.display_tracking_start` and `display_tracking_end`
- `typography.support_family`
- `typography.support_weight`
- `typography.support_tracking`
- `typography.alignment`
- `typography.animation_curve`
- `typography.forbidden_fonts`

**Passed to Color Director:**
- `color.palette_mode`
- `color.dominant_hex`
- `color.supporting_hex`
- `color.accent_hex`
- `color.film_grain`
- `color.lut_reference`
- `color.negative_palette`
- `color.prompt_injection`
- `color.negative_prompt_injection`

**Passed to Motion Director:**
- `motion.energy_level`
- `motion.primary_easing`
- `motion.camera_vocabulary`
- `motion.motion_level`
- `motion.rhythm_profile`
- `motion.forbidden_motion`
- `composition.hero_placement`
- `composition.negative_space_target`
- `composition.composition_rules`
- `composition.forbidden_compositions`
- `texture.imperfection_level`
- `texture.grain_strength`
- `texture.lens_breathing`
- `texture.vignette`

**Passed to Sound Director:**
- `sound.material_metaphor`
- `sound.forbidden_sounds`

### Step 3 — Enforce forbidden moves before code

Before any implementation begins, the Aesthetic Governor runs a forbidden-moves check against the draft brief. Any element from the following lists must be removed or redesigned before implementation:

- `typography.forbidden_fonts` — if the current font choice appears in this list, it must be replaced
- `color.negative_palette` — if any current color move appears in this list, it must be removed
- `motion.forbidden_motion` — if any current motion pattern appears in this list, it must be replaced
- `composition.forbidden_compositions` — if the current layout approach appears in this list, it must be redesigned

The forbidden-moves check is not optional. It is the primary mechanism by which the AestheticManager prevents aesthetic drift.

### Step 4 — Apply the museum test

Before finalizing the brief, the Aesthetic Governor evaluates the complete visual plan against the profile's `museum_test` sentence. This is a binary pass/fail judgment. If the plan does not pass the museum test, the brief is returned to the directing layer for revision.

The museum test is intentionally written in subjective human terms. It cannot be automated. The directing agent must make an honest judgment.

### Step 5 — Write the locked aesthetic contract

The Aesthetic Governor writes a compact aesthetic contract into the video brief:

```markdown
## Aesthetic Contract

**Profile loaded:** [profile_id]
**Museum test:** [copy the museum_test sentence here]

**Typography lock:** [display_family] [display_weight] / [support_family] [support_weight]
**Tracking animation:** [display_tracking_start] → [display_tracking_end] at [animation_curve]
**Color lock:** [dominant_hex] / [supporting_hex] / [accent_hex] — [palette_mode]
**Motion lock:** Energy [energy_level]/10 — [rhythm_profile] — [primary_easing]
**Grain/texture:** [film_grain] grain, [grain_strength] strength, vignette [vignette]

**Forbidden moves confirmed clear:** [list of the checked categories]
```

This contract is the single source of truth for all downstream implementation. If a downstream director asks "what font should I use?" or "what color is the background?", the answer comes from this contract, not from re-interpreting the user's original reference.

---

## Combining Profiles

Users frequently name two aesthetic anchors together: "Peter Lindbergh meets Linear", "A24 cinematic but with Bloomberg data authority", "Loewe editorial feeling for an Apple product reveal."

The combination rule is strict and exists to prevent aesthetic incoherence.

### The Primary/Secondary Rule

One profile must be declared **PRIMARY**. The other is **SECONDARY**.

The PRIMARY profile:
- Controls all forbidden moves — its entire `forbidden_motion`, `color.negative_palette`, `composition.forbidden_compositions`, and `typography.forbidden_fonts` lists are enforced without exception
- Controls the `museum_test` — the final clip is evaluated only against the primary profile's museum test
- Controls the `composition` block entirely
- Controls the `motion` block entirely
- Controls the `texture` block entirely
- Controls the `sound` block entirely

The SECONDARY profile may influence:
- `typography.display_family` and `typography.display_weight` only — if the secondary profile's typography is more distinctive and does not violate the primary profile's forbidden fonts
- `color.accent_hex` only — if the secondary profile's accent color does not violate the primary profile's negative palette

The SECONDARY profile may **not** influence:
- Any forbidden moves list — the primary profile's forbidden moves are absolute
- Composition, negative space, or hero placement
- Motion energy, rhythm, or easing
- Sound or texture

### How to determine which profile is PRIMARY

**When the user says "X meets Y" or "X with Y energy":** X is PRIMARY.

**When the user says "like X but more Y":** X is PRIMARY.

**When the user says "Y feeling for an X product":** If X is a named profile in this registry (e.g., Apple), X is PRIMARY. If X is a product category (not a registered profile), Y is PRIMARY.

**When the user says two names with no qualifier:** The directing agent must ask: "Which should define the overall grammar — [Profile A] or [Profile B]? The primary profile controls all forbidden moves." This is a required decision; it cannot be deferred.

### Combination example

User says: "Peter Lindbergh meets Linear"

- PRIMARY: `peter_lindbergh`
- SECONDARY: `linear_modern`

Result:
- Monochrome absolute — no color whatsoever (peter_lindbergh forbidden: "any color at all")
- Film grain pronounced (peter_lindbergh texture)
- Motion energy 2/10, luxury rhythm (peter_lindbergh motion)
- Static locked frame or imperceptible push (peter_lindbergh camera vocabulary)
- No product UI visible (peter_lindbergh: "Product flat-lay or object isolation" forbidden — but the human subject rule applies; a person using a tool is acceptable if it reads as Lindbergh, not Linear)
- Typography: Inter 600 (linear_modern display) is permitted as a secondary influence IF it does not violate peter_lindbergh's forbidden fonts — Inter is on peter_lindbergh's forbidden list. Therefore Inter is **not** permitted. Typography reverts to primary: Didot 400.
- Museum test: peter_lindbergh's test applies: "A still frame pulled from any moment must be indistinguishable from a silver gelatin contact sheet print from a 1990s Lindbergh Vogue Italia session."

### Hard combination incompatibilities

The following profile pairs are incompatible and should not be combined. If a user requests them together, the directing agent must flag the incompatibility and ask the user to choose one:

| Pair | Reason |
|---|---|
| `peter_lindbergh` + `bloomberg_authority` | Lindbergh forbids all color; Bloomberg requires amber #FFA02F as a core element |
| `apple_keynote` + `saint_laurent_hedi_era` | Apple forbids bold weights above 600 and requires centered composition; Saint Laurent requires confrontational left-anchor and hard contrast |
| `naoto_fukasawa_muji` + `bloomberg_authority` | MUJI requires 65%+ empty space; Bloomberg requires maximum data density (15–25% negative space) |
| `a24_cinematic` + `linear_modern` | A24 forbids product UI and digital aesthetics; Linear requires the product UI as the hero |
| `loewe_editorial` + `bloomberg_authority` | Loewe requires warm paper ground and object honesty; Bloomberg requires dark-ground terminal density |

---

## Fallback Behavior

When no aesthetic profile is named by the user and no aesthetic reference can be inferred from the brief, the Aesthetic Governor defaults to a category-based profile selection.

| Brief category | Default profile |
|---|---|
| Luxury / brand / fashion / cosmetics / premium consumer | `loewe_editorial` |
| Product / SaaS / developer tool / app / technical | `linear_modern` |
| Data / financial / metrics / journalism / research / analytics | `bloomberg_authority` |
| Lifestyle / educational / wellness / inspirational / human story | `naoto_fukasawa_muji` |

The default is not a suggestion. It is the loaded profile. All forbidden moves, typography locks, and color constraints from the default profile are enforced exactly as they would be for a named reference.

If a brief spans multiple categories (e.g., a product with a human lifestyle component), the Aesthetic Governor selects the default for the **primary emotional job** of the clip — not the surface content. A SaaS tool marketed through a human story still loads `linear_modern`, not `naoto_fukasawa_muji`, because the primary job is to demonstrate the product's capability.

If the primary emotional job is genuinely ambiguous between two categories, the Aesthetic Governor loads `loewe_editorial` as the universal fallback — it is the profile with the greatest compatibility with other visual systems and the fewest hard incompatibilities.

---

## References

- For the six design school DNA, video-native token values, and composition rules per school: [STYLE-SCHOOL-MAP.md](../aesthetic-layout-direction/STYLE-SCHOOL-MAP.md)
- For the overall aesthetic governance layer that invokes this manager: [AESTHETIC-GOVERNOR.md](AESTHETIC-GOVERNOR.md)
- For color hex values, LUT references, film grain implementation, and palette enforcement: [COLOR-DIRECTOR.md](COLOR-DIRECTOR.md)
- For the typography selection workflow that receives `typography.*` values from this manager: [../typography-selection/SKILL.md](../typography-selection/SKILL.md)
- For optical tracking corrections and CJK density compensation applied on top of this manager's tracking values: [../typography-optics/SKILL.md](../typography-optics/SKILL.md)
- For motion pattern implementation that receives `motion.*` values from this manager: [../motion-graphic-design/SKILL.md](../motion-graphic-design/SKILL.md)
- For the overall video production orchestration layer: [../flagship-video-director/SKILL.md](../flagship-video-director/SKILL.md)
