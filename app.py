import pandas as pd
import streamlit as st
import plotly.express as px

# SCORING FUNCTION

def calculate_score(row):
    score = 0

    role_keywords = ["director", "head", "vp", "toxicology", "safety", "hepatic", "preclinical"]
    if any(word in row["Title"].lower() for word in role_keywords):
        score += 30

    if row["Funding_Stage"] in ["Series A", "Series B"]:
        score += 20

    if row["Uses_InVitro"] == "Yes":
        score += 15

    hubs = ["bengaluru", "bangalore", "hyderabad", "pune", "mumbai", "delhi", "gurugram"]
    if any(hub in row["Company_HQ"].lower() for hub in hubs):
        score += 10

    if row["Published_Recent_Paper"] == "Yes":
        score += 40

    if row["Conference_Participation"] == "Yes":
        score += 10

    if float(row["Tenure_Years"]) < 1:
        score += 5

    return min(score, 100)

# STREAMLIT APP

st.set_page_config(page_title="AI Lead Ranking Demo", layout="wide")
st.title("AI-Based Lead Generation & Ranking Tool (India Demo)")

st.write("""
This is a **demo prototype** for identifying and ranking biotech leads
based on role, funding, technology use, location, and scientific activity.
""")


data = {
    "Name": [
        "Dr. Ankit Sharma","Dr. Priya Nair","Rahul Mehta","Neha Verma",
        "Dr. Suresh Iyer","Amit Kulkarni","Dr. Kavita Rao","Rohit Singh"
    ],
    "Title": [
        "Director of Toxicology","Head of Preclinical Safety","Senior Scientist",
        "Junior Scientist","VP Safety Assessment","Principal Scientist",
        "Director – Hepatic Toxicology","Research Scientist"
    ],
    "Company": [
        "Biocon Research","Strand Life Sciences","Syngene International","StartupBio Labs",
        "Piramal Pharma Solutions","GVK BIO","Aragen Life Sciences","Sun Pharma Advanced Research"
    ],
    "Person_Location": [
        "Bengaluru KA","Bengaluru KA","Hyderabad TS","Pune MH",
        "Mumbai MH","Hyderabad TS","Bengaluru KA","Gurugram HR"
    ],
    "Company_HQ": [
        "Bengaluru KA","Bengaluru KA","Bengaluru KA","Pune MH",
        "Mumbai MH","Hyderabad TS","Bengaluru KA","Gurugram HR"
    ],
    "Funding_Stage": [
        "Series B","Series A","Series B","None","Series B","Series A","Series B","None"
    ],
    "Uses_InVitro": ["Yes","Yes","Yes","No","Yes","Yes","Yes","No"],
    "Published_Recent_Paper": ["Yes","Yes","No","No","Yes","No","Yes","Yes"],
    "Conference_Participation": ["Yes","Yes","Yes","No","Yes","No","Yes","No"],
    "Tenure_Years": [2,0.5,1.5,0.7,3,1,2,1.2],
    "LinkedIn": [
        "https://linkedin.com/in/ankitsharma",
        "https://linkedin.com/in/priyanair",
        "https://linkedin.com/in/rahulmehta",
        "https://linkedin.com/in/nehaverma",
        "https://linkedin.com/in/sureshiyer",
        "https://linkedin.com/in/amitkulkarni",
        "https://linkedin.com/in/kavitarrao",
        "https://linkedin.com/in/rohitsingh"
    ]
}

df = pd.DataFrame(data)


df["Probability_Score"] = df.apply(calculate_score, axis=1)
df = df.sort_values(by="Probability_Score", ascending=False)
df["Rank"] = range(1, len(df) + 1)


search = st.text_input("Search by location, company, or title")
if search:
    df = df[df.apply(lambda row: search.lower() in row.to_string().lower(), axis=1)]


def highlight_top(row):
    if row["Rank"] <= 3:
        return ['background-color: lightgreen']*len(row)
    else:
        return ['']*len(row)

st.subheader("Ranked Leads Table")
st.dataframe(df.style.apply(highlight_top, axis=1))


st.subheader("Probability Score Distribution")
fig = px.histogram(df, x="Probability_Score", nbins=10, title="Lead Score Distribution")
st.plotly_chart(fig, use_container_width=True)


st.download_button(
    "Download Ranked Leads CSV",
    df.to_csv(index=False),
    "ranked_leads.csv",
    "text/csv"
)
