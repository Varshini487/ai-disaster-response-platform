# 🚨 AI Disaster Response Platform

A **real-time decision support platform** that fuses satellite imagery, social media, and IoT sensor data to rapidly assess disaster impact and intelligently prioritize relief efforts — turning hours of manual assessment into minutes of actionable intelligence.

## 🎯 Three Data Streams

### 1. Satellite Imagery Analysis
- Ingests pre/post-disaster satellite photos (Copernicus, Landsat)
- Deep learning model detects flooded areas, collapsed buildings, landslides
- Output: damage heatmap with severity levels

### 2. Social Media Signals
- Real-time scraping of Twitter/Reddit (tweets, posts from affected region)
- NLP classifier flags: calls for help, injury reports, infrastructure damage
- Clustering: identifies geographic hotspots (cluster of "water everywhere" tweets = flood epicenter)

### 3. IoT & Sensor Fusion
- Weather stations, seismic sensors, stream gauges feed live data
- Predictive model: "if rainfall continues, flooding will spread to Zone C in 4 hours"
- Real-time updates allow dynamic reallocation

## 🛠️ Tech Stack
- Python, TensorFlow (damage detection CNN)
- Tweepy/PRAW (social media APIs)
- GeoPandas (geospatial data)
- Folium (interactive maps)
- Streamlit (live dashboard)
- FastAPI (real-time API)

## 🚀 Getting Started
```bash
git clone https://github.com/Varshini487/ai-disaster-response-platform
cd ai-disaster-response-platform
pip install -r requirements.txt
streamlit run app.py
```

## 💡 3 Interview Talking Points

1. **Speed saves lives.** "In a flood, the first 2 hours are critical. Manual satellite analysis takes 6-8 hours. Our CNN damage classifier produces heatmaps in 5 minutes. Responders know 'South district needs boats NOW; North is passable.' This speed = faster evacuations, fewer casualties."

2. **Fusion beats single source.** "Satellite misses some damage (clouds, shadows). Social media is noisy (false reports). Sensors are sparse. Combined: satellite flags general area, social media pinpoints street-level hotspots, sensors predict spread. Ensemble > any single source."

3. **Fairness in allocation prevents aid bias.** "Without data, responders help visible/accessible zones first. Remote villages get nothing. Our platform maps hard-hit areas regardless of visibility. It's data-driven equity: every region gets help proportional to damage, not proximity to responders."
