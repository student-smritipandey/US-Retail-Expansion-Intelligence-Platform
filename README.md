# US Retail Expansion Intelligence Platform
## 📌 Project Overview

The US Retail Expansion Intelligence Platform is a data-driven business intelligence solution designed to identify the most promising locations for retail expansion across the United States.

By combining demographic, economic, and competitor datasets, the project helps answer a critical business question:

"Which US counties offer the highest potential for opening a new retail store while minimizing competitive pressure and maximizing customer demand?"

The solution leverages Python, Pandas, Feature Engineering, Data Modeling, and Power BI to transform raw public datasets into actionable expansion insights.

 ## Project Objective

Develop a decision-support system that evaluates US counties based on:

Market Size
Purchasing Power
Economic Stability
Competitor Presence

and ranks counties according to their retail expansion potential.

# 🗂 Datasets Used
1. US County Population Data

Source: US Census Population Estimates

Purpose:

Estimate market size
Measure customer base potential

Key Metric:

Population_2023
2. Educational Attainment Data

Source: USDA Economic Research Service

Purpose:

Proxy for purchasing power
Consumer sophistication indicator

Key Metric:

% Adults with Bachelor's Degree or Higher (2019–2023)
3. Unemployment Data

Source: USDA Economic Research Service

Purpose:

Measure economic health
Estimate consumer spending capacity

Key Metric:

Unemployment Rate (2023)
4. Starbucks Store Locations

Source: Kaggle

Purpose:

Measure retail attractiveness
Estimate market demand

Key Metric:

Starbucks Store Count
5. Walmart Store Locations

Source: Kaggle

Purpose:

Measure competitor concentration
Estimate retail saturation

Key Metric:

Walmart Store Count
⚙️ Data Engineering & Preparation
Population Data Processing
Steps Performed
Filtered county-level population estimates
Removed national-level records
Standardized county identifiers using FIPS codes
Created population_final.csv
Result

✅ 3,275 US Counties

Education Data Processing
Steps Performed
Selected latest educational attainment data (2019–2023)
Extracted percentage of adults with bachelor's degree or higher
Removed national-level records
Created education_final.csv
Result

✅ 3,275 US Counties

Unemployment Data Processing
Steps Performed
Extracted 2023 unemployment rates
Removed non-county records
Created unemployment_final.csv
Result

✅ 3,272 Counties

Master Dataset Creation

The datasets were merged using:

FIPS Code

as the unique county identifier.

Merged Sources
Population Dataset
Education Dataset
Unemployment Dataset
Output

master_county_data.csv

Result

✅ 3,264 Counties

🏬 Competitor Analysis
Starbucks Analysis
Steps Performed
Filtered US locations from global dataset
Aggregated stores by state
Calculated Starbucks store counts
Walmart Analysis
Steps Performed
Aggregated Walmart locations by state
Calculated Walmart store counts
Competitor Density Metric

To estimate retail saturation:

Competitor Density =
Starbucks Count + Walmart Count

This metric represents the overall concentration of major retail competitors within each state.

# 🧠 Feature Engineering

Several analytical features were created to evaluate county attractiveness.

Population Score

Measures:

Market size
Customer volume potential

Higher population = Higher score

Education Score

Measures:

Purchasing power
Consumer sophistication

Higher education attainment = Higher score

Unemployment Score

Measures:

Economic health
Consumer spending capability

Lower unemployment = Better score

Competitor Density Ratio

Calculated as:

Competitor Stores
----------------------------
Population / 100,000

Purpose:

Measure competition intensity relative to population size.

# 🤖 AI-Inspired Opportunity Scoring Model

To identify the most attractive expansion locations, all variables were normalized using:

Min-Max Scaling

Each metric was transformed to a standardized scale between 0 and 1.

Opportunity Score Formula
Opportunity_Score =
0.40 * Pop_Score
+ 0.30 * Edu_Score
- 0.15 * Unemp_Score
- 0.15 * Comp_Score
Weighting Logic
Factor	Weight
Population Score	40%
Education Score	30%
Unemployment Score	-15%
Competition Score	-15%
Interpretation

Higher Opportunity Score indicates:

