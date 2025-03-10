import os
import pandas as pd
import statsmodels.api as sm



def load_data(filename, path, env):
    if env in [1,2]:
        file_path = os.path.join(path, filename)
    elif env == 3:
        from google.colab import drive
        drive.mount("/content/drive", force_remount=True)
        file_path = os.path.join(drive_path, file_name)
    return pd.read_csv(file_path)

# def parameter_significance_test(X, y, significance = 0.05):
#     X = sm.add_constant(X)
    
#     hasChange = False
#     while not hasChange:
#         model = sm.OLS(y,X).fit()
#          = model.pvalues[1:]


sector_mapping = {
    range(1, 4): "AGRICULTURE",
    range(1, 3): "Agriculture and Forestry",
    range(3, 4): "Fishing",
    range(5, 44): "INDUSTRY",
    range(5, 10): "Mining and Quarrying",
    range(10, 34): "Manufacturing",
    range(35, 36): "Electricity, Gas, Steam and Air Conditioning Supply",
    range(36, 40): "Water Supply; Sewerage, Waste Management and Remediation",
    range(41, 44): "Construction",
    range(45, 100): "SERVICES",
    range(45, 48): "Wholesale and Retail Trade; Repair of Motor Vehicles and Motorcycles",
    range(49, 54): "Transportation and Storage",
    range(55, 57): "Accommodation and Food Service Activities",
    range(58, 64): "Information and Communication",
    range(64, 67): "Financial and Insurance Activities",
    range(68, 69): "Real Estate Activities",
    range(69, 76): "Professional, Scientific and Technical Activities",
    range(77, 83): "Administrative and Support Service Activities",
    range(84, 85): "Public Administration and Defense; Compulsory Social Security",
    range(85, 86): "Education",
    range(86, 89): "Human Health and Social Work Activities",
    range(90, 94): "Arts, Entertainment and Recreation",
    range(94, 97): "Other Service Activities",
    range(97, 99): "Activities of Households as Employers",
    range(99, 100): "Activities of Extraterritorial Organizations and Bodies"
}

# Function to find the sector
def map_sector(value):
    for sector_range, sector_name in sector_mapping.items():
        if value == '  ':
            return "Unknown"
        elif int(value) in sector_range:
            return sector_name
    return "Unknown"
