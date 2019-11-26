import pandas as pd
from until import data_process

# =========================read data============================
stock_file_path = r'D:\temp\file_name'
stock_data = pd.read_excel(stock_file_path)

# =========================data process ===========================
date_sequence = data_process(stock_data)
