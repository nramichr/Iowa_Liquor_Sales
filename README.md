Iowa Liquor Sales Analysis (Python) 

Project Overview:
    This project analyzes reatil liquor sales data from the state of Iowa to identify sales trends, top-performing counties, and revenue concentration patterns. The analysis is designed from a Business Analyst perspective, focusing on clear KPIs, aggregation logic, and acitonable insights rather than advanced modeling.

The Primary goal of this project is to demonstrate:

    - Practical Python data analysis skills
    - Business-focused thinking and metric defintion
    - Ability to work wiht large, real world data sets efficiently
    - Clear communication of insights for non-technical stakeholders

Business Context
State-level sales data can help decision-makers understand:

    - Which geographic regions drive the majority of revenue
    - How sale fluctuate over time
    - Where revenue concentration or depenendency risk exists

For this project, Liquor sales are treated as a proxy for consumer spending behavior and reatil perfomrance across countires.

Dataset Description:
Source: Iowa Department of Revenue - https://data.iowa.gov/Sales-Distribution/Iowa-Liquor-Sales/m3tr-qhgy/about_data

Dataset: Iowa Liquor Sales

Original Size: 9.14GB

Format: CSV

Granularity: Individual retail transactions

    Key Columns Used 
        To improve perfomance and keep the analysis focused, only a subset of columns was used:
            date - Date of sale
            county - County where the sale occurred
            store_name - Retail store name
            sale_dollars - Dollar amount of each sale


Data Handling & Performance Strategy
The full dataset conatins millions of records and is too large for routine analysis ona  standard laptop. To address this:

    - Only relevant columns were loaded using "usecols"
    - A subset of rows was sampled for analysis
    - Datew parsing was handled during ingestion for accurate time-series aggregation

This approach mirrors real-world Business Analyst workflows, where analysts rarelty work with raw prodution datasets in full.

        *** The full 9.14GB dataset is not included in this repositor. A smaller sampled dataset was used for reproducibilty and performance. ***

Key Business Metrics (KPIs)
    The following KPIs were calculated using Python and pandas:
    
        - Total Sales Revenue
        - Sales by County (Top 10)
        - Monthly Sales Trends
        - Revenue Concentration by Geography
    These metrics are commonly used in reatil adn public secotr reporting.

Analysis Summary

1. County-Level Performance
        Sales were aggregated by country to identify top-performing regions. This helps highlight:
   
            - Revenue concentration in urban area
            - Counties that may warrant deeper investigation or targeted policy decisions
   
3. Time-Series Trends
        Sales were aggregated on a monthly basis to evaluate:
   
            - Seasonality
            - Growth or decline patterns
            - Patterns of unsually high or low revenue

Key Insights

    - Liquor sale revenue is highly concentrated in a small number of counties
    - Monthyl sales exhibit consistent seasonal patterns
    - Urban counties contribute a disproportionate share of total revenue
    - Revenue concentraiotn suggests potential geographic depndency risk
    
These insights reflect how a Business Analyst would summarize findings for leadership or stakeholders

Tool & Technologies

    - Python
    - pandas - Data cleaning and aggregation
    - matplotlib - Visualization
    - Visual Studio Code - Exploratory analysis

    *** Final Notes ***
                This project was intentionally scoped to reflect how a Business Analyst would work with a large public dataset: effiently, selectively, and with an emphasis on insights rather than techincal complexity. 
