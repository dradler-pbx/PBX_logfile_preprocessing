import PBX_auxiliary.data_postprocessing.data_postprocessing as PBX_dp
import os
import pandas as pd
from CoolProp.CoolProp import PropsSI as CPPSI

folderpath = 'files'
filelist = os.listdir(folderpath)
parameterID = pd.read_excel('ParameterID.xlsx')

data = PBX_dp.read_csv_to_df(filelist, folderpath)
data = PBX_dp.convert_column_names(data, parameterID)
# data = PBX_dp.aggregate_samplingtime(data, 10)

data['T0'] = [CPPSI('T', 'P', max(p, 1e5), 'Q', 0, 'R290') for p in data['press_ref_low'].values]