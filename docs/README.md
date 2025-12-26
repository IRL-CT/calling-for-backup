# Calling for Backup: How Children Navigate Successive Robot Communication Failures

This is the project website for the HRI 2026 paper "Calling for Backup: How Children Navigate Successive Robot Communication Failures" by Maria Teresa Parreira, Isabel Neto, Filipa Rocha, and Wendy Ju.

## Viewing the Website

To view the website locally:

1. Open `index.html` in a web browser
2. Or use a simple HTTP server:
   ```bash
   # Using Python 3
   python -m http.server 8000

   # Using Python 2
   python -m SimpleHTTPServer 8000

   # Using Node.js
   npx http-server
   ```

3. Navigate to `http://localhost:8000` in your browser

## Hosting on GitHub Pages

To host this website on GitHub Pages:

1. Push the `docs` folder to your GitHub repository
2. Go to repository Settings > Pages
3. Select "Deploy from a branch"
4. Choose `main` branch and `/docs` folder
5. Save

Your site will be available at: `https://yourusername.github.io/badrobots-meets-kids/`

## Structure

- `index.html` - Main website content
- `style.css` - Styling and layout
- `figures/` - All images and video from the paper
- `submission/` - Paper PDFs and supplementary materials

## Paper Abstract

How do children respond to repeated robot errors? While prior research has examined adult reactions to successive robot errors, children's responses remain largely unexplored. This study reproduces the successive robot failure paradigm with child participants (N=59, ages 8-10) to examine how young users respond to repeated robot conversational errors.

We found both similarities and differences compared to adult responses. Like adults, children adjusted their prompts and exhibited increasingly emotional responses. However, children demonstrated more disengagement behaviors, including actively seeking an adult ("calling for backup"). These findings inform the design of more effective and developmentally appropriate human-robot interaction systems.

## Citation

```bibtex
@inproceedings{parreira2026calling,
  title={Calling for Backup: How Children Navigate Successive Robot Communication Failures},
  author={Parreira, Maria Teresa and Neto, Isabel and Rocha, Filipa and Ju, Wendy},
  booktitle={Proceedings of ACM/IEEE International Conference on Human-Robot Interaction (HRI)},
  year={2026},
  location={Edinburgh, Scotland, UK}
}
```
