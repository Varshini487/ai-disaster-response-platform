import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd
import numpy as np
from datetime import datetime

st.set_page_config(page_title="🚨 Disaster Response AI", layout="wide")
st.title("🚨 AI Disaster Response Platform")
st.markdown("Real-time disaster impact assessment using satellite, social media, and sensor fusion")

st.sidebar.header("⚙️ Data Inputs")
disaster_type = st.sidebar.selectbox("Disaster Type:", ["Flood", "Earthquake", "Wildfire", "Landslide"])
hours_since = st.sidebar.slider("Hours Since Event:", 0, 48, 4)

tab1, tab2, tab3 = st.tabs(["🛰️ Satellite Damage Map", "💬 Social Media Signals", "📊 Prioritization"])

with tab1:
    st.subheader("Satellite-Based Damage Assessment")
    
    m = folium.Map(location=[28.7041, 77.1025], zoom_start=11)
    
    damage_zones = {
        "High": (28.71, 77.11, "red"),
        "Moderate": (28.70, 77.10, "orange"),
        "Low": (28.69, 77.09, "yellow"),
    }
    
    for level, (lat, lon, color) in damage_zones.items():
        folium.CircleMarker(
            location=[lat, lon], radius=20, color=color, fill=True, fillColor=color,
            popup=f"{level} damage zone", tooltip=level
        ).add_to(m)
    
    st_folium(m, width=700, height=500)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("🔴 High Damage Zones", 3, "150+ buildings affected")
    col2.metric("🟠 Moderate Zones", 5, "30-150 buildings")
    col3.metric("🟡 Low Zones", 8, "<30 buildings")

with tab2:
    st.subheader("Social Media Intelligence (Live Streaming)")
    
    signals = [
        {"time": "09:15 AM", "location": "South District", "type": "Call for Help", "text": "Water rising fast! Trapped on roof!", "confidence": 0.95},
        {"time": "09:22 AM", "location": "Market St", "type": "Injury Report", "text": "Building collapsed, people under rubble", "confidence": 0.92},
        {"time": "09:31 AM", "location": "North Ward", "type": "Infrastructure", "text": "Bridge washed away", "confidence": 0.88},
        {"time": "09:45 AM", "location": "South District", "type": "Call for Help", "text": "Hospitals overwhelmed, need supplies", "confidence": 0.85},
    ]
    
    for sig in signals:
        if sig["type"] == "Call for Help":
            icon = "🆘"
        elif sig["type"] == "Injury Report":
            icon = "🚑"
        else:
            icon = "🏗️"
        
        st.write(f"{icon} **{sig['time']} — {sig['location']}** ({sig['confidence']:.0%} confidence)")
        st.caption(f""{sig['text']}"")

with tab3:
    st.subheader("Smart Relief Prioritization")
    
    priorities = pd.DataFrame({
        "Zone": ["South District", "Market St", "North Ward", "East Industrial", "West Residential"],
        "Damage %": [85, 72, 45, 30, 15],
        "Population Affected": [12000, 8500, 5600, 2200, 1100],
        "Recommended Action": ["🚁 Evacuation + Heavy Equipment", "🚑 Medical + Rescue Teams", "⛑️ Search & Rescue", "📦 Food & Water", "✅ Minor Support"],
        "Dispatch Priority": ["URGENT", "URGENT", "HIGH", "MEDIUM", "LOW"]
    })
    
    st.dataframe(priorities, use_container_width=True)
    
    st.markdown("### 📍 Estimated Relief Allocation")
    col1, col2, col3 = st.columns(3)
    col1.metric("Teams Deployed", 47, "+12 this hour")
    col2.metric("Medical Units", 8, "3 helicopter rescues active")
    col3.metric("Supplies Distributed", "240 tons", "Next: 60 tons South District")

st.markdown("---")
st.caption(f"Live update: {datetime.now().strftime('%H:%M:%S')} | Satellite updated 8 min ago | Social media live | Sensors 2 min lag")
