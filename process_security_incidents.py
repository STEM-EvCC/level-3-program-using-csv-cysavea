import csv

# CSV content as a string
csv_content = """IncidentID,Date,Type,Severity,Description,Status
1,1/15/2023,Phishing,High,Phishing email targeting company employees,Pending
2,1/20/2023,Malware,Medium,Malware detected on employee workstation,Pending
3,2/5/2023,Ransomware,Critical,Ransomware attack encrypting company data,Pending
4,3/10/2023,Phishing,Low,Phishing email targeting external customers,Pending
5,3/15/2023,Data Breach,Critical,Sensitive data leaked from database,Pending"""

# Read CSV content and store in a list of dictionaries
data = list(csv.DictReader(csv_content.splitlines()))

# Add the new column with the default value
for row in data:
    row['Status'] = 'Pending'

# Print the data
print(data)