**Online Retail Data Analysis Report**

**Introduction**  
This project analyzes customer data from an online retail dataset to uncover insights and provide actionable business recommendations. The steps included data cleaning, exploratory data analysis (EDA), customer segmentation, and customer lifetime value (CLV) analysis.

**Results and Insights**

1. **Popular Products:**
   - The bar chart (`top_products_bar.png`) shows that “WHITE HANGING HEART T-LIGHT HOLDER” and similar items are the most popular, generating the highest revenue.
   - **Insight:** These products appeal to a wide range of customers, especially the largest segment (Cluster 0).

2. **Profitable Customer Segments:**
   - **Segmentation Results:**
     - Cluster 0 (Occasional Buyers): 3919 customers, average spending 903.37, frequency 2.78.
     - Cluster 1 (High-Value Regulars): 19 customers, average spending 40,824.96, frequency 63.89.
     - Cluster 2 (Moderate Spenders): 360 customers, average spending 6,585.93, frequency 15.90.
     - Cluster 3 (Super VIPs): 2 customers, average spending 139,896.48, frequency 131.
   - **CLV Results:**
     - Cluster 0: CLV = 445.68
     - Cluster 1: CLV = 37,888.30
     - Cluster 2: CLV = 5,863.01
     - Cluster 3: CLV = 138,461.94
   - **Insight:** Clusters 1 and 3 are the most profitable per customer, with the highest CLV (37,888.30 and 138,461.94). Cluster 0 generates the most total revenue (≈3.54 million) due to its size but has the lowest individual value (CLV = 445.68).

3. **Peak Transaction Times:**
   - The line plot (`sales_trend_line.png`) shows a spike in sales in December, likely due to holiday shopping.
   - **Insight:** The holiday season is the busiest time, offering a key opportunity to boost sales.

**Business Recommendations**

1. **Retain High-Value Customers (Clusters 1 and 3):**
   - Target the 21 customers in Clusters 1 and 3 with a VIP loyalty program (e.g., exclusive discounts, free shipping).
   - Use personalized marketing to keep them engaged.

2. **Turn Cluster 2 into High-Value Customers:**
   - Offer incentives to Cluster 2 (360 customers) to increase their buying frequency, like “Buy 5 times, get 10% off.”
   - Promote popular products in bundles to boost their spending.

3. **Engage Cluster 0 to Increase Spending:**
   - Run re-engagement campaigns for Cluster 0 (3919 customers), like “Free shipping on your next order.”
   - Promote affordable, popular products to encourage more purchases.

4. **Optimize for Peak Sales Periods:**
   - Prepare for the December sales spike by stocking up on popular products and running holiday promotions.

5. **Focus Marketing on Key Regions:**
   - Concentrate marketing efforts in the UK (from `country_sales_pie.png`) while testing small campaigns to grow sales in other countries.

**Deliverables**
- **Code:** Available on GitHub at `<your-repo-url>` (e.g., `retail-data-analysis`).
- **Visualizations:** Included in the repository (`correlation_heatmap.png`, `top_products_bar.png`, etc.).
