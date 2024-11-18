import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX

# Data Dummy Penjualan UMKM Bakso (dalam porsi per bulan)
dummy_data = [120, 150, 170, 200, 190, 210, 230, 250, 240, 220, 210, 200,
              250, 270, 290, 310, 300, 320, 340, 360, 350, 330, 310, 300]


# Fungsi SARIMA
def sarima_forecast(data, steps):
    # Konversi data ke Pandas Series
    data_series = pd.Series(data)
    
    # Model SARIMA
    model = SARIMAX(data_series, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
    model_fit = model.fit(disp=False)
    
    # Prediksi
    forecast = model_fit.forecast(steps=steps)
    return forecast.tolist()
