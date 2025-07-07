# 📦 Inventory Stock Tracking System

A dynamic Streamlit web app to track and filter pharmaceutical inventory data.

## 🔧 Features
- Upload a cleaned inventory `.csv` file
- Filter by:
  - Movement status (Moved / Not Moved)
  - Search product name
  - Inward / Outward quantity
  - Out-of-stock products
  - Outward value range
  - Sort by value/quantity
- 🎯 Specific Product Selection with total sales summary
- Download filtered data

## ▶️ How to Run

```bash
pip install -r requirements.txt
streamlit run inventory_app.py
```

## 📤 Data Format Required

CSV file must contain these columns:
- Product Name
- Opening Qty, Rate, Value
- Inward Qty, Rate, Value
- Outward Qty, Rate, Value
- Closing Qty, Rate, Value
- Movement Status

Make sure **Grand Total row is removed or will be auto-filtered**.