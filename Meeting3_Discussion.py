#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 11:58:13 2025

@author: donavanrooi
"""

import streamlit as st

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

# Create empty list for aims comments
comments_aims = []
# Comment on aims
new_comment_aims = st.text_area("Leave a comment about the title and aims here:")

# Save comments to a temp list
if st.button("Submit Aims Comment"):
    comments_aims.append(new_comment_aims)

with st.expander("Comments:"):
    for comment in comments_aims:
        st.markdown(f"- {comments_aims}")

# Assign objectives to a variable
objective1 = "To compare the 5-year change in modifiable risk factors between the EVA, AVA, and SUPERNOVA groups."
objective2 = "To compare the 5-year change in cardiac structure and function between the EVA, AVA, and SUPERNOVA groups."
objective3 = "To determine the strongest predictors at baseline of PWV and cardiac changes at follow-up within the EVA, AVA, and SUPERNOVA groups respectively."

# Write objectives
st.write(f"Objective 1: {objective1}")
st.write(f"Objective 2: {objective2}")
st.write(f"Objective 3: {objective3}")

# Create empty list for objectives comments
comments_objectives = []

# Comment on objectives
new_comment_objectives = st.text_area("Leave a comment about the objectives here:")
if st.button("Submit Objectives Comment"):
    comments_objectives.append(new_comment_objectives)

with st.expander("Comments:"):
    for comment in comments_objectives:
        st.markdown(f"- {comments_objectives}")

# Add a table describing how aim 1 and 2 will be answered
Table_1 = "Draft table of descriptives"
st.write(f"Table 1: {Table_1}")

st.image("Table_1.png")

comments_table_1 = []

# Comment on table 1
new_comment_table_1 = st.text_area("Leave a comment about Table 1 here:")
if st.button("Submit Table 1 Comment"):
    comments_table_1.append(new_comment_table_1)

with st.expander("Comments:"):
    for comment in comments_table_1:
        st.markdown(f"- {comments_table_1}")

# Add a table describing how aim 3 will be answered
Table_2 = "Draft table of hazard ratios"
st.write(f"Table 2: {Table_2}")

comments_table_2 = []

new_comment_table_2 = st.text_area("Leave a comment about Table 2 here:")
if st.button("Submit Table 2 Comment"):
    comments_table_2.append(new_comment_table_2)

with st.expander("Comments:"):
    for comment in comments_table_2:
        st.markdown(f"- {comments_table_2}")


# insert statistical approach in detail - screenshot
# add comments for statistical approach

# Add a contact section
email = "27515230@mynwu.ac.za"
st.write(f"You can reach {name} at {email}.")
