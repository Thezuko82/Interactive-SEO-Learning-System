import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import graphviz
import networkx as nx
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Interactive SEO Learning Dashboard",
    layout="wide"
)

st.title("🔍 Interactive SEO Learning System")
st.markdown("Learn SEO through interactive visualizations, flowcharts, simulations, and dashboards.")

# ==================================================
# SIDEBAR
# ==================================================

topic = st.sidebar.radio(
    "Select Topic",
    [
        "Search Engine Working Process",
        "Keyword Research",
        "Competitor Analysis",
        "On-Page SEO",
        "Technical SEO",
        "SEO Audit",
        "Local SEO",
        "Link Building",
        "SEO Reporting"
    ]
)

# ==================================================
# 1 SEARCH ENGINE PROCESS
# ==================================================

if topic == "Search Engine Working Process":

    st.header("Search Engine Working Process")

    st.subheader("Flowchart")

    dot = graphviz.Digraph()

    dot.node("A", "Website")
    dot.node("B", "Crawler")
    dot.node("C", "Indexer")
    dot.node("D", "Ranking Algorithm")
    dot.node("E", "Search Results")

    dot.edge("A", "B")
    dot.edge("B", "C")
    dot.edge("C", "D")
    dot.edge("D", "E")

    st.graphviz_chart(dot)

    st.subheader("Interactive Search Engine Simulator")

    pages = st.slider("Number of Pages Crawled", 0, 1000, 500)

    indexed = int(pages * 0.85)

    ranked = int(indexed * 0.9)

    col1, col2, col3 = st.columns(3)

    col1.metric("Crawled", pages)
    col2.metric("Indexed", indexed)
    col3.metric("Ranked", ranked)

# ==================================================
# 2 KEYWORD RESEARCH
# ==================================================

elif topic == "Keyword Research":

    st.header("Keyword Research Tool")

    keyword = st.text_input("Keyword", "SEO")

    volume = st.slider("Search Volume", 100, 100000, 10000)
    difficulty = st.slider("Keyword Difficulty", 1, 100, 50)

    opportunity = volume / difficulty

    st.metric("Opportunity Score", round(opportunity,2))

    df = pd.DataFrame({
        "Keyword":[
            keyword,
            keyword+" course",
            keyword+" tutorial",
            keyword+" training",
            "best "+keyword
        ],
        "Volume":[
            volume,
            volume*0.7,
            volume*0.5,
            volume*0.4,
            volume*0.3
        ]
    })

    fig = px.bar(
        df,
        x="Keyword",
        y="Volume",
        title="Keyword Opportunities"
    )

    st.plotly_chart(fig,use_container_width=True)

# ==================================================
# 3 COMPETITOR ANALYSIS
# ==================================================

elif topic == "Competitor Analysis":

    st.header("Competitor Analysis Dashboard")

    competitors = pd.DataFrame({
        "Website":["You","Competitor A","Competitor B"],
        "Keywords":[120,350,280],
        "Backlinks":[900,3000,2200],
        "Traffic":[4000,18000,13000]
    })

    st.dataframe(competitors)

    fig = px.bar(
        competitors,
        x="Website",
        y=["Keywords","Backlinks","Traffic"],
        barmode="group"
    )

    st.plotly_chart(fig,use_container_width=True)

# ==================================================
# 4 ON PAGE SEO
# ==================================================

elif topic == "On-Page SEO":

    st.header("On-Page SEO Optimizer")

    title = st.text_input("Page Title")
    description = st.text_area("Meta Description")

    score = 0

    if 30 <= len(title) <= 60:
        score += 50

    if 120 <= len(description) <= 160:
        score += 50

    st.progress(score/100)

    st.metric("SEO Score", score)

    radar = go.Figure()

    radar.add_trace(go.Scatterpolar(
        r=[score,80,90,70],
        theta=['Title','Description','Keywords','Headings'],
        fill='toself'
    ))

    radar.update_layout(
        polar=dict(radialaxis=dict(visible=True)),
        showlegend=False
    )

    st.plotly_chart(radar)

# ==================================================
# 5 TECHNICAL SEO
# ==================================================

elif topic == "Technical SEO":

    st.header("Technical SEO Assessment")

    mobile = st.checkbox("Mobile Friendly")
    ssl = st.checkbox("HTTPS")
    sitemap = st.checkbox("XML Sitemap")
    robots = st.checkbox("Robots.txt")
    speed = st.checkbox("Fast Loading")

    score = sum([mobile,ssl,sitemap,robots,speed])*20

    st.metric("Technical SEO Score",score)

    st.progress(score/100)

# ==================================================
# 6 SEO AUDIT
# ==================================================

elif topic == "SEO Audit":

    st.header("SEO Audit Checklist")

    items = [
        "Title Tags",
        "Meta Description",
        "Page Speed",
        "Mobile Friendly",
        "Broken Links",
        "Backlinks",
        "Structured Data",
        "Sitemap"
    ]

    completed = 0

    for item in items:
        if st.checkbox(item):
            completed += 1

    percentage = completed/len(items)

    st.metric("Audit Completion",f"{percentage*100:.1f}%")

    st.progress(percentage)

# ==================================================
# 7 LOCAL SEO
# ==================================================

elif topic == "Local SEO":

    st.header("Local SEO & Google Business Profile")

    reviews = st.slider("Number of Reviews",0,500,50)

    rating = st.slider("Average Rating",1.0,5.0,4.2)

    visibility = reviews*0.6 + rating*20

    st.metric("Local Visibility Score",round(visibility))

    df = pd.DataFrame({
        "Factor":["Reviews","Rating","Photos","Posts"],
        "Score":[reviews/5,rating*20,70,60]
    })

    fig = px.pie(
        df,
        names="Factor",
        values="Score"
    )

    st.plotly_chart(fig)

# ==================================================
# 8 LINK BUILDING
# ==================================================

elif topic == "Link Building":

    st.header("Link Building Network")

    G = nx.Graph()

    G.add_edges_from([
        ("Your Site","Blog 1"),
        ("Your Site","Blog 2"),
        ("Your Site","Directory"),
        ("Blog 1","Authority Site"),
        ("Blog 2","Authority Site")
    ])

    fig, ax = plt.subplots(figsize=(8,5))

    nx.draw(
        G,
        with_labels=True,
        node_size=2500,
        ax=ax
    )

    st.pyplot(fig)

    backlinks = st.slider("Backlinks",0,500,100)

    st.metric("Authority Growth",round(backlinks*0.08,2))

# ==================================================
# 9 SEO REPORTING
# ==================================================

elif topic == "SEO Reporting":

    st.header("SEO Reporting Dashboard")

    months = ['Jan','Feb','Mar','Apr','May','Jun']

    traffic = [1000,1400,1900,2500,3200,4100]

    keywords = [30,50,80,110,150,200]

    report = pd.DataFrame({
        "Month":months,
        "Traffic":traffic,
        "Keywords":keywords
    })

    st.dataframe(report)

    fig1 = px.line(
        report,
        x="Month",
        y="Traffic",
        markers=True,
        title="Organic Traffic Growth"
    )

    st.plotly_chart(fig1,use_container_width=True)

    fig2 = px.line(
        report,
        x="Month",
        y="Keywords",
        markers=True,
        title="Keyword Ranking Growth"
    )

    st.plotly_chart(fig2,use_container_width=True)

    st.success("SEO Reports help track growth and ROI.")