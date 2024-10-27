# How to use: Open readme.md




import time
import pyautogui
time.sleep(8)
# Parameters
x_start = 0  # Initial x value
y_start = 0  # Initial y value


# to be changed
x_step = 0.0515  # Distance between x points
y_steps = [0.042, 0.042, 0.03, 0.04, 0.04]  # Distance between y points 
z_values = [1,1,1,0,0,0,1,    1,1,0,0,0,0,0,   1,0,0,0,0,0,0,    1,1,1,1,0,0,-1,     1,1,1,1,1,0,-1,     1,1,1,1,1,0,-1] # Possible z values 
pyautogui.press('/PREP7')
pyautogui.press('enter')
pointnum = 1
points = []  # To store points for triangle creation

# Loop through y values (6 rows)
for i in range(6):
    y = y_start + sum(y_steps[:i])  # Calculate y for the current row

    # Loop through x values (7 columns)
    for j in range(7):
        x = x_start + (j * x_step)  # Calculate x for the current column

        # Get the corresponding z value for the current point
        z_value = z_values[pointnum - 1]/1000  # Get the z value based on pointnum

        # Format the point as K, x, y, z
        point = f"K, {pointnum},{x:.3f}, {y:.3f}, {z_value:.3f}"
        pyautogui.write(point)  # Type the point
        pyautogui.press('enter')  # Press Enter after typing the point

        points.append(pointnum)  # Store point number for triangle creation
        pointnum += 1
        time.sleep(0.05)  # Small delay to ensure smooth typing


# Create triangles by connecting points in clockwise manner
triangles = []
for i in range(5):  # Loop over rows (5 triangles per row)
    for j in range(6):  # Loop over columns (6 triangles per row)
        # Define triangle points
        p1 = points[i * 7 + j]  # Bottom left point
        p2 = points[i * 7 + (j + 1)]  # Bottom right point
        p3 = points[(i + 1) * 7 + j]  # Top left point
        p4 = points[(i + 1) * 7 + (j + 1)]  # Top right point

        # Create two triangles for the square formed by p1, p2, p3, and p4
        triangles.append(f"a,{p1},{p2},{p3}")  # First triangle
        triangles.append(f"a,{p2},{p4},{p3}")  # Second triangle

# Output the triangles
for triangle in triangles:
    pyautogui.write(triangle)  # Type the triangle definition
    pyautogui.press('enter')  # Press Enter after typing the triangle definition
    time.sleep(0.05)  # Small delay to ensure smooth typing

# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_pdf import PdfPages

# # Define the data for before and after welding
# time_freq_before = [
#     0.0000000, 0.0000000, 0.0000000, 0.28392023E-03, 0.70205040E-03,
#     0.50627276E-02, 1951.8866, 2049.3667, 4584.0287,
#     5345.0186, 5977.5133, 7280.8493, 8090.3895,
#     9993.0156, 10947.313
# ]

# time_freq_after = [
#     0.0000000, 0.0000000, 0.0000000, 0.59894750E-03, 0.74846393E-03,
#     0.83868384E-03, 1947.6408, 2034.2744, 4508.5924,
#     5249.3492, 5876.6780, 7123.2462, 7928.9924,
#     9718.7227, 10513.724
# ]

# cumulative = list(range(1, len(time_freq_before) + 1))  # Cumulative values

# # Create DataFrames for each data set
# df_before = pd.DataFrame({
#     'Cumulative': cumulative,
#     'Time/Freq (Before)': time_freq_before
# })

# df_after = pd.DataFrame({
#     'Cumulative': cumulative,
#     'Time/Freq (After)': time_freq_after
# })

