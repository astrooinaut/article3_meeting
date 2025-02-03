#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 11:58:13 2025

@author: donavanrooi
"""

import streamlit as st

# Title of the app
st.title("Article 3 Planning")

# Collect basic information
name = "Article 3"
field = "Determining the prognostic value of modifiable risk factors for arterial stiffness in vascular aging extremes"

# An image of longitudinal research
header_image = ""

# Display aims of the research
st.write(f"**Title:** {field}")

aim = "To determine the change over time of modifiable risk factors and cardiac structure and function between EVA and SUPERNOVA groups and to identify the strongest modifiable predictors of arterial stiffness and target organ damage in each group respectively."
st.write(f"**Aim:** {aim}")

# Create empty list for aims comments
comments_aims = []
# Comment on aims
new_comment_aims = st.text_area("Leave a comment about the aims here:")

# Save comments to a temp list
if st.button("Submit Aims Comment"):
    comments_aims.append(new_comment_aims)

with st.expander("Comments:"):
    for comment in comments_aims:
        st.markdown(f"- {comments_aims}")

# Assign objectives to a variable
objective1 = "To compare the 5-year change in modifiable risk factors between the EVA, AVA, and SUPERNOVA groups."
objective2 = "To compare the 5-year change in microvascular- and cardiac structure and function between the EVA, AVA, and SUPERNOVA groups."
objective3 = "3.	To determine the strongest predictors at baseline of PWV and microvascular and cardiac changes at follow-up within the EVA, AVA, and SUPERNOVA groups respectively."

# Write objectives
st.write(f"**Objective 1: ** {objective1}")
st.write(f"**Objective 2: ** {objective2}")
st.write(f"**Objective 3: ** {objective3}")

# Create empty list for objectives comments
comments_objectives = []

# Comment on objectives
new_comment_objectives = st.text_area("Leave a comment about the objectives here:")
if st.button("Submit Objectives Comment"):
    comments_objectives.append(new_comment_objectives)

with st.expander("Comments:"):
    for comment in comments_objectives:
        st.markdown(f"- {comments_objectives}")

# insert screenshot of chosen variables - maybe as code?
# add comments on variables

# insert statistical approach in detail - screenshot
# add comments for statistical approach

# Add a contact section
email = "27515230@mynwu.ac.za"
st.write(f"You can reach {name} at {email}.")