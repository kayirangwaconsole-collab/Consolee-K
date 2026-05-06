# 🌍 Conflict-Affected Regions Analysis

Analysis and visualization of conflict-affected regions in Sub-Saharan Africa, the Middle East, and South-East Asia.

## 📁 Project Structure

```
Consolee-K/
├── data/                              # CSV data files
│   ├── conflict_regions.csv           # Original dataset (19 countries)
│   └── filtered_conflict_regions.csv  # Filtered results (15 countries)
├── scripts/                           # Python scripts
│   └── filter_conflict_regions.py     # Script to filter regions
├── docs/                              # Web files (GitHub Pages)
│   └── conflict-map.html              # Interactive Leaflet map
└── README.md                          # This file
```

## 🚀 Quick Start

### View the Interactive Map
Open the live Education Intelligence map at:
```
https://kayirangwaconsole-collab.github.io/Consolee-K/
```

### Map Focus
This map supports the argument for **Building an Adaptive Education Intelligence System** by highlighting 15 priority conflict-affected regions with specific educational insights.

### Run the Filter Script
```bash
cd scripts/
python filter_conflict_regions.py
```

## 📊 Data Overview

**Total Countries:** 15

| Region | Countries | Count |
|--------|-----------|-------|
| 🔴 Sub-Saharan Africa | Nigeria, Somalia, South Sudan, Ethiopia, DRC, Cameroon | 6 |
| 🟠 Middle East | Syria, Yemen, Iraq, Lebanon | 4 |
| 🟡 South-East Asia | Myanmar, Philippines, Thailand, Laos, Cambodia | 5 |

## 🗺️ Interactive Map Features

- **Color-coded markers** by region
- **Click markers** to view country details
- **Hover effects** for better interactivity
- **Responsive design** for mobile and desktop
- **Modern dark theme** for better visibility

## 🛠️ Technologies Used

- **Frontend:** Leaflet.js, HTML/CSS
- **Data Processing:** Python, Pandas
- **Hosting:** GitHub Pages
- **Maps:** OpenStreetMap
