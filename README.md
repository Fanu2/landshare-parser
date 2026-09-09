# 📐 Land Share & Ownership Calculator

A standalone **PySide6 desktop application** for calculating proportional ownership shares in land and converting the resulting area into the traditional:

**Killa → Kanal → Marla → Sarshai**

format.

This application is a desktop conversion of the original Streamlit-based Land Share Calculator, redesigned as a practical local utility with a richer interface, owner management, validation, import/export, presets, and clipboard-based table input.

---

## 1. Overview

Land records frequently express ownership as fractions or shares rather than as a directly stated physical area.

For example:

| Owner | Fraction / Share |
|---|---:|
| Owner A | 1/2 |
| Owner B | 1/4 |
| Owner C | 1/4 |

If the total holding is known, the application calculates each owner's proportional area.

The calculator performs three main tasks:

1. **Convert the total holding into Marla**
2. **Apply each owner's fractional/percentage share**
3. **Convert the resulting area back into Killa, Kanal, Marla and Sarshai**

The result is displayed in a structured ownership table.

---

# 2. Main Features

## 🧮 Total Area Calculator

The total holding is entered using:

- Kanal
- Additional Marla

The application internally converts this into total Marla.

For example:

```text
10 Kanal + 5 Marla

= (10 × 20) + 5
= 205 Marla
```

The total is displayed immediately.

---

## 👥 Multiple Owners

The ownership table supports any practical number of owner rows.

Each row contains:

- Owner name
- Fraction / Share
- Calculated share
- Total Marla Share
- Killa
- Kanal
- Marla
- Sarshai
- Combined result

Example:

```text
Owner A    1/2
Owner B    1/4
Owner C    1/4
```

The calculations update automatically when the inputs change.

---

# 3. Supported Share Formats

The calculator accepts several convenient formats.

## Fraction

Examples:

```text
1/2
1/4
3/16
5/32
7/128
```

A fraction is converted into its decimal equivalent.

For example:

```text
1/8 = 0.125
```

---

## Decimal

Decimal values are also accepted:

```text
0.5
0.25
0.125
0.0625
```

---

## Percentage

Percentage values can be entered directly:

```text
50%
25%
12.5%
6.25%
```

For example:

```text
25% = 0.25
```

---

# 4. Land Measurement Basis

The calculator uses the following conversion system:

```text
1 Kanal = 20 Marla

1 Killa = 8 Kanal

1 Killa = 160 Marla

1 Marla = 9 Sarshai
```

Therefore:

```text
1 Killa = 8 Kanal
         = 160 Marla
         = 1440 Sarshai
```

The smallest unit used internally for the final conversion is Sarshai.

This helps avoid unnecessary rounding errors when fractional Marla values are involved.

---

# 5. Calculation Method

Suppose:

```text
Total Area = 10 Kanal
Owner Share = 1/4
```

First the application converts the total area:

```text
10 Kanal × 20
= 200 Marla
```

Then applies the ownership fraction:

```text
200 × 1/4
= 50 Marla
```

The resulting 50 Marla is then converted into Killa/Kanal/Marla/Sarshai:

```text
50 Marla
= 2 Kanal + 10 Marla
```

The table therefore reports the physical area corresponding to that owner's share.

---

# 6. Ownership Validation

The application does more than calculate individual rows.

It also checks the total ownership allocation.

The ideal situation is:

```text
Total ownership = 1.0
```

or:

```text
100%
```

## Balanced

Example:

```text
1/2 + 1/4 + 1/4
= 1
= 100%
```

The application reports:

```text
BALANCED
```

---

## Partially Allocated

Example:

```text
1/2 + 1/4
= 3/4
= 75%
```

The application reports that:

```text
25% remains unallocated
```

This can be useful when entering only some of the owners from a larger holding.

---

## Over-Allocated

Example:

```text
1/2 + 1/2 + 1/4
= 1.25
= 125%
```

The application flags the data as:

```text
OVER-ALLOCATED
```

This is particularly useful for catching data-entry errors.

---

## Invalid Share

If a share cannot be interpreted, the row is marked as invalid and the application reports:

```text
CHECK INPUT
```

Examples of malformed values include:

```text
1/
abc
1/0
```

---

# 7. Dashboard Summary

At the top of the calculation workspace, three summary cards provide a quick overview.

### TOTAL AREA

Shows the complete holding in Marla.

Example:

```text
205 marla
```

### ALLOCATED

Shows the percentage represented by the entered owner shares.

Example:

```text
75.00%
```

### REMAINING

Shows the portion that has not yet been allocated.

Example:

```text
25.00%
```

These values update as the ownership table changes.

---

# 8. Owner Presets

The application includes convenient equal-ownership presets.

Available presets:

```text
Equal 2 owners
Equal 3 owners
Equal 4 owners
Equal 5 owners
Equal 8 owners
```

For example, selecting:

```text
Equal 4 owners
```

automatically creates:

```text
Owner 1    1/4
Owner 2    1/4
Owner 3    1/4
Owner 4    1/4
```

This is useful for quickly creating a starting ownership structure.

