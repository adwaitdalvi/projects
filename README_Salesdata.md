# projects
Sales analytics is the practice of generating insights from sales data, trends, and metrics to set targets and forecast future sales performance. Sales analysis is mining your data to evaluate the performance of your sales team against its goals. It provides insights about the top performing and underperforming products/services, the problems in selling and market opportunities, sales forecasting, and sales activities that generate revenue.

Content
Order ID - An Order ID is the number system that Amazon uses exclusively to keep track of orders. Each order receives its own Order ID that will not be duplicated. This number can be useful to the seller when attempting to find out certain details about an order such as shipment date or status.
Product - The product that have been sold.
Quantity Ordered - Ordered Quantity is the total item quantity ordered in the initial order (without any changes).
Price Each - The price of each products.
Order Date - This is the date the customer is requesting the order be shipped.
Purchase Address - The purchase order is prepared by the buyer, often through a purchasing department. The purchase order, or PO, usually includes a PO number, which is useful in matching shipments with purchases; a shipping date; billing address; shipping address; and the request items, quantities and price.
Target
A target market analysis is an assessment of how your product or service fits into a specific market and where it will gain the most.

Task:
Q: What was the best Year for sales? How much was earned that Year?
Q: What was the best month for sales? How much was earned that month?
Q: What City had the highest number of sales?
Q: What time should we display adverstisement to maximize likelihood of customer's buying product?
Q: What products are most often sold together?
Q: What product sold the most? Why do you think it sold the most?

[Sales_January_2019.csv](https://github.com/adwaitdalvi/projects/files/11188638/Sales_January_2019.csv)
[Sales_July_2019.csv](https://github.com/adwaitdalvi/projects/files/11188640/Sales_July_2019.csv)
[Sales_June_2019.csv](https://github.com/adwaitdalvi/projects/files/11188641/Sales_June_2019.csv)
[Sales_March_2019.csv](https://github.com/adwaitdalvi/projects/files/11188642/Sales_March_2019.csv)
[Sales_May_2019.csv](https://github.com/adwaitdalvi/projects/files/11188643/Sales_May_2019.csv)
[Sales_November_2019.csv](https://github.com/adwaitdalvi/projects/files/11188644/Sales_November_2019.csv)
[Sales_October_2019.csv](https://github.com/adwaitdalvi/projects/files/11188645/Sales_October_2019.csv)
[Sales_September_2019.csv](https://github.com/adwaitdalvi/projects/files/11188646/Sales_September_2019.csv)
[Sales_April_2019.csv](https://github.com/adwaitdalvi/projects/files/11188647/Sales_April_2019.csv)
[Sales_August_2019.csv](https://github.com/adwaitdalvi/projects/files/11188649/Sales_August_2019.csv)
[Sales_December_2019.csv](https://github.com/adwaitdalvi/projects/files/11188650/Sales_December_2019.csv)
[Sales_February_2019.csv](https://github.com/adwaitdalvi/projects/files/11188651/Sales_February_2019.csv)

Step1: Combined the monthly data to a single CSV file.
Step2: Remove all the blankspaces in datasets.
Step3: Changing the column name for "Quantity Ordered" - "Qty" & "Price Each" - "Price Per Product"	
Step4: Checking if there are any null values if yes remove them.
Step5: Check for the duplicated values if yes delete them.
Step6: Converted the columns names in Smallercase
Step7: Resetting the index.
Step8: Seperating month from order date column.
Step9: Creating a colum "Total Sales" by multiplying "Qty" and "price Per product"
Step10: Seperating States from address.
Step 11: Answering the question.
