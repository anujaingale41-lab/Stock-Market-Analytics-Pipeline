# Stock Market Analytics Pipeline

An end-to-end **data engineering pipeline** that ingests stock market data, processes it, and stores it in a scalable cloud-based data lake (AWS S3), with an API trigger and testing layer.

---

#  Overview

This project demonstrates how to build a **modular data pipeline** using Python, following industry best practices such as:

* Layered architecture (Ingestion → Transformation → Loading)
* Cloud storage (AWS S3)
* API-triggered pipeline execution
* Data validation and cleaning
* Unit testing with pytest

---

# Architecture

```
Client Request
     ↓
Flask API (app.py)
     ↓
Pipeline Runner (run_pipeline.py)
     ↓
Ingestion → Transformation → Loading
     ↓
AWS S3 (Data Lake)
```

---

# Tech Stack

* **Python**
* **Pandas**
* **AWS S3 (boto3)**
* **Flask (API layer)**
* **Pytest (testing)**
* **dotenv (environment variables)**

---

# Project Structure

```
Stock-Market-Analytics-Pipeline/
│
├── src/
│   ├── ingestion/         # Fetch stock data
│   ├── transformation/    # Clean & validate data
│   ├── loading/           # Upload to S3
│   ├── pipeline/          # Orchestration logic
│   └── utils/             # Logging (optional)
│
├── tests/                 # Unit tests
├── app.py                 # API trigger
├── config.py              # Configurations
├── models.py              # Database models (optional)
├── requirements.txt
├── README.md
└── .env                   # Environment variables (not committed)
```

---

# Pipeline Flow

1. **Ingestion**

   * Fetches stock data via API
   * Example: AAPL, TSLA

2. **Transformation**

   * Cleans raw data
   * Converts data types
   * Removes invalid records

3. **Loading**

   * Stores processed data in AWS S3
   * Partitioned by date:

   ```
   stock-data/date=YYYY-MM-DD/data.csv
   ```

---

# AWS S3 Integration

* Data is stored in a structured format for scalability
* Example path:

```
s3://your-bucket-name/stock-data/date=2026-05-04/data.csv
```

---

# Running Tests

```bash
pytest
```

Tests cover:

* Data ingestion
* Data transformation
* Pipeline execution

---

#  How to Run

## 1. Clone repo

```bash
git clone https://github.com/your-username/Stock-Market-Analytics-Pipeline.git
cd Stock-Market-Analytics-Pipeline
```

---

## 2. Create virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Setup environment variables

Create `.env` file:

```
AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
AWS_REGION=ap-south-1
```

---

## 5. Run pipeline

```bash
python -m src.pipeline.run_pipeline
```

---

## 6. Run via API (optional)

```bash
flask run
```

Then open:

```
http://127.0.0.1:5000/fetch?symbol=AAPL
```

---

# Key Features

* Modular pipeline architecture
* Cloud data storage (S3)
* API-triggered execution
* Data validation and cleaning
* Test coverage with pytest
* Scalable and extensible design

---

#  Author

**Anuja Ingale**
Aspiring Data Engineer | Data Analyst

---

#  Summary

This project demonstrates the transition from:

* Script-based data processing 
  to
* Scalable, modular data engineering pipeline 
