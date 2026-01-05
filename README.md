
# SVLF EMI Calculator (Flask)

A simple Flask web app implementing a **Flat-Rate EMI** calculator with **processing charges** (percentage or fixed ₹) and **interest** as either **% per annum** or **₹ per month**.

## Features
- Processing charges input: **%** (default 10%) or **₹ amount**; computed amount added to principal.
- Interest input: **% per annum** or **₹ per month** (default ₹2/month).
- Outputs: Processing amount, Adjusted principal, Total interest, Total payable, Monthly EMI.

## Run locally
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
Open http://localhost:8000 in your browser.

## Deploy to Render (free tier)
1. Create a new **Web Service**.
2. Connect your GitHub repo.
3. Set **Build Command**: `pip install -r requirements.txt`
4. Set **Start Command**: `python app.py`
5. Set **Port**: 8000 (Render will detect from logs).

## Notes
- This app uses the **Flat-Rate** method you requested. If you prefer **reducing balance**, we can add it as an option.
- For ₹/month interest, the app treats it as a fixed monthly addition independent of principal.
