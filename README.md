### Exploratory Data Analysis of the ['2000_2024_Stocks_data'](https://www.kaggle.com/datasets/sbgonenc96/2000-2024-stocks-data/code?datasetId=5602820&sortBy=dateRun&tab=profile&excludeNonAccessedDatasources=false)
# Executive Summary
__This analysis was stopped and not completed as of 1/20/2025.__

The data source claimed to contain "NASDAQ and NYSE historical data from 02/01/2000 to 27/08/2024 per 30 minutes." however it contained only 2 years 2022-08-30 to 2024-08-23.   The count of tickers by letter reporting close prices per interval (i.e., the number of non-null values) dropped by 25% - 50% from the start of history until the end.  It is expected that the aggregate count would be relatively stable over a two-year period without significant market events.  


![image](https://github.com/user-attachments/assets/0e697163-81f1-414e-b495-39670fb9f788)

### Next Steps
The initial objectives can still be studied with the current dataset, but the declining ticker counts will introduce inaccuracies.   Alternatively, different data sources are available to be explored.

__Primary Objective:__  
What is the maximum possible return that could be achieved trading the top performing NASDAQ and NYSE historical stocks from 02/01/2000 to 27/08/2024?

__Secondary Objectives:__
* explore 'return/bar' as a performance metric
* understand distributions and possible application of 'return/bar'
