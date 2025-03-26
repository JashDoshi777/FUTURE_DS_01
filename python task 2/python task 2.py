import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load dataset
csv_path = "customer_support_tickets.csv"
df = pd.read_csv(csv_path)

# Convert date columns to datetime format
df['First Response Time'] = pd.to_datetime(df['First Response Time'], errors='coerce')
df['Time to Resolution'] = pd.to_datetime(df['Time to Resolution'], errors='coerce')

# Calculate Response and Resolution times
df['Response Time (hours)'] = (df['First Response Time'] - df['First Response Time'].dt.normalize()).dt.total_seconds() / 3600
df['Resolution Time (hours)'] = (df['Time to Resolution'] - df['First Response Time']).dt.total_seconds() / 3600

# Analyze most frequent issues
issue_counts = df['Ticket Type'].value_counts()
plt.figure(figsize=(8, 4))
sns.barplot(x=issue_counts.index, y=issue_counts.values, hue=issue_counts.index, legend=False, palette='Blues')
plt.xticks(rotation=45)
plt.title('Most Frequent Ticket Types')
plt.ylabel('Count')
plt.show()

# Analyze average resolution time per ticket type
avg_resolution_time = df.groupby('Ticket Type')['Resolution Time (hours)'].mean().dropna()
plt.figure(figsize=(8, 4))
sns.barplot(x=avg_resolution_time.index, y=avg_resolution_time.values, hue=avg_resolution_time.index, legend=False, palette='Oranges')
plt.xticks(rotation=45)
plt.title('Average Resolution Time by Ticket Type')
plt.ylabel('Hours')
plt.show()

# Customer Satisfaction Analysis
satisfaction_avg = df.groupby('Ticket Type')['Customer Satisfaction Rating'].mean().dropna()
plt.figure(figsize=(8, 4))
sns.barplot(x=satisfaction_avg.index, y=satisfaction_avg.values, hue=satisfaction_avg.index, legend=False, palette='Greens')
plt.xticks(rotation=45)
plt.title('Average Customer Satisfaction by Ticket Type')
plt.ylabel('Satisfaction Rating')
plt.show()


# Suggestions to improve response time
improvement_suggestions = """
1. Prioritize High-Priority Tickets: Assign dedicated teams to urgent tickets.
2. Implement Automation: Use AI chatbots for quick responses to common issues.
3. Improve Staff Training: Ensure support staff are well-trained to handle issues efficiently.
4. Optimize Workflows: Reduce unnecessary steps in ticket resolution.
5. Use Data Insights: Analyze past trends to predict and resolve common issues faster.
"""

print("\nSuggestions to Improve Response Time:")
print(improvement_suggestions)

# Summary of findings
summary = {
    "Most Frequent Issue": issue_counts.idxmax(),
    "Slowest Resolved Issue": avg_resolution_time.idxmax() if not avg_resolution_time.empty else "N/A",
    "Highest Satisfaction Issue": satisfaction_avg.idxmax() if not satisfaction_avg.empty else "N/A",
}