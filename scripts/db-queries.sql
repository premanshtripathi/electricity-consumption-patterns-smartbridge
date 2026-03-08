-- ==============================================================================
-- Project: EnergyGrid Analytics - COVID-19 Power Consumption Impact
-- Description: Schema creation, data ingestion, and analytical operations.
-- ==============================================================================

-- ------------------------------------------------------------------------------
-- 1. DATABASE SETUP & SCHEMA CREATION
-- ------------------------------------------------------------------------------
CREATE DATABASE IF NOT EXISTS skillwallet;
USE skillwallet;

-- Drop table if it already exists to ensure a clean slate
DROP TABLE IF EXISTS electricity_final;

-- Create the optimized table for the melted time-series data
CREATE TABLE electricity_final (
    Record_Date DATE NOT NULL,
    State VARCHAR(100) NOT NULL,
    Consumption_MU DECIMAL(10, 2) NOT NULL,
    INDEX idx_date (Record_Date),  -- Indexed for faster time-series querying
    INDEX idx_state (State)        -- Indexed for faster regional grouping
);

-- ------------------------------------------------------------------------------
-- 2. DATA INGESTION (ETL LOAD PHASE)
-- ------------------------------------------------------------------------------
-- Note: In local development, this was executed via MySQL Workbench Data Wizard.
-- The following is the production-equivalent LOAD statement for 23,000+ records.

LOAD DATA LOCAL INFILE 'D:/project_data/power_consumption_clean.csv'
INTO TABLE electricity_final
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(Record_Date, State, Consumption_MU);


-- ------------------------------------------------------------------------------
-- 3. SCENARIO PREPARATION (FILTERING & VIEWS)
-- ------------------------------------------------------------------------------
-- Isolate the project scope (Jan 2019 - Dec 2020)
-- This view acts as the secure, filtered data source for the Tableau connection

CREATE OR REPLACE VIEW v_covid_power_analysis AS
SELECT * FROM electricity_final
WHERE Record_Date BETWEEN '2019-01-01' AND '2020-12-05';


-- ------------------------------------------------------------------------------
-- 4. ANALYTICAL QUERIES (SCENARIO VALIDATION)
-- ------------------------------------------------------------------------------

-- Scenario 1 Validation: Finding the lowest consumption month (The Crash)
SELECT 
    DATE_FORMAT(Record_Date, '%Y-%m') AS YearMonth,
    SUM(Consumption_MU) AS Total_National_Consumption
FROM electricity_final
WHERE Record_Date BETWEEN '2020-01-01' AND '2020-12-31'
GROUP BY YearMonth
ORDER BY Total_National_Consumption ASC
LIMIT 3; 
-- Expected Result: April & May 2020 should appear at the top.


-- Scenario 2 Validation: Regional Impact (YoY Drop Calculation for Industrial Hub)
-- Comparing Pre-Pandemic (April 2019) vs Strict Lockdown (April 2020) for Maharashtra
SELECT 
    State,
    SUM(CASE WHEN Record_Date BETWEEN '2019-04-01' AND '2019-04-30' THEN Consumption_MU ELSE 0 END) AS April_2019_MU,
    SUM(CASE WHEN Record_Date BETWEEN '2020-04-01' AND '2020-04-30' THEN Consumption_MU ELSE 0 END) AS April_2020_MU,
    ROUND(
        ((SUM(CASE WHEN Record_Date BETWEEN '2020-04-01' AND '2020-04-30' THEN Consumption_MU ELSE 0 END) - 
        SUM(CASE WHEN Record_Date BETWEEN '2019-04-01' AND '2019-04-30' THEN Consumption_MU ELSE 0 END)) / 
        SUM(CASE WHEN Record_Date BETWEEN '2019-04-01' AND '2019-04-30' THEN Consumption_MU ELSE 0 END)) * 100, 
    2) AS Percentage_Drop
FROM electricity_final
WHERE State IN ('Maharashtra', 'Gujarat', 'Delhi')
GROUP BY State;


-- ------------------------------------------------------------------------------
-- 5. PERFORMANCE & INTEGRITY TESTING
-- ------------------------------------------------------------------------------
-- Verify total data volume rendered to DB (Should be 23,000+)
SELECT COUNT(*) AS Total_Records_Processed FROM electricity_final;

-- Verify data boundaries and integrity
SELECT 
    MIN(Record_Date) AS Project_Start_Date, 
    MAX(Record_Date) AS Project_End_Date,
    COUNT(DISTINCT State) AS Total_Regions_Tracked
FROM v_covid_power_analysis;