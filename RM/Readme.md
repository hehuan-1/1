# COMP4037 Coursework 2: Data Visualization

This repository contains a complete solution for Coursework 2 of COMP4037 - Research Methods, with a focus on advanced data visualization using Python.

##  Project Summary

We analyze the environmental impact of different diet types using a large-scale dataset derived from research at Oxford University. The dataset includes various ecological indicators linked to consumer dietary habits.

##  Visualization Approach

A **Radar Chart** (Spider Plot) is used to display and compare the normalized environmental burden of different diet groups:

- Vegan
- Vegetarian
- Fish-eater
- Meat-eater

The environmental indicators visualized include:

- Greenhouse gas emissions
- Land usage
- Water scarcity
- Eutrophication potential
- CH₄ (Methane) emissions
- N₂O (Nitrous Oxide) emissions
- Biodiversity loss
- Water usage
- Acidification potential

##  Data Processing Pipeline

1. Load and clean dataset
2. Drop rows with missing values
3. Normalize all environmental indicators using Min-Max Scaling
4. Create a composite environmental score (sum of normalized indicators)
5. Group by `diet_group` and calculate mean scores
6. Plot radar chart using `matplotlib`
7. Automatically save the chart to `images/diet_radar_chart.png` and display it

##  Project Structure

```
.
├── data/
│   └── Results_21MAR2022_nokcaladjust.csv
├── images/
│   └── diet_radar_chart.png
├── COMP4037_CW2_Visualization_Report.docx
├── radar_visualization.py
└── README.md
```

##  Key Insights

- **Vegan** diets have the lowest environmental burden across all metrics.
- **Meat-eaters** show the highest impact, particularly in CH₄ emissions, biodiversity loss, and water use.
- **Fish-eaters** surprisingly show higher water scarcity and eutrophication compared to vegetarians.

##  Technologies Used

- Python 3
- pandas
- scikit-learn
- matplotlib

##  License

For academic use only as part of COMP4037 coursework.

---

Created by Kaiyi Zheng
