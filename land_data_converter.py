# filename: land_data_converter.py

import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup
import io
import re

st.set_page_config(page_title="📋 Land Data Converter", layout="wide")
st.title("📋 Comprehensive Land Record Converter")

tab1, tab2 = st.tabs(["📂 Upload HTML File", "📋 Paste Raw Text"])

# --------------------- Tab 1: HTML File Upload --------------------- #
with tab1:
    st.header("📂 Upload HTML Land Record File")

    uploaded_file = st.file_uploader("Upload .htm or .html file", type=["htm", "html"])

    def parse_land_html(file):
        html_content = file.read().decode("utf-8", errors="ignore")
        soup = BeautifulSoup(html_content, "html.parser")
        rows = []

        tables = soup.find_all("table")
        if not tables:
            return pd.DataFrame()

        for table in tables:
            tr_elements = table.find_all("tr")
            if len(tr_elements) < 2:
                continue

            first_data_row = tr_elements[1].find_all("td")
            if len(first_data_row) >= 7:
                for tr in tr_elements[1:]:  # Skip header
                    tds = tr.find_all("td")
                    if len(tds) < 7:
                        continue

                    khewat = tds[0].text.strip()
                    marba = tds[1].text.strip()
                    killa_no = tds[6].text.strip()        # share → killa
                    kanal_raw = tds[3].text.strip()       # treated as owner
                    owner_field = tds[5].text.strip()     # owner + fraction

                    # Extract owner and fraction
                    owner_match = re.match(r"^(.*?)\s*\((.*?)\)$", owner_field)
                    if owner_match:
                        owner_name = owner_match.group(1).strip()
                        share_fraction = owner_match.group(2).strip()
                    else:
                        owner_name = owner_field
                        share_fraction = ""

                    if not owner_name and kanal_raw:
                        owner_name = kanal_raw

                    rows.append({
                        "Khewat No": khewat,
                        "Marba No": marba,
                        "Killa No": killa_no,
                        "Total Area (Kanals)": "",
                        "Total Area (Marlas)": "",
                        "Owner Name": owner_name,
                        "Share Fraction": share_fraction
                    })
                break

        return pd.DataFrame(rows)

    if uploaded_file:
        df = parse_land_html(uploaded_file)

        if not df.empty:
            st.success("✅ HTML parsed successfully!")
            st.dataframe(df, use_container_width=True)

            output = io.BytesIO()
            with pd.ExcelWriter(output, engine="openpyxl") as writer:
                df.to_excel(writer, index=False, sheet_name="Land Data")
            output.seek(0)

            st.download_button(
                label="📥 Download Excel File",
                data=output,
                file_name="converted_land_data.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        else:
            st.error("❌ No valid table found in the uploaded file.")

# --------------------- Tab 2: Paste-Based Parser --------------------- #
with tab2:
    st.header("📋 Parse Owner Blocks from Pasted Text")

    st.markdown("""
    Paste owner and share information below.
    Each group of owner lines must be followed by a share line (e.g., `603/3076 भाग`).
    Any lines like `वासी`, `हर दो समभाग` will be added as narration to the last name in the group.
    """)

    pasted_text = st.text_area("📤 Paste Raw Data Below", height=300)

    def parse_owner_blocks(text):
        lines = [line.strip().strip('"') for line in text.strip().splitlines() if line.strip()]
        result_rows = []
        current_names = []

        for line in lines:
            clean_line = re.sub(r'\s+', ' ', line).strip()

            if "भाग" in clean_line and re.search(r"\d+/\d+", clean_line):
                share_match = re.search(r"(\d+/\d+)", clean_line)
                share = share_match.group(1) if share_match else ""

                for name in current_names:
                    result_rows.append({
                        "Owner Name": name,
                        "Share Fraction": share
                    })

                current_names = []  # reset for next block
            else:
                if current_names:
                    current_names[-1] = f"{current_names[-1]} {clean_line}"
                else:
                    current_names.append(clean_line)

        # Handle any remaining names without share (optional)
        for name in current_names:
            result_rows.append({
                "Owner Name": name,
                "Share Fraction": ""
            })

        return pd.DataFrame(result_rows)

    if pasted_text:
        df_paste = parse_owner_blocks(pasted_text)

        if not df_paste.empty:
            st.success("✅ Parsed pasted data successfully!")
            st.dataframe(df_paste, use_container_width=True)

            output2 = io.BytesIO()
            with pd.ExcelWriter(output2, engine='openpyxl') as writer:
                df_paste.to_excel(writer, index=False, sheet_name='Pasted Data')
            output2.seek(0)

            st.download_button(
                label="📥 Download Excel File",
                data=output2,
                file_name="parsed_pasted_data.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        else:
            st.warning("⚠️ No data parsed.")
    else:
        st.info("⬆️ Paste data above to begin.")