The **Custom** option allows complete manual control.

---

# 9. Adding and Removing Owners

## Add Owner

Use:

```text
＋ Add Owner
```

A new row is added to the table.

You can then enter:

```text
Owner name
Share
```

---

## Remove Owner

Select one or more table rows and use:

```text
− Remove Selected
```

The selected rows are removed and the calculation is immediately refreshed.

---

# 10. Paste Excel-Style Tables

The application supports direct clipboard input.

This is especially useful when data already exists in Excel.

For example, copy:

```text
Owners    Fraction / Share
Ram       1/2
Sham      1/4
Mohan     1/4
```

and use:

```text
Paste Table
```

The application reads the tab-separated clipboard contents and creates the owner rows automatically.

This avoids manually entering every row.

---

# 11. Excel Import

Use:

```text
📥 Import Excel / CSV
```

Supported formats:

```text
.xlsx
.xls
.csv
```

The importer looks for columns corresponding to:

```text
Owners
Fraction / Share
```

The column matching is deliberately tolerant of common variations containing:

```text
owner
fraction
share
```

After import, the application calculates the results automatically.

---

# 12. Export Results

Use:

```text
📤 Export Results
```

Supported output formats:

```text
.xlsx
.csv
```

## Excel Export

The Excel workbook contains:

```text
Land Share Results
```

with the calculated table.

The exported workbook also includes:

- Frozen header row
- Automatically sized columns
- Calculated ownership information

---

## CSV Export

CSV is useful for:

- Further spreadsheet processing
- Data exchange
- Archiving
- Import into other applications

---

# 13. Result Table

The calculation table contains the following columns:

| Column | Purpose |
|---|---|
| Owners | Owner/person name |
| Fraction / Share | Original entered share |
| Share | Normalized decimal share |
| Total Marla Share | Physical land corresponding to the share |
| Killa | Calculated Killa |
| Kanal | Calculated Kanal |
| Marla | Calculated Marla |
| Sarshai | Calculated Sarshai |
| Result | Combined human-readable result |

The final result has the form:

```text
0Ki-2K-10M-0S
```

meaning:

```text
0 Killa
2 Kanal
10 Marla
0 Sarshai
```

---

# 14. Example Calculation

Assume:

```text
Total land:
12 Kanal
```

Ownership:

```text
Owner A    1/2
Owner B    1/4
Owner C    1/4
```

### Step 1 — Total area

```text
12 × 20
= 240 Marla
```

### Step 2 — Owner A

```text
240 × 1/2
= 120 Marla
```

Therefore:

```text
120 Marla
= 6 Kanal
```

### Step 3 — Owner B

```text
240 × 1/4
= 60 Marla
```

Therefore:

```text
60 Marla
= 3 Kanal
```

### Step 4 — Owner C

```text
240 × 1/4
= 60 Marla
= 3 Kanal
```

### Ownership check

```text
1/2 + 1/4 + 1/4
= 1
= 100%
```

The holding is therefore balanced.

---

# 15. Typical Workflow

A normal calculation can be performed in a few steps.

### Step 1

Enter the total holding:

```text
Kanal
Marla
```

### Step 2

Add owners.

### Step 3

Enter each ownership fraction.

For example:

```text
1/2
1/4
1/4
```

### Step 4

Review the calculated physical areas.

### Step 5

Check the ownership status.

You want:

```text
BALANCED
```

when all ownership shares are expected to account for the complete holding.

### Step 6

Export the result if required.

---

# 16. Installation

The application requires Python and PySide6.

The supplied `requirements.txt` contains:

```text
PySide6
pandas
openpyxl
```

Install them with:

```powershell
pip install -r requirements.txt
```

Or:

```powershell
python -m pip install -r requirements.txt
```

---

# 17. Running the Application

From the application directory:

```powershell
python land_share_calculator.py
```

The application opens as a normal desktop window.

No web browser is required.

No Streamlit server is required.

---

# 18. Windows Usage

A typical Windows setup might look like:

```text
Land_Share_Ownership_Calculator\
│
├── land_share_calculator.py
├── requirements.txt
└── README.md
```

Open PowerShell in the directory and run:

```powershell
python land_share_calculator.py
```

If Python is installed through the Python launcher, this can also be:

```powershell
py land_share_calculator.py
```

---

# 19. Linux Usage

Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Run:

```bash
python3 land_share_calculator.py
```

The application is designed to work with PySide6 on Linux as well as Windows.

---

# 20. Why PySide6 Instead of Streamlit?

The original application was written using Streamlit, which is excellent for rapidly building browser-based data applications.

This version is intentionally a desktop application.

### Streamlit version

```text
Python
   ↓
Streamlit
   ↓
Web application
   ↓
Browser
```

### PySide6 version

```text
Python
   ↓
PySide6
   ↓
Native desktop application
```

The PySide6 version provides:

- Native desktop workflow
- No browser dependency
- No local web server
- More control over keyboard/mouse interaction
- Better foundation for future desktop tools
- Easier integration with other local utilities
- More suitable for an offline calculation workstation

---

# 21. Data Privacy