✅ Large customer base

✅ Strong purchasing power

✅ Healthy economy

✅ Lower competitive pressure

# 🏆 Top Retail Expansion Opportunities
Rank	County	State
1	Los Angeles County	California
2	Cook County	Illinois
3	Maricopa County	Arizona
4	Harris County	Texas
5	Arlington County	Virginia
6	Falls Church City	Virginia
7	King County	Washington
8	Fairfax County	Virginia
9	New York County	New York
10	Middlesex County	Massachusetts
## 📊 Power BI Dashboard

 The final stage of the project was the development of a multi-page Power BI dashboard designed to support strategic retail expansion decisions.

The dashboard transforms raw demographic, economic, and competitor data into actionable business insights that enable decision-makers to identify high-potential expansion markets across the United States.

The dashboard follows a business storytelling approach:

Page 1 → Where should we expand?
Page 2 → Why should we expand there?

This structure allows executives to move from opportunity identification to opportunity validation.

🏠 Dashboard Page 1: Executive Expansion Overview

The Executive Overview page provides a high-level summary of the retail expansion landscape across all analyzed US counties.

This page is designed for senior stakeholders who require quick insights without reviewing detailed county-level data.

Executive KPI Cards

Several key performance indicators (KPIs) were created to summarize market conditions.

Average Education Rate

Represents the average percentage of adults holding a bachelor's degree or higher.

Business Importance

Higher educational attainment often correlates with:

Higher disposable income
Stronger purchasing power
Greater retail spending potential
Average Unemployment Rate

Represents the average unemployment level across all counties.

Business Importance

Lower unemployment generally indicates:

Strong local economies
Stable consumer spending
Reduced business risk
Total Population

Represents the total population covered within the analysis.

Business Importance

Provides visibility into the overall addressable market size.

A larger population indicates a greater customer base for potential retail expansion.

Counties Analyzed

Represents the total number of counties included in the final analytical dataset.

Business Importance

Ensures broad geographic coverage and statistical reliability.

Total Competitor Stores

Represents combined Starbucks and Walmart store presence.

Business Importance

Used to estimate market saturation and competitive pressure.

Top Expansion State

Identifies the state with the highest average opportunity score.

Business Importance

Provides executives with an immediate understanding of which state offers the strongest retail expansion potential.

Best Opportunity Score

Displays the highest opportunity score achieved by any county.

Business Importance

Highlights the most attractive expansion target identified by the model.

Expansion Readiness Index

A summarized indicator reflecting overall market attractiveness.

Business Importance

Acts as a strategic benchmark for comparing market readiness.

📈 Top Retail Expansion Opportunities
Visualization Type

Horizontal Bar Chart

Purpose

Ranks counties according to Opportunity Score.

Business Question Answered

Which counties should be prioritized for retail expansion?

The chart highlights counties that combine:

Large populations
High educational attainment
Healthy economic conditions
Lower competitive pressure

These counties represent the strongest candidates for future retail investment.

🎯 Market Opportunity Matrix
Visualization Type

Scatter Plot

Dimensions
X-Axis

Competitor Density Ratio

Y-Axis

Opportunity Score

Bubble Size

Population

Legend

State

Business Purpose

This is the most important visual in the dashboard.

The matrix simultaneously evaluates:

Market attractiveness
Competition intensity
Customer volume

allowing decision-makers to compare counties across multiple dimensions.

Interpretation
Upper Left Quadrant

High Opportunity + Low Competition

These represent ideal expansion targets.

Upper Right Quadrant

High Opportunity + High Competition

These markets offer strong demand but require aggressive competitive strategies.

Lower Left Quadrant

Low Opportunity + Low Competition

Markets may require additional investigation.

Lower Right Quadrant

Low Opportunity + High Competition

Least attractive markets for expansion.

Business Value

This visual helps executives quickly identify counties offering the highest return potential with the lowest competitive risk.

📍 Dashboard Page 2: Expansion Intelligence Analysis

The second dashboard page focuses on understanding the underlying drivers behind expansion opportunities.

While Page 1 identifies where expansion should occur, Page 2 explains why those locations are attractive.

