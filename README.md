# Bank Fraud Analysis

Analysis of financial transactions to identify patterns associated with fraud, using SQL and Power BI, with data loaded via a Python/Postgres pipeline.

**Data source:** [Kaggle — Financial Transactions Dataset for Fraud Detection](https://www.kaggle.com/) (synthetic data). Analysis is based on a stratified random sample of 500,000 transactions out of the full dataset.

## Contents

- `data.py` — loads the raw CSV, samples and cleans it (parses timestamps, derives hour/day-of-week/weekend flags), and writes the result into a Postgres table.
- `bank fraud sql.sql` — SQL queries analyzing fraud rate by transaction type, amount, and other dimensions.
- `bank fraud.pbix` — Power BI report/dashboard built on the analysis.
- `Fraud_Analysis_Insights.docx` — written summary of findings and recommendations.
- `Bank Fraud.pdf` — exported report.
- `bank.csv` — **not included** in this repo (796 MB, exceeds GitHub's 100 MB file limit). Download the source dataset from Kaggle to reproduce locally.

## Key findings

- Overall fraud rate: **3.60%** (18,000 of 500,000 sampled transactions).
- Average fraud transaction amount ($360.90) is nearly identical to average legitimate amount ($359.26) — amount alone is not a reliable fraud signal in this dataset.
- Fraud rate is fairly flat across transaction type, hour of day, and day of week (roughly 3.2%–3.8% throughout), suggesting no single static attribute is strongly predictive — behavioral/velocity-based signals likely matter more.

Full write-up in `Fraud_Analysis_Insights.docx`.

## Reproducing locally

1. Download `bank.csv` from the Kaggle dataset above and place it in a `Bank Fraud/` subfolder.
2. Set your Postgres credentials as environment variables before running the loader:
   ```
   export DB_USER=postgres
   export DB_PASSWORD=your_password
   ```
3. Run `python data.py` to sample, clean, and load the data into Postgres.
4. Run the queries in `bank fraud sql.sql` against the `fraud` table.
