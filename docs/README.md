# Calling for Backup: How Children Navigate Successive Robot Communication Failures

**Project Website for HRI 2026**

Maria Teresa Parreira\* · Isabel Neto\* · Filipa Rocha · Wendy Ju

\*Equal contribution

---

## About

This is the project website for our HRI 2026 paper exploring how children respond to repeated robot errors. Unlike adults who primarily persist with the robot, children demonstrate unique behaviors including actively seeking external help from adults - what we call "calling for backup."

### Research Questions

- **How do children perceive and react to repeated robot errors?**
- **Social Error:** How do children respond to inappropriate interruptions?
- **Performance Error:** How do children adapt to 3 successive conversational failures?

### Key Findings

- ✅ Children show **similar** verbal adaptations and emotional progressions as adults
- 🆕 Children demonstrate **more disengagement** behaviors (ignoring, seeking help)
- 🤝 Children actively **seek adult help** unlike self-directed adult problem-solving
- 💭 Robot errors **did not change** children's perception of the robot
- 🔄 Children show **dynamic engagement patterns** (disengage then re-engage)

## Viewing the Website

### Option 1: Open directly
Simply open `index.html` in your web browser.

### Option 2: Local server (recommended)
Using a local server ensures all assets load correctly:

```bash
# Navigate to docs directory
cd docs

# Using Python 3
python -m http.server 8000

# Using Python 2
python -m SimpleHTTPServer 8000

# Using Node.js
npx http-server

# Using PHP
php -S localhost:8000
```

Then navigate to `http://localhost:8000` in your browser.

## Hosting on GitHub Pages

The website is hosted at: **https://irl-ct.github.io/calling-for-backup/**

To deploy this website publicly:

1. **Push to GitHub:**
   ```bash
   git add docs/
   git commit -m "Add project website"
   git push origin main
   ```

2. **Enable GitHub Pages:**
   - Go to https://github.com/IRL-CT/calling-for-backup/settings/pages
   - Source: **Deploy from a branch**
   - Branch: **main** → Folder: **/docs**
   - Click **Save**

3. Wait 1-2 minutes for GitHub to build and deploy

4. Your site will be live at: **https://irl-ct.github.io/calling-for-backup/**

### Troubleshooting 404 Error

If you see a 404 error:

1. **Check the docs folder exists in your repo:**
   - Visit https://github.com/IRL-CT/calling-for-backup/tree/main/docs
   - Ensure `index.html`, `style.css`, and `figures/` are there

2. **Verify GitHub Pages settings:**
   - Go to Settings → Pages
   - Confirm it shows: "Your site is live at https://irl-ct.github.io/calling-for-backup/"
   - Make sure Branch is set to `main` and folder is `/docs`

3. **Wait for deployment:**
   - Check the Actions tab: https://github.com/IRL-CT/calling-for-backup/actions
   - Look for "pages build and deployment" workflow
   - Wait for it to complete (green checkmark)

4. **Hard refresh your browser:**
   - Press `Ctrl+Shift+R` (Windows/Linux) or `Cmd+Shift+R` (Mac)

5. **Check you're visiting the right URL:**
   - ❌ Wrong: https://github.com/IRL-CT/calling-for-backup
   - ✅ Correct: https://irl-ct.github.io/calling-for-backup/

## Website Structure

```
docs/
├── index.html              # Main website
├── style.css              # Styling and responsive design
├── README.md              # This file
├── figures/               # All visual assets
│   ├── badchild_videofigure.mp4    # Main video vignette
│   ├── collage_p*.png              # Participant vignettes
│   ├── doodle_*.png                # Behavioral illustrations
│   ├── setup_cropped.png           # Experimental setup
│   └── vignette_p*.png             # Additional vignettes
└── submission/            # Paper materials
    ├── manuscript_calling4backup.pdf
    └── supp_material_calling4backup.pdf
```

## Website Features

### Content Sections
- **Hero Video:** Prominent video figure showing child's reactions to successive errors
- **Abstract:** Research overview and key findings
- **Research Focus:** Study questions and error types
- **Experimental Setup:** Protocol and methodology
- **Example Vignettes:** Visual examples from different participants
- **Key Findings:** Similarities and differences with adult responses
- **Design Implications:** Practical guidelines for child-robot interaction
- **Behavioral Illustrations:** Doodle-style visualizations
- **Citation:** BibTeX format for referencing

### Design Features
- Clean, academic single-page layout
- Responsive design (mobile-friendly)
- Color-coded sections for easy navigation
- Grid layouts for figures
- Embedded video with controls
- Links to paper PDF and supplementary materials

## Study Overview

**Participants:** 59 children, ages 8-10
**Design:** Two conditions (Interruption vs. Control)
**Measures:** Video analysis, behavioral coding, robot perception surveys

**Protocol:**
1. Introduction to robot Simon (Nodbot)
2. Video visualization task
3. Pre-interaction robot perception survey
4. Social error manipulation (interruption or control)
5. Performance error: 3 successive failures to understand
6. Post-interaction robot perception survey

## Design Implications

Our findings suggest several key design principles for child-robot interaction systems:

1. **Design for Error Tolerance:** Leverage children's flexible expectations
2. **Facilitate External Help-Seeking:** Implement graceful human handoff mechanisms
3. **Multi-Layered Conversational Repair:** Detect prompt reformulations and politeness markers
4. **Non-Intrusive Error Recovery:** Allow natural re-engagement after disengagement
5. **Utilize Timing as Metric:** Monitor response latencies for distress detection

## Citation

If you use this work, please cite:

```bibtex
@inproceedings{parreira2026calling,
  title={Calling for Backup: How Children Navigate Successive Robot Communication Failures},
  author={Parreira, Maria Teresa and Neto, Isabel and Rocha, Filipa and Ju, Wendy},
  booktitle={Proceedings of the 2026 ACM/IEEE International Conference on Human-Robot Interaction (HRI)},
  year={2026},
  location={Edinburgh, Scotland, UK},
  publisher={ACM}
}
```

## Related Work

This study reproduces and extends the successive robot failure paradigm from:
- Liu, S., Parreira, M. T., & Ju, W. (2025). "I'm Done": Describing Human Reactions to Successive Robot Failure. *HRI 2025*.

## License

© 2026 Authors. This website is for academic purposes.

## Contact

For questions about this research, please contact the authors through their affiliated institutions:
- Cornell University
- Faculdade de Ciências, Universidade de Lisboa
- Instituto Superior Técnico, Universidade de Lisboa
