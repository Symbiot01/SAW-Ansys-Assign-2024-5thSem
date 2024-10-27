# SAW-Ansys-Assign-2024-5thSem  

This Python script automates the **mesh creation process in Ansys**, removing the need for manual input of mesh points. This saves time and effort, especially for repetitive tasks.  

## Overview  

The code automates **Step 4** of your workflow, which usually requires manual entry of points. With this script, you only need to edit a few parameters and switch to Ansys while the code runs.  

---

## How to Use  

1. **Follow the instructions in the provided PPT until Step 3**.  
2. Once you reach Step 3, **keep Ansys open and running in the background**.  
3. **Switch to the Python script** to edit and run it.  
4. **Edit the `x_step`, `y_step`, and `z_values` parameters** (detailed below) to match your project requirements.  
5. **Run the Python script**:  
   ```bash
   python automate.py
   ```
6. **Quickly switch back to the Ansys window** after starting the script, and place your cursor on the **Ansys Command Line**.  
   - The script will automatically enter all necessary commands to create the mesh.  
7. Once the script completes the process, **continue with the workflow from Step 5 in the PPT**.

---

## Editing the Values  

Before running the script, you need to adjust the parameters based on your mesh design. 

![Edit Value Diagram](https://github.com/user-attachments/assets/5a36f31b-a835-4ab3-a263-b427d0a74d4c)

### **1. x_step and y_steps**  
- These parameters represent the **horizontal distance** and **vertical distances** between points in the mesh.  
- Values must be specified in **meters**.  
- Refer to the diagram in the PPT to determine the correct spacing for your design.

### **2. z_values**  
- This parameter is an **array containing the z-coordinates** of all 42 points in the mesh.  
- These values should be specified in **millimeters**.  
- Make sure to input the z-coordinates in the **correct order** based on the diagram’s point numbering.

Example:
```python
x_step = 0.0515  # Distance between x points in meters
y_steps = [0.042, 0.042, 0.03, 0.04, 0.04]  # Distance between y points in meters
z_values = [1,1,1,0,0,0,1,    1,1,0,0,0,0,0,   1,0,0,0,0,0,0,    1,1,1,1,0,0,-1,     1,1,1,1,1,0,-1,     1,1,1,1,1,0,-1] # Array of z-coordinates in millimeters
```

---

## How to Run the Script  

1. **Install the required library**:  
   ```bash
   pip install pyautogui
   ```  
   - **Note:** The `pyautogui` library is used to automate mouse movements and keystrokes.  

2. **Run the script**:  
   ```bash
   python automate.py
   ```  

3. **Switch back to the Ansys window** immediately after running the script.  
   - Make sure the **Command Line** in Ansys is active to avoid interruptions.  

---

## Troubleshooting  

- **The script is not working or the cursor is not active:**  
  Ensure that Ansys is open, and the **cursor is placed on the Command Line** when you run the script.  
- **Incorrect z-coordinates:**  
  Double-check the order of your z-values to match the diagram’s sequence.  
- **Issues with `pyautogui`:**  
  If the library fails to install, ensure your Python version is up-to-date or run:
  ```bash
  pip install --upgrade pyautogui
  ```

---
