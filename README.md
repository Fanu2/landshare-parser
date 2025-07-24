# 📋 Land Record Converter – HTML & Text to Excel

This Streamlit app helps convert **Indian land record data** from either:

- 📂 **Uploaded HTML files** (with land ownership tables), **or**
- 📋 **Pasted unstructured text** (owner names and share fractions)

…into a clean, editable **Excel spreadsheet** format.

---

## 🚀 Features

### 🔹 Tab 1: HTML File Upload
- Upload `.html` or `.htm` land record files.
- Automatically extracts:
  - Khewat No
  - Marba No
  - Killa No (parsed from "Share Fraction" column)
  - Owner Name (parsed and cleaned)
  - Share Fraction (extracted from brackets)
- Download result as Excel (`.xlsx`).

### 🔹 Tab 2: Paste Raw Text
- Paste copied land share text (e.g. from PDFs or printouts).
- Parses:
  - Owner Names
  - Narration (like वासी or दत्तक पुत्र)
  - Share Fractions (e.g. `603/3076 भाग`)
- Outputs structured table ready for Excel download.

---

## 📥 Sample Input Formats

### Example Pasted Text:

