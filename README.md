# Cardiotree Classifier — simple web runner

This keeps the original Python analysis and adds a minimal web page with a **Run program** button.

## Files to put in the GitHub repository root
- `index.html`
- `style.css`
- `script.js`
- `main.py` (the web-ready version with interactive `input()` pauses removed)
- `GWCutilities.py`
- `heartDisease_2020_sampling.csv`
- `requirements.txt`
- `api/run.py`

Keep the CSV and `GWCutilities.py` alongside `main.py`.

## Deploy
1. Upload these files and the `api` folder to the root of your GitHub repository.
2. Import the repository into Vercel.
3. Choose **Other** if asked for a framework.
4. Set no build command; deploy.
5. Open the deployed page and click **Run program**.

Vercel will run the Python analysis through `/api/run` and show its printed output on the page. The first deployment may need troubleshooting if the Python dependencies or serverless function size exceed the limits of the selected Vercel plan.

## Important
This is an educational model, not a medical diagnostic tool. Do not use it for health decisions.