# # Save both graphs and data in a single PDF
# pdf_filename = 'welding_analysis.pdf'
# with PdfPages(pdf_filename) as pdf:
#     # Plot 1: Before Welding
#     plt.figure(figsize=(10, 6))
#     plt.plot(cumulative, time_freq_before, marker='o', linestyle='-', color='b', label='Before Welding')
#     plt.xlabel('Cumulative')
#     plt.ylabel('Time/Freq')
#     plt.title('Time/Frequency vs Cumulative (Before Welding)')
#     plt.grid(True)
#     plt.legend()
#     pdf.savefig()  # Save the plot to the PDF
#     plt.close()

#     # Plot 2: After Welding
#     plt.figure(figsize=(10, 6))
#     plt.plot(cumulative, time_freq_after, marker='o', linestyle='-', color='r', label='After Welding')
#     plt.xlabel('Cumulative')
#     plt.ylabel('Time/Freq')
#     plt.title('Time/Frequency vs Cumulative (After Welding)')
#     plt.grid(True)
#     plt.legend()
#     pdf.savefig()  # Save the plot to the PDF
#     plt.close()

#     # Create a new page for the data tables (Before and After Welding)
#     fig, ax = plt.subplots(figsize=(10, 8))
#     ax.axis('off')

#     # Display both data tables side-by-side
#     table_data = pd.concat([df_before, df_after.drop('Cumulative', axis=1)], axis=1)
#     table = ax.table(
#         cellText=table_data.values,
#         colLabels=table_data.columns,
#         cellLoc='center',
#         loc='center'
#     )
#     table.scale(1.2, 1.5)  # Adjust the scale for better fit

#     pdf.savefig()  # Save the table page to the PDF
#     plt.close()

# print(f"Graphs and data successfully saved in {pdf_filename}")


# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_pdf import PdfPages

# # Define the Z value differences and key point numbers
# z_value_diff = [
#     0.001, 0, 0, 0.001,
#     0, 0, 0, 0.001, 0, 0, 0, 0, 
#     0.001, 0.001, 0.001, 0.001,
#     0.001, 0.001, 0.001, 0.001, 
#     0.001, 0.002, 0.001, 0.001, 0, 0, 0.001, 
#     0.001, 0, 0, 0.001, 0, 0.001, 
#     0, 0.001, 0.001, -0.001, -0.001, -0.001, 0, 0, 0
# ]

# # Generate key point numbers (1 to length of z_value_diff)
# key_point_no = list(range(1, len(z_value_diff) + 1))

# # Create a DataFrame
# df = pd.DataFrame({
#     'Key Point No.': key_point_no,
#     'Difference(Before and after Welding)': z_value_diff
# })

# # Define the PDF file to save the output
# pdf_filename = 'z_value_difference_graph.pdf'

# # Save the plot and table to a PDF
# with PdfPages(pdf_filename) as pdf:
#     # Create the plot (Landscape, A4 size)
#     plt.figure(figsize=(11.69, 8.27))  # A4 in landscape (inches: 11.69 x 8.27)
#     plt.plot(df['Key Point No.'], df['Difference(Before and after Welding)'], marker='o', linestyle='-', color='b')
#     plt.axhline(0, color='black', linewidth=1, linestyle='--')  # Add horizontal line at y=0
#     plt.xlabel('Key Point No.')
#     plt.ylabel('Difference(Before and after Welding) in mm')
#     plt.title('Difference(Before and after Welding) vs Key Point No.')
#     plt.grid(True)

#     # Save the plot as the first page in the PDF
#     pdf.savefig()
#     plt.close()

#     # Create a table to display the data on the second page (A4 size)
#     fig, ax = plt.subplots(figsize=(8.27, 11.69))  # A4 in portrait (inches: 8.27 x 11.69)
#     ax.axis('off')  # Hide axes

#     # Create the table from the DataFrame
#     table = ax.table(
#         cellText=df.values,
#         colLabels=df.columns,
#         cellLoc='center',
#         loc='center'
#     )
#     table.scale(1, 1.5)  # Adjust the table size for better fit

#     # Save the table as the second page in the PDF
#     pdf.savefig()
#     plt.close()

# print(f"Graph and data successfully saved in {pdf_filename}.")
