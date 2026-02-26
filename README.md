# Sales Automation & Monitoring System

### Project Overview

The Sales Automation & Monitoring System is an end-to-end data analytics project that automates daily sales data generation, monitors revenue trends from a MySQL database, detects anomalies, and triggers alerts for faster business decision-making.

This project combines Python automation, MySQL data storage, and Power BI visualization to build a complete sales monitoring solution.

### Objective

Manual sales tracking requires time and delays issue detection.
This project automates the process by:

Generating daily sales data
Monitoring revenue performance
Detecting abnormal increases or decreases
Triggering alerts automatically
Visualizing trends in a Power BI dashboard


### Tech Stack

- Python
- Pandas
- MySQL
- SMTP (Email alerts)
- Power BI
- VS Code

### Project Structure

sales-automation/

data_generator.py → Inserts daily sales data into MySQL  
sales_analyzer.py → Analyzes sales trends and detects anomalies  
alert_service.py → Sends alert notifications  
main.py → Runs complete automation pipeline  
  
dashboard/
  sales_dashboard.pbix  

### Workflow

Sales data is generated daily and stored in MySQL  
Analyzer fetches and processes sales data  
Daily revenue is compared with previous day  
If change exceeds threshold → alert triggered  
Power BI dashboard shows updated business insights  


### Key Features

Automated daily sales data insertion  
MySQL-based data storage  
Revenue trend analysis using Pandas  
Day-over-day percentage change detection  
Automated alert system  
Power BI visualization dashboard  
Modular and scalable project structure  


### 📊 Power BI Dashboard

- Dashboard provides:
- Daily revenue trend
- Sales performance overview
- Anomaly tracking
- Business insights for decision-making



### How to Run the Project

Run the pipeline using:  
python run_pipeline.py  

This will:  
Insert daily sales data  
Analyze performance  
Trigger alerts if required  


### Business Impact

- Reduced manual monitoring effort
- Faster detection of revenue drops or spikes
- Improved reporting automation
- Data-driven decision support
- Better sales visibility for stakeholders


🔮 Future Enhancements

Machine learning–based anomaly detection  
Deployment using Docker  
Scheduling using Cron / Task Scheduler  
Web dashboard using Flask  
Multi-store / multi-region sales tracking  



### Project Value

This project demonstrates:

Python automation  
SQL + Python integration  
Business analytics thinking  
Alerting & monitoring system design  
Dashboard-driven decision support  
