from mlops.utils.analytics.data import load_data

# https://docs.mage.ai/visualizations/dashboards

@data_source
def data(*args, **kwargs):
    df=load_data()
    df['start_time_seconds']=df['start_time'].astype(np.int64)//10**9
    return df