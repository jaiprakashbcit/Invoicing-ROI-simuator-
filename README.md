# Invoicing ROI Simulator — Initial Prototype (15-Minute Version)

## 🧩 Overview
This is a simple prototype of the **Invoicing ROI Simulator** that calculates cost savings, ROI, and payback for switching to automated invoicing.  
It includes a Flask backend API and a basic HTML frontend for quick testing.

## 🏗️ Architecture
- **Frontend:** Static HTML + JavaScript (fetch API)
- **Backend:** Flask (Python)
- **Database:** Planned (SQLite for future CRUD)
- **API:** `/simulate` endpoint for ROI calculations

## ⚙️ Tech Stack
- Python 3.10+
- Flask
- HTML, JavaScript, CSS
- SQLite (for next phase)

## 💡 Features
- Input key business parameters
- Compute ROI instantly
- Favorable (biased) automation results
- Ready for expansion with CRUD and reports

## 🚀 Run Locally
```bash
cd backend
pip install flask
python app.py
