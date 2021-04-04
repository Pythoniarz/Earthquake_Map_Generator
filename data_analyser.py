import requests

import json

import datetime

from plotly.graph_objs import Layout
from plotly import offline


def create_eq_map(eq_mag, eq_time_past):
    # Pobranie i załadowanie pliku GeoJSON zawierającego informacje o trzęsieniach ziemi.
    url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/{}_{}.geojson'.format(eq_mag, eq_time_past)

    req = requests.get(url)
    url_content = req.content
    csv_file = open('downloaded.json', 'wb')

    csv_file.write(url_content)
    csv_file.close()

    filename = 'downloaded.json'
    with open(filename, encoding='utf-8') as f:
        all_eq_data = json.load(f)

    # Analiza danych JSON.
    all_eq_dicts = all_eq_data['features']

    mags, lons, lats, hover_texts = [], [], [], []
    for eq_dict in all_eq_dicts:
        mag = eq_dict['properties']['mag']
        lon = eq_dict['geometry']['coordinates'][0]
        lat = eq_dict['geometry']['coordinates'][1]
        title = eq_dict['properties']['title']
        time = eq_dict['properties']['time'] / 1000
        formatted_time = datetime.datetime.fromtimestamp(time).strftime('%d-%m-%Y %H:%M:%S')
        hover_text = title + "<br>" + formatted_time
        mags.append(mag)
        lons.append(lon)
        lats.append(lat)
        hover_texts.append(hover_text)

    # Mapa trzęsień ziemi.
    data = [{
        'type': 'scattergeo',
        'lon': lons,
        'lat': lats,
        'hovertext': hover_texts,
        'marker': {
            'size': [mag ** 2 for mag in mags],
            'color': mags,
            'colorscale': 'Inferno',
            'reversescale': True,
            'colorbar': {'title': 'Magnitude'},
        }
    }]
    my_layout = Layout(title='Earthquakes with magnitude over {} during past {}'
                       .format(eq_mag, eq_time_past))

    fig = {'data': data, 'layout': my_layout}
    offline.plot(fig, filename='global_earthquakes.html')
