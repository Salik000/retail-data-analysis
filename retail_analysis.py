# Import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Step 1: Load and Clean Data
data = pd.read_excel('C:/Users/mohds/OneDrive/Documents/Online Retail.xlsx')
data = data.dropna(subset=['CustomerID'])
data['Description'] = data['Description'].fillna('Unknown')
data = data.drop_duplicates()
data = data[(data['Quantity'] > 0) & (data['Quantity'] <= 100)]
data = data[(data['UnitPrice'] > 0) & (data['UnitPrice'] <= 500)]

# Step 2: Transform Data
data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])
data['CustomerID'] = data['CustomerID'].astype(int)
data['TotalPrice'] = data['Quantity'] * data['UnitPrice']
data['Day'] = data['InvoiceDate'].dt.day
data['Month'] = data['InvoiceDate'].dt.month
data['Year'] = data['InvoiceDate'].dt.year
data['DayOfWeek'] = data['InvoiceDate'].dt.day_name()

# Step 3: Exploratory Data Analysis (EDA)
# Summary statistics
print(data[['Quantity', 'UnitPrice', 'TotalPrice']].describe())

# Correlation heatmap
sns.heatmap(data[['Quantity', 'UnitPrice', 'TotalPrice']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.savefig('correlation_heatmap.png')
plt.close()

# Histogram of customer spending
sns.histplot(data['TotalPrice'], bins=30)
plt.title('Distribution of Customer Spending')
plt.xlabel('Total Price')
plt.savefig('spending_histogram.png')
plt.close()

# Bar chart of top products
top_products = data.groupby('Description')['TotalPrice'].sum().sort_values(ascending=False).head(10)
top_products.plot(kind='bar')
plt.title('Top 10 Products by Revenue')
plt.ylabel('Total Revenue')
plt.savefig('top_products_bar.png')
plt.close()

# Line plot of sales over time
sales_trend = data.groupby(data['InvoiceDate'].dt.to_period('M'))['TotalPrice'].sum()
sales_trend.plot()
plt.title('Sales Trends Over Time')
plt.ylabel('Total Sales')
plt.savefig('sales_trend_line.png')
plt.close()

# Pie chart of sales by country
country_sales = data.groupby('Country')['TotalPrice'].sum()
country_sales.plot(kind='pie', autopct='%1.1f%%')
plt.title('Sales Distribution by Country')
plt.savefig('country_sales_pie.png')
plt.close()

# Step 4: Customer Segmentation
# Summarize customer data
customer_data = data.groupby('CustomerID').agg({
    'TotalPrice': 'sum',
    'InvoiceNo': 'nunique'
}).rename(columns={'TotalPrice': 'TotalSpending', 'InvoiceNo': 'Frequency'})

# Standardize the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(customer_data)

# Elbow method to find the best number of clusters
inertia = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_data)
    inertia.append(kmeans.inertia_)
plt.plot(range(1, 11), inertia)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.savefig('elbow_plot.png')
plt.close()

# Apply K-Means with 4 clusters
kmeans = KMeans(n_clusters=4, random_state=42)
customer_data['Cluster'] = kmeans.fit_predict(scaled_data)

# Analyze clusters
print(customer_data.groupby('Cluster')[['TotalSpending', 'Frequency']].mean())
print(customer_data['Cluster'].value_counts())

# Step 5: Customer Lifetime Value (CLV)
# Calculate lifespan
customer_dates = data.groupby('CustomerID')['InvoiceDate'].agg(['min', 'max'])
customer_dates['Lifespan'] = (customer_dates['max'] - customer_dates['min']).dt.days / 365
customer_dates = customer_dates.rename(columns={'min': 'FirstPurchase', 'max': 'LastPurchase'})

# Add average purchase value and lifespan to customer_data
customer_data['AvgPurchaseValue'] = customer_data['TotalSpending'] / customer_data['Frequency']
customer_data = customer_data.join(customer_dates['Lifespan'])

# Calculate CLV
customer_data['CLV'] = customer_data['TotalSpending'] * customer_data['Lifespan']
print(customer_data.groupby('Cluster')['CLV'].mean())