🗺 State Opportunity Heatmap
Visualization Type

Conditional Formatting Matrix

Metrics Displayed
Average Education
Average Unemployment
Average Opportunity Score

for each state.

Business Purpose

Allows users to compare state-level performance across key market indicators.

Business Insights Generated

The heatmap helps identify:

Highly educated states
Economically stable states
States with strong expansion potential

without requiring detailed county-level analysis.

🔻 Population Concentration by State
Visualization Type

Funnel Chart

Purpose

Displays how population is distributed across states.

Business Importance

Retail success is heavily influenced by customer availability.

States with larger populations offer:

Larger addressable markets
Greater sales opportunities
Higher long-term growth potential
Strategic Use

Supports prioritization of expansion efforts toward population-dense regions.

🥧 Walmart Store Distribution Analysis
Visualization Type

Pie Chart

Purpose

Visualizes Walmart's geographic presence across states.

Business Importance

Acts as a competitor footprint analysis.

Higher Walmart concentration often indicates:

Mature retail markets
Strong consumer demand
Increased competitive pressure
Strategic Use

Helps identify markets where retail competition may impact future expansion performance.

📉 Impact of Education on Retail Potential
Visualization Type

Trend Analysis Chart

Variables
Education Percentage
Opportunity Score
Purpose

Evaluates the relationship between education levels and retail attractiveness.

Business Insight

The analysis demonstrates that counties with higher educational attainment often achieve stronger opportunity scores.

This supports the hypothesis that education can serve as a useful proxy for purchasing power and consumer quality.

🚦 Expansion Readiness Indicators

Additional KPI cards were developed to support decision-making.

High Opportunity Counties

Counties exceeding the defined opportunity threshold.

Purpose

Identifies immediate expansion candidates.

Low Competition Counties

Counties with relatively low competitor density.

Purpose

Highlights markets where entry barriers are lower.

Expansion Ready Counties

Counties satisfying both:

High Opportunity
Low Competition

Purpose

Represents the highest-priority markets for future expansion.

🎯 Business Impact of the Dashboard

The dashboard enables retailers to:

✅ Identify high-potential counties for expansion

✅ Understand market attractiveness drivers

✅ Measure competitive pressure

✅ Compare states using key economic indicators

✅ Prioritize investment decisions using data

✅ Reduce risk associated with store location selection

✅ Support strategic planning through visual analytics





# 🛠 Tech Stack

Data Processing

Python

Pandas

NumPy

Data Analysis

Feature Engineering

Min-Max Scaling

Business Scoring Models

Visualization

Power BI Desktop


Data Sources

US Census Bureau

USDA Economic Research Service

Kaggle

📂 Project Structure

US-Retail-Expansion-Intelligence-Platform/

│
├── data/
│   ├── PopulationEstimates.csv
│   ├── Education.csv
│   ├── Unemployment.csv
│   ├── Starbucks.csv
│   └── Walmart.csv
│
├── processed_data/
│   ├── population_final.csv
│   ├── education_final.csv
│   ├── unemployment_final.csv
│   ├── master_county_only.csv
│   ├── competitor_master.csv
│   └── retail_opportunity_final.csv
│
├── scripts/
│   ├── clean_population.py
│   ├── clean_education.py
│   ├── clean_unemployment.py
│   ├── clean_starbucks.py
│   ├── clean_walmart.py
│   ├── merge_master.py
│   ├── merge_competitors.py
│   └── opportunity_score.py
│
├── dashboard/
│   └── Retail_Expansion_Dashboard.pbix
│
├── screenshots/
│   ├── dashboard_page1.png
│   └── dashboard_page2.png
│
├── requirements.txt
├── README.md
└── .gitignore
🚀 Future Improvements

Integrate additional retail brands for deeper competitor analysis.

Incorporate median household income data.

Add population growth forecasting.

Build predictive ML models for future expansion opportunities.

Deploy dashboard online using Power BI Service.
# 👩‍💻 Author

Smriti Pandey

B.Tech (CSE - Artificial Intelligence & Machine Learning)

Data Analytics | Business Intelligence | Machine Learning | Power BI
