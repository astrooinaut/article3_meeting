#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 11:58:13 2025

@author: donavanrooi
"""

import os
import json
import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Load Google Service Account key from environment variable
json_key = os.getenv("mimetic-sweep-322719")
if json_key is None:
    st.error("Missing SECRET_JSON environment variable.")
    st.stop()

# Define Google Sheets scope
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

# Authenticate with Google Sheets
creds_dict = json.loads(json_key)
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(creds)
SHEET_NAME = "comments_test"
sheet = client.open(SHEET_NAME).sheet1

# --- Streamlit UI ---

# Page title
st.title("Article 3 Planning")

# Research Info
name = "Article 3"
field = "Determining the prognostic value of modifiable risk factors for arterial stiffness in vascular aging extremes"
aim = ("To determine the change over time of modifiable risk factors and cardiac structure and function between EVA and SUPERNOVA groups "
       "and to identify the strongest modifiable predictors of arterial stiffness and target organ damage in each group respectively.")

st.image("Tonometer.jpg")
st.write(f"**Title:** {field}")
st.write(f"**Aim:** {aim}")

# --- Commenting Section ---

def save_comment(comment_text, section):
    """Save a comment to Google Sheets with section label."""
    sheet.append_row([section, comment_text])

def load_comments(section):
    """Load comments by section from Google Sheets."""
    all_comments = sheet.get_all_values()
    return [row[1] for row in all_comments if row[0] == section]

# Comment 1: On aims
st.subheader("💬 Comment on Research Aim")
comment_aim = st.text_area("Your comment on the research aim:", key="comment_aim")

if st.button("Submit Aim Comment"):
    if comment_aim.strip():
        save_comment(comment_aim, "aim")
        st.success("Your comment has been saved.")
        st.rerun()

st.markdown("#### Previous Comments on Aim:")
for c in load_comments("aim"):
    st.write(f"- {c}")

# Objectives
objectives = [
    "To compare the 5-year change in modifiable risk factors between the EVA, AVA, and SUPERNOVA groups.",
    "To compare the 5-year change in cardiac structure and function between the EVA, AVA, and SUPERNOVA groups.",
    "To determine the strongest predictors at baseline of PWV and cardiac changes at follow-up within the EVA, AVA, and SUPERNOVA groups respectively."
]

st.subheader("📌 Objectives")
for i, obj in enumerate(objectives, 1):
    st.write(f"**Objective {i}:** {obj}")

# Comment 2: On objectives
comment_objectives = st.text_area("Your comment on the objectives:", key="comment_objectives")

if st.button("Submit Objective Comment"):
    if comment_objectives.strip():
        save_comment(comment_objectives, "objectives")
        st.success("Your comment has been saved.")
        st.rerun()

st.markdown("#### Previous Comments on Objectives:")
for c in load_comments("objectives"):
    st.write(f"- {c}")

# Table 1
st.subheader("📊 Table 1: Descriptives")
st.write("Draft table of descriptives")
st.image("Screenshot 2025-02-06 at 17.13.26.png")
comment_table1 = st.text_area("Your comment on Table 1:", key="comment_table1")

if st.button("Submit Table 1 Comment"):
    if comment_table1.strip():
        save_comment(comment_table1, "table1")
        st.success("Your comment has been saved.")
        st.rerun()

st.markdown("#### Previous Comments on Table 1:")
for c in load_comments("table1"):
    st.write(f"- {c}")

# Table 2
st.subheader("📊 Table 2: Hazard Ratios")
st.write("Draft table of hazard ratios")
comment_table2 = st.text_area("Your comment on Table 2:", key="comment_table2")

if st.button("Submit Table 2 Comment"):
    if comment_table2.strip():
        save_comment(comment_table2, "table2")
        st.success("Your comment has been saved.")
        st.rerun()

st.markdown("#### Previous Comments on Table 2:")
for c in load_comments("table2"):
    st.write(f"- {c}")

# Contact section
st.write("📧 **Contact:**")
st.write(f"You can reach {name} at [27515230@mynwu.ac.za](mailto:27515230@mynwu.ac.za)")
