# ⚡ Project Documentation: India Electricity Consumption Analysis (COVID-19 Impact)

## 📖 1. Project Overview
This project provides an end-to-end data engineering and visualization solution to analyze the shift in India's power consumption before, during, and after the 2020 COVID-19 lockdowns. The analysis tracks the transition from a pre-pandemic baseline through the industrial shutdown and maps the subsequent economic recovery across different states and geographic regions.

**🛠️ Tech Stack:** * **Data Processing:** 🐍 Python (Pandas)
* **Database:** 🗄️ MySQL 8.0
* **Visualization:** 📊 Tableau Public
* **Frontend UI:** 🌐 Flask (Python), HTML, Tailwind CSS

---

## 🚀 2. Step-by-Step Development Procedure

### 📥 Phase 1: Data Collection & Extraction
* **Dataset Acquisition:** Sourced a comprehensive time-series dataset detailing daily state-wise power consumption (in Mega Units) from 2013 to 2024.
* **Timeline Definition:** Isolated the project scope to focus strictly on the period between January 1, 2019, and December 5, 2020, to capture the complete pre-lockdown, strict lockdown, and recovery phases.

### 🧹 Phase 2: Data Preparation (ETL Process)
* **Data Transformation:** Developed a Python script utilizing the Pandas library to clean the raw dataset.
* **Dimensional Remodeling:** Converted the dataset from a "wide" format (states as individual columns) to a "long" format (Dates, State, Consumption) using the `pd.melt()` function to make it compatible with relational databases and BI mapping tools.
* **Data Standardization:** Standardized anomalous geographic data strings (e.g., mapping "Pondy" to "Puducherry" and combining "DNH" and "DD") to align with standard geographic coordinate systems.

### 💾 Phase 3: Database Storage & SQL Operations
* **Schema Creation:** Engineered a normalized relational database schema (`electricity_final`) in MySQL to handle high-volume time-series data.
* **Data Ingestion:** Executed high-speed bulk data imports, successfully loading over 23,000+ records.
* **SQL Analytics:** Performed validation queries utilizing aggregate functions (`SUM`, `GROUP BY`, `BETWEEN`) to verify regional consumption drops during the April 2020 lockdown period.

### 📈 Phase 4: Tableau Data Visualization
* **Data Connection:** Linked the cleaned dataset to Tableau and assigned correct Geographic Roles (State/Province) to generate spatial maps of India.
* **Calculated Fields:** Programmed custom logical fields to segment the data:
  * **Lockdown Phase:** An `IF-ELSE` statement categorizing dates into Pre-Lockdown, Lockdown, and Recovery.
  * **Region Group:** A geographic mapping field grouping 30+ individual states into 5 main regions (Northern, Southern, Eastern, Western, North-Eastern).
* **Unique Visualizations:** Designed three core analytical charts:
  * **Scenario 1 (National Trend):** A time-series Area Chart visualizing the massive dip in national power usage from March to June 2020.
  * **Scenario 2 (Regional Variations):** A stacked Bar Chart highlighting which industrial sectors (e.g., Western vs. Northern India) experienced the sharpest declines.
  * **Scenario 3 (Recovery):** A choropleth Map of India comparing pre-pandemic baselines to late-2020 usage to prove economic recovery.

### 🎬 Phase 5: Dashboarding & Storytelling
* **Responsive Design:** Assembled the three visualizations into a unified, responsive dashboard precisely sized at 1200x800 pixels for web embedding.
* **Interactive Filtering:** Implemented cross-dashboard filter actions, allowing users to click on a specific state on the map to dynamically update the corresponding trend lines and regional metrics.
* **Data Storytelling:** Constructed a 3-scene Tableau Story to guide the viewer chronologically through the data narrative: The Crash, The Regional Divide, and The Recovery.

### 💻 Phase 6: Web Integration (Flask)
* **Application Architecture:** Built a lightweight Python web server using the Flask framework to host the final analysis.
* **UI/UX Design:** Engineered a modern, "SaaS-style" frontend utilizing Tailwind CSS. The design features a dark-mode cyberpunk aesthetic, glassmorphism UI cards, and dynamic KPI trackers.
* **Embed Implementation:** Seamlessly integrated the 1200x800 Tableau Story into the center of the web application, ensuring a zero-gap, interactive user experience directly from the browser.

---

## ⏱️ 3. Performance Testing Metrics
To ensure the solution was robust and scalable, the following metrics were recorded during the testing phase:

* **Amount of Data Rendered to DB:** 23,000+ individual daily consumption records.
* **Number of Unique Visualizations/Graphs:** 3 highly customized charts (Area, Bar, Map).
* **Number of Calculation Fields:** 3 custom fields (Lockdown Phase, Region Group, % Change in Consumption).
* **Utilization of Data Filters:** Dynamic, dashboard-wide date sliders and action-based geographic filters were successfully implemented without latency.