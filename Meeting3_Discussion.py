#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 11:58:13 2025

@author: donavanrooi
"""

import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
        
# Google Sheets authentication
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("mimetic-sweep-322719-1c455a049c9b.json", scope)
client = gspread.authorize(creds)

SHEET_NAME = "comments_test"
sheet = client.open(SHEET_NAME).sheet1

# Title of the app
st.title("Article 3 Planning")

# Article Title
name = "Article 3"
field = "Determining the prognostic value of modifiable risk factors for arterial stiffness in vascular aging extremes"

# An image of longitudinal research
st.image("Tonometer.jpg")

# Display aims of the research
st.write(f"Title: {field}")

aim = "To determine the change over time of modifiable risk factors and cardiac structure and function between EVA and SUPERNOVA groups and to identify the strongest modifiable predictors of arterial stiffness and target organ damage in each group respectively."
st.write(f"Aim: {aim}")

comment = st.text_area("Write your comment about the aims:")

# Function to save comment
def save_comment(comment):
    sheet.append_row([comment])

# Function to load comments
def load_comments():
    return sheet.col_values(1)  # Get all comments from column A

if st.button("Submit Comment"):
    if comment:
        save_comment(comment)
        st.success("Comment saved!")
        st.rerun()

# Display all comments
st.write("### Comments:")
for c in load_comments():
    st.write(f"- {c}")

# Assign objectives to a variable
objective1 = "To compare the 5-year change in modifiable risk factors between the EVA, AVA, and SUPERNOVA groups."
objective2 = "To compare the 5-year change in cardiac structure and function between the EVA, AVA, and SUPERNOVA groups."
objective3 = "To determine the strongest predictors at baseline of PWV and cardiac changes at follow-up within the EVA, AVA, and SUPERNOVA groups respectively."

# Write objectives
st.write(f"Objective 1: {objective1}")
st.write(f"Objective 2: {objective2}")
st.write(f"Objective 3: {objective3}")

comment = st.text_area("Write your comment about the objectives:")

# Add a table describing how aim 1 and 2 will be answered
Table_1 = "Draft table of descriptives"
st.write(f"Table 1: {Table_1}")

st.image("Screenshot 2025-02-06 at 17.13.26.png")

comment = st.text_area("Write your comment about table 1:")

# Add a table describing how aim 3 will be answered
Table_2 = "Draft table of hazard ratios"
st.write(f"Table 2: {Table_2}")

comment = st.text_area("Write your comment about table 2:")

# insert statistical approach in detail - screenshot
# add comments for statistical approach

# Add a contact section
email = "27515230@mynwu.ac.za"
st.write(f"You can reach {name} at {email}.")
