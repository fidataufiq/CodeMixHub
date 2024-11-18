from flask import Flask, render_template, request, redirect, url_for, jsonify
from forecast_model import sarima_forecast, dummy_data

app = Flask(__name__)

# Halaman Dashboard
@app.route('/')
def dashboard():
    return render_template('dashboard.html', data=dummy_data)

# Halaman Forecast
@app.route('/forecast', methods=['GET', 'POST'])
def forecast():
    global dummy_data
    months = [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun", 
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ]
    start_year = 2023
    forecast_result = []
    forecast_data = []

    if request.method == 'POST':  # Hanya proses jika form di-submit
        steps = int(request.form['steps'])
        # Generate forecast data
        forecast_data = sarima_forecast(dummy_data, steps)

        # Prepare forecast data for table
        for i in range(len(dummy_data), len(dummy_data) + steps):
            month_index = i % 12
            year = start_year + (i // 12)
            forecast_result.append({
                "no": i - len(dummy_data) + 1,
                "month": months[month_index],
                "year": year,
                "porsi": forecast_data[i - len(dummy_data)]
            })

    # Render template with data
    return render_template(
        'forecast.html',
        data=forecast_result,
        actual_data=dummy_data,
        forecast_data=forecast_data
    )



# Halaman Results
@app.route('/results')
def results():
    global dummy_data
    # Data tambahan untuk tabel
    months = [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun", 
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ]
    # Buat data dengan kolom No, Bulan, Tahun, dan Porsi
    results_data = []
    start_year = 2023
    for i, value in enumerate(dummy_data):
        month_index = i % 12
        year = start_year + (i // 12)
        results_data.append({
            "no": i + 1,
            "month": months[month_index],
            "year": year,
            "porsi": value
        })
    return render_template('results.html', data=results_data)


# Halaman Settings
@app.route('/settings', methods=['GET', 'POST'])
def settings():
    global dummy_data
    # Data tambahan untuk tabel
    months = [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun", 
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ]
    # Buat data dengan kolom No, Bulan, Tahun, dan Porsi
    settings_data = []
    start_year = 2023
    for i, value in enumerate(dummy_data):
        month_index = i % 12
        year = start_year + (i // 12)
        settings_data.append({
            "no": i + 1,
            "month": months[month_index],
            "year": year,
            "porsi": value,
            "index": i
        })

    if request.method == 'POST':
        action = request.form.get('action')

        # Tambah Bulan
        if action == "add":
            new_value = int(request.form['new_value'])
            dummy_data.append(new_value)

        # Hapus Bulan
        elif action == "delete":
            index = int(request.form['index'])
            if 0 <= index < len(dummy_data):
                dummy_data.pop(index)

        # Update Data
        elif action == "update":
            index = int(request.form['index'])
            new_value = int(request.form['new_value'])
            dummy_data[index] = new_value

        return redirect(url_for('settings'))

    return render_template('settings.html', data=settings_data)

import io
import base64
from matplotlib.figure import Figure

import plotly.graph_objs as go
from flask import jsonify

@app.route('/forecast_plot')
def forecast_plot():
    global dummy_data
    months = [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun", 
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ]
    start_year = 2023
    steps = request.args.get('steps', type=int)  # Ambil jumlah langkah dari query parameter
    forecast_data = sarima_forecast(dummy_data, steps) if steps else []

    # Generate x-labels for graph
    x_labels_actual = []
    x_labels_forecast = []
    for i in range(len(dummy_data)):
        month_index = i % 12
        year = start_year + (i // 12)
        x_labels_actual.append(f"{months[month_index]} {year}")
    for i in range(len(dummy_data), len(dummy_data) + len(forecast_data)):
        month_index = i % 12
        year = start_year + (i // 12)
        x_labels_forecast.append(f"{months[month_index]} {year}")

    # Create Plotly traces for actual and forecast data
    actual_trace = go.Scatter(
        x=x_labels_actual,
        y=dummy_data,
        mode='lines+markers',
        name='Data Aktual',
        line=dict(color='blue', width=2),
        marker=dict(size=6)
    )
    forecast_trace = go.Scatter(
        x=x_labels_forecast,
        y=forecast_data,
        mode='lines+markers',
        name='Data Forecast',
        line=dict(color='orange', dash='dash', width=2),
        marker=dict(size=6)
    )

    # Combine traces and layout
    layout = go.Layout(
        title="Forecasting Penjualan Bulanan",
        xaxis=dict(title="Bulan", showgrid=True, tickangle=45),
        yaxis=dict(title="Jumlah Porsi Penjualan", showgrid=True),
        hovermode="x unified",
        template="plotly_white"
    )
    fig = go.Figure(data=[actual_trace, forecast_trace] if forecast_data else [actual_trace], layout=layout)

    # Return figure as JSON for frontend
    return jsonify(fig.to_dict())



if __name__ == '__main__':
    app.run(debug=True)
