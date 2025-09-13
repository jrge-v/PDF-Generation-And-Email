import pandas as pd
import json
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Load JSON data
with open('sales.json', 'r') as file:
    data_sales = json.load(file)

# Transform data into flat structure
rows = []
for item in data_sales:
    car = item['car']
    car_name = f"{car['car_make']} {car['car_model']} ({car['car_year']})"
    rows.append([
        item['id'],
        car_name,
        item['price'],
        item['total_sales']
    ])

# Create DataFrame
df = pd.DataFrame(rows, columns=['ID', 'Car', 'Price', 'Total Sales'])

# Create figure and axis for table
fig, ax = plt.subplots(figsize=(12, len(df) * 0.5 + 1))
ax.axis('off')

# pdf header
ax.set_title("Sales Summary for last month", fontsize=16, weight='bold', pad=20)

# Create the table in the plot
table = ax.table(
    cellText=df.values,
    colLabels=df.columns,
    loc='center',
    cellLoc='center'
)

# Style the table
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 1.5)

# Save to PDF
with PdfPages("cars.pdf") as pdf:
    pdf.savefig(fig, bbox_inches='tight')

plt.close()