The application is designed as a local utility.

The calculations are performed locally by Python.

There is no requirement for:

- Internet access
- Cloud storage
- Remote database
- Web server

Imported files are read locally and exported locally.

---

# 22. Data Handling

The application does not require a permanent database.

The current design is intentionally simple:

```text
Input
 ↓
Calculation
 ↓
Result table
 ↓
Optional export
```

This makes the application easy to understand, maintain and move between computers.

---

# 23. Technical Architecture

The application currently uses a compact architecture.

```text
land_share_calculator.py
        │
        ├── Input / UI
        │
        ├── Share Parser
        │
        ├── Area Conversion
        │
        ├── Ownership Validation
        │
        ├── Table Management
        │
        └── Import / Export
```

### Share Parser

Responsible for interpreting:

```text
1/8
0.125
12.5%
```

### Area Conversion

Responsible for:

```text
Marla
    ↓
Sarshai
    ↓
Killa / Kanal / Marla / Sarshai
```

### Ownership Validation

Responsible for determining:

```text
Balanced
Partial
Over-allocated
Invalid
```

### Import / Export

Uses:

```text
pandas
openpyxl
```

for spreadsheet interoperability.

---

# 24. Error Handling

The application handles common input problems without crashing.

Examples include:

- Invalid fraction
- Division by zero
- Missing required spreadsheet columns
- Invalid spreadsheet format
- Empty clipboard
- Failed file import
- Failed file export

Errors are presented through the desktop interface.

---

# 25. Important Interpretation Note

This application performs **mathematical proportional allocation**.

It does not determine:

- Legal ownership
- Title
- Mutation entitlement
- Inheritance entitlement
- Revenue-record corrections
- Partition validity
- Court-determined rights
- Applicable local revenue rules

For an actual land transaction, inheritance matter, partition, mutation, or revenue-record issue, the calculated result should be checked against the applicable official record and relevant legal/revenue requirements.

---

# 26. Limitations of the Current Version

The current version intentionally focuses on calculation rather than becoming a complete land-record management system.

It does not currently provide:

- Jamabandi record parsing
- Khewat management
- Khatoni management
- Khasra/parcel management
- Mutation management
- Inheritance-rule calculation
- Legal heir determination
- Partition history
- Revenue-record OCR
- Village/master-data management
- Database persistence

Those are separate concerns and can be added later if there is a clear requirement.

---

# 27. Future Development Possibilities

The calculator provides a useful foundation for more advanced land tools.

Possible future additions include:

## V2 — Advanced Ownership Workspace

- Owner grouping
- Share normalization
- Share comparison
- Multiple holdings
- Copy/paste between holdings
- Calculation history
- Undo/redo

## V3 — Jamabandi-Oriented Input

Potential fields:

```text
Village
Year
Khewat
Khatoni
Khasra
Owner
Share
Area
```

The calculation engine could then operate directly on structured Jamabandi data.

## V4 — Ownership Statement

Generate a formatted ownership statement such as:

```text
Total Holding
-------------------------
Killa   Kanal   Marla

Owner 1
-------------------------
Share
Area

Owner 2
-------------------------
Share
Area
```

## V5 — Document Generation

Potential outputs:

- Excel report
- CSV
- PDF
- Printable ownership statement

---

# 28. Design Philosophy

The application follows a simple principle:

> **Keep the calculation engine simple, transparent and independently useful.**

The calculation should be understandable without depending on a large land-record system.

That makes this application useful as:

- A standalone calculator
- A verification tool
- A spreadsheet companion
- A development component for larger revenue applications

---

# 29. Project Structure

```text
Land_Share_Ownership_Calculator/
│
├── land_share_calculator.py
│       Main PySide6 application
│
├── requirements.txt
│       Python dependencies
│
└── README.md
        Documentation
```

---

# 30. Quick Reference

### Area conversion

```text
1 Killa  = 8 Kanal
1 Kanal  = 20 Marla
1 Marla  = 9 Sarshai
```

### Total area

```text
Total Marla =
(Kanal × 20) + Additional Marla
```

### Owner area

```text
Owner Area =
Total Marla × Owner Share
```

### Balanced ownership

```text
Σ Owner Shares = 1.0
```

or:

```text
Σ Owner Shares = 100%
```

---

# 31. Example Input Table

The following can be copied from Excel and pasted into the application:

```text
Owners	Fraction / Share
Owner A	1/2
Owner B	1/4
Owner C	1/4
```

Set the total area, then select **Paste Table**.

The calculator will populate and calculate the rows.

---

# 32. Project Status

**Current release:** Initial PySide6 desktop release

The application is intended to be a focused and maintainable calculation utility rather than an unnecessarily large land-management system.

The current feature set provides the core workflow:

```text
Total Area
     ↓
Owner Shares
     ↓
Validation
     ↓
Physical Area
     ↓
Killa/Kanal/Marla/Sarshai
     ↓
Excel / CSV
```

---

## License

Add the project's preferred license here before publishing the repository.

---

## Author / Repository

Add the project's GitHub repository and author information here when the repository is created or published.
