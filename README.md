# Dyeing Recipe Lab – Textile Colour & Dye Calculator

Dyeing Recipe Lab is a Streamlit web application designed to help textile students practise basic dyeing calculations and explore digital colours. The project is maintained with GitHub and can be deployed through Streamlit Community Cloud.

## Features

### 1. Dye Recipe Calculator
- Enter fabric weight in kilograms.
- Enter dye concentration as a percentage on weight of fabric (% owf).
- Enter the liquor ratio.
- Calculate estimated dye mass and liquor volume.
- Add multiple dye or chemical components to a recipe table.
- Download the recipe as a CSV file.

### 2. RGB Colour Studio
- Adjust Red, Green, and Blue values from 0 to 255.
- View a live colour preview.
- Display RGB and HEX codes.
- Explore preset digital colours.

### 3. Colour Comparison
- Compare up to three digital colours using HEX codes.
- View RGB channel values in a table.
- Compare red, green, and blue channel values in an interactive chart.
- Download colour data as CSV.

### 4. Learning Corner
- Learn key textile-dyeing and digital-colour terms.
- Review the calculation formulas.
- Read a worked example and notes about colour-matching limitations.

## Project files

```text
Dyeing-Recipe-Lab/
├── App.py
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.10 or newer
- pip
- Internet connection for installing Python packages and deploying online

## Run the app locally

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start Streamlit:

   ```bash
   streamlit run App.py
   ```

5. Open the local address printed in the terminal, usually `http://localhost:8501`.

## Upload to GitHub

1. Sign in to [GitHub](https://github.com/).
2. Create a repository, for example `dyeing-recipe-lab`.
3. Upload `App.py`, `requirements.txt`, and `README.md` to the repository's root.
4. Commit the files.

## Deploy with Streamlit Community Cloud

1. Visit [Streamlit Community Cloud](https://share.streamlit.io/).
2. Sign in with GitHub and authorize repository access if prompted.
3. Create a new app and select your repository and branch.
4. Set the main file path to `App.py`.
5. Deploy the app.

## Calculation formulas

### Dye mass

`Dye (g) = Fabric weight (kg) × 1000 × Concentration (% owf) ÷ 100`

Example: 2 kg of fabric at 1.5% owf:

`2 × 1000 × 1.5 ÷ 100 = 30 g of dye`

### Approximate liquor volume

`Liquor volume (L) = Fabric weight (kg) × Liquor ratio factor`

Example: 2 kg of fabric at a 1:10 liquor ratio:

`2 × 10 = 20 L of liquor`

These formulas provide educational estimates. Actual process requirements may depend on the dyeing machine, bath preparation, fibre, dye class, and the laboratory's approved method.

## Important limitations and safety

- The RGB Colour Studio represents colours on a digital display. RGB or HEX values do not directly specify a physical textile dye recipe.
- The calculator does not determine salt, alkali, auxiliaries, pH, temperature curves, fixation, or dye exhaustion.
- Confirm calculations with your instructor or an approved technical recipe.
- Follow all laboratory chemical handling and safety procedures.

## Technologies used

- Python
- Streamlit
- Pandas
- Plotly
- GitHub
