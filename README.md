# Calling for Backup: How Children Navigate Successive Robot Communication Failures



[Maria Teresa Parreira](https://www.mariateresaparreira.com/)* ¹ · [Isabel Neto](https://isabelcaniconeto.github.io/site/)* ² · [Filipa Rocha](https://web.tecnico.ulisboa.pt/filipa.rocha/)²³ · [Wendy Ju](https://www.wendyju.com/)¹

¹Cornell University · ²Lasige, Faculdade de Ciências · ³ITI/LarSys, Universidade de Lisboa 

*Equal contribution

---

## 🌐 Project Website
[**View Project Website**](https://irl-ct.github.io/calling-for-backup/)

![Calling for Backup - Main Video Vignette](docs/figures/badchild_videofigure.mp4)


### Experimental Conditions
- **Interruption Condition (n=30):** Robot interrupts child before they finish answering
- **Control Condition (n=29):** Robot does not interrupt
- **All participants** experienced 3 successive performance errors

### Robot Platform
- **Robot:** Simon (Nodbot) - simple 2-axis robot with speaker
- **Control:** Wizard-of-Oz methodology
- **Recording:** 2 cameras (room view + laptop webcam)

### Protocol
1. Introduction to robot Simon
2. Video visualization task (6 short videos with robots/humans, successes/failures)
3. Pre-interaction robot perception survey (5-point Likert scale)
4. Social error manipulation (interruption or control during Q&A)
5. **Performance error:** 3 successive failures to understand "call the researcher" command
6. Post-interaction robot perception survey
7. Debriefing and deception explanation

**Session duration:** ~7 minutes

## Research Question

**How do children perceive and react to repeated robot error?**

To investigate this question, we examine children's responses to two types of robot failures:

- **Social Error (Interruption):** Robot inappropriately interrupts the child during conversation, violating social norms
- **Performance Error (Successive Failure):** Robot fails to understand the child's request to "call the researcher" three successive times

## Key Findings

### Similarities with Adult Responses

Like adults (Liu et al., 2025), children demonstrated:

- ✅ **Verbal adaptation:** Modified prompts (repeating, simplifying, adding specificity) and adjusted vocal tone/cadence (slower speech, demanding/interrogative tones)
- 📈 **Emotional progression:** Similar evolution from confusion to frustration across successive errors
- ⏱️ **Response timing:** Increased response latencies and variability with successive failures
- 🚪 **Interaction abandonment:** Some participants completely discontinued interaction by the third error

### Key Differences from Adult Responses

Children exhibited distinct behavioral patterns:

- 🔴 **Greater disengagement:** Children showed notably more disengagement behaviors, often temporarily ignoring the robot
- 🙋 **External help-seeking ("Calling for Backup"):** Unlike adults who attempted self-directed problem-solving, children looked for or called the researcher, demonstrating different agency expectations
- 🙏 **Politeness strategies:** Children more readily shifted to polite language forms ("please") when initial commands failed
- ⚡ **Earlier disengagement:** Children showed disengagement beginning at Error I, while adults primarily abandoned after Error III (n=7)
- 🔄 **Mixed engagement patterns:** Children displayed more dynamic patterns, sometimes disengaging then re-engaging, unlike the more linear adult progression

### Social Error (Interruption)

- **84%** of children (21/25) in the Interruption condition shifted their answer to the new question, **not acknowledging the interruption**
- Only 2 children continued responding to the previous question
- Children appeared oblivious to or unconcerned with interruption as a social violation

### Robot Perception

**No significant changes** in robot perception across any measured dimension:
- Willingness to continue interacting
- Competence
- Trust
- Social acceptance
- Likeability

This suggests children have **more flexible conversational expectations** with robots compared to adults.

### Behavioral Response Patterns

**Most common engagement trajectories** (Error I → Error II → Error III):
1. Engage → Engage → Engage (n=15)
2. Engage → Disengage → Engage (n=5)
3. Engage → Disengage → Disengage (n=4)

**Response categories observed:**
- **Verbal reprompting:** Repeating, more specific/longer prompts, simpler prompts, term swapping
- **Vocal modifications:** Slower speech, demanding tone, interrogative tone, assertive tone, filler words
- **Physical behaviors:** Moving closer to robot, standing up, leaving room
- **Emotional displays:** Confusion, frustration, amusement/humor
- **Disengagement:** Looking for researcher, no prompt, quitting interaction

## Design Implications for Child-Robot Interaction

| Observed Behavior | Design Implication |
|-------------------|-------------------|
| Children's perception remained stable despite successive errors | **Design for Error Tolerance:** Focus on managing errors gracefully rather than aggressively eliminating them. Allow minor errors without elaborate apologies. |
| Children frequently call for adult help after repeated failures | **Facilitate External Help-Seeking:** Recognize requests for human assistance as valid and implement graceful handoff mechanisms. |
| Children use sophisticated verbal strategies (repetition, specificity, politeness) | **Implement Multi-Layered Conversational Repair:** Design systems sensitive to prompt reformulation and increase error confidence based on politeness markers. |
| Children exhibit dynamic engagement patterns | **Employ Non-Intrusive Error Recovery:** Recognize disengagement as active problem-solving. Avoid intrusive re-engagement; monitor passively. |
| Response latencies increase with successive errors | **Utilize Timing as Failure Metric:** Integrate response latency analysis as real-time measure of cognitive load and distress. |

## Repository Structure

```
.
├── docs/                                    # Project website files
│   ├── index.html                          # Main website page
│   ├── style.css                           # Website styling
│   ├── README.md                           # Website documentation
│   ├── figures/                            # All images and video
│   │   ├── badchild_videofigure.mp4       # Main video vignette
│   │   ├── collage_p*.png                 # Participant vignettes
│   │   ├── doodle_*.png                   # Behavioral illustrations
│   │   ├── experimental_setup.png         # Study setup
│   │   └── vignette_p*.png                # Additional examples
│   └── submission/                         # Paper PDFs
│       ├── manuscript_calling4backup.pdf
│       └── supp_material_calling4backup.pdf
├── submission/                             # Original submission materials
│   ├── manuscript_calling4backup.pdf
│   ├── supp_material_calling4backup.pdf
│   └── figures/                            # Paper figures
└── README.md                               # This file
```

## Materials

- **📄 Paper:** [submission/manuscript_calling4backup.pdf](submission/manuscript_calling4backup.pdf)
- **📑 Supplementary Material:** [submission/supp_material_calling4backup.pdf](submission/supp_material_calling4backup.pdf)
- **🎥 Video Figures:** Available in [docs/figures/](docs/figures/)
- **🌐 Project Website:** https://irl-ct.github.io/calling-for-backup/

## Keywords

successive error · robot error · reproducibility · child-robot interaction · error recovery · performance error · social error

## Citation

```bibtex
@inproceedings{parreira2026calling,
  title={Calling for Backup: How Children Navigate Successive Robot Communication Failures},
  author={Parreira, Maria Teresa and Neto, Isabel and Rocha, Filipa and Ju, Wendy},
  booktitle={TBD},
  year={2026},
```

## Related Work

This study reproduces and extends the successive robot failure paradigm from:
- Liu, S., Parreira, M. T., & Ju, W. (2025). "I'm Done": Describing Human Reactions to Successive Robot Failure. *HRI 2025*.

## Contact

For questions about this research, please contact the authors:
- **Maria Teresa Parreira:** mb2554@cornell.edu
- **Isabel Neto:** aineto@fc.ul.pt

---

© 2026 Authors. Licensed under Cornell University IRB exempt protocol #IRB0010006.
