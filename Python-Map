import folium
import os

# create map object
m = folium.Map(location=[40.73061, -73.935242], zoom_start=12)

# global tooltip
tooltip = "Click For More Info"

# create custom marker icon
newyorkIcon = folium.features.CustomIcon('new york.png', icon_size=(50, 50))
sanfranciscoIcon = folium.features.CustomIcon('san francisco.png', icon_size=(50, 50))
bostonIcon = folium.features.CustomIcon('boston.png', icon_size=(50, 50))
miamiIcon = folium.features.CustomIcon('miami.png', icon_size=(50, 50))
chicagoIcon = folium.features.CustomIcon('chicago.png', icon_size=(50, 50))
losangelesIcon = folium.features.CustomIcon('los angeles.png', icon_size=(50, 50))
lasvegasIcon = folium.features.CustomIcon('las vegas.png', icon_size=(50, 50))
dallasIcon = folium.features.CustomIcon('dallas.png', icon_size=(50, 50))
denvorIcon = folium.features.CustomIcon('denvor.png', icon_size=(50, 50))
detroitIcon = folium.features.CustomIcon('detroit.png', icon_size=(50, 50))
pennIcon = folium.features.CustomIcon('penn.png', icon_size=(50, 50))
phoenixIcon = folium.features.CustomIcon('phoenix.png', icon_size=(50, 50))
washingtondcIcon = folium.features.CustomIcon('washington dc.png', icon_size=(50, 50))
seattleIcon = folium.features.CustomIcon('seattle.png', icon_size=(50, 50))
atlantaIcon = folium.features.CustomIcon('atlanta.png', icon_size=(50, 50))

# geojson data
newyork = os.path.join('geo', newyork.json)
atlanta = os.path.join('geo', atlanta.json)
chicago = os.path.join('geo', chicago.json)
dallas = os.path.join('geo', dallas.json)
detroit = os.path.join('geo', detroit.json)
lasvegas = os.path.join('geo', lasvegas.json)
losangeles = os.path.join('geo', losangeles.json)
sanfrancisco = os.path.join('geo', sanfrancisco.json)
washingtondc = os.path.join('geo', washingtondc.json)
penn = os.path.join('geo', penn.json)
seattle = os.path.join('geo', seattle.json)
boston = os.path.join('geo', boston.json)
denvor = os.path.join('geo', denvor.json)
phoenix = os.path.join('geo', phoenix.json)
miami = os.path.join('geo', miami.json)

# create markers
folium.Marker([40.730610, -73.935242],
              popup='<strong>New York City</strong>',
              tooltip=tooltip,
              icon=newyorkIcon).add_to(m),

folium.Marker([42.331429, -83.045753],
              popup='<strong>Detroit</strong>',
              tooltip=tooltip,
              icon=detroitIcon).add_to(m),

folium.Marker([34.052235, -118.243683],
              popup='<strong>Los Angeles</strong>',
              tooltip=tooltip,
              icon=losangelesIcon).add_to(m),

folium.Marker([41.203323, -77.194527],
              popup='<strong>Pennsylvania</strong>',
              tooltip=tooltip,
              icon=pennIcon).add_to(m),

folium.Marker([33.448376, -112.074036],
              popup='<strong>Phoenix</strong>',
              tooltip=tooltip,
              icon=phoenixIcon).add_to(m),

folium.Marker([47.608013, -122.335167],
              popup='<strong>Seattle</strong>',
              tooltip=tooltip,
              icon=seattleIcon).add_to(m),

folium.Marker([41.881832, -87.623177],
              popup='<strong>Chicago</strong>',
              tooltip=tooltip,
              icon=chicagoIcon).add_to(m),

folium.Marker([36.114647, -115.172813],
              popup='<strong>Las Vegas</strong>',
              tooltip=tooltip,
              icon=lasvegasIcon).add_to(m),

folium.Marker([25.761681, -80.191788],
              popup='<strong>Miami</strong>',
              tooltip=tooltip,
              icon=miamiIcon).add_to(m),

folium.Marker([39.742043, -104.991531],
              popup='<strong>Denver</strong>',
              tooltip=tooltip,
              icon=denvorIcon).add_to(m),

folium.Marker([42.361145, -71.057083],
              popup='<strong>Boston</strong>',
              tooltip=tooltip,
              icon=bostonIcon).add_to(m),

folium.Marker([33.753746, -84.38633],
              popup='<strong>Atlanta</strong>',
              tooltip=tooltip,
              icon=atlantaIcon).add_to(m),

folium.Marker([32.89748, -97.040443],
              popup='<strong>Dallas</strong>',
              tooltip=tooltip,
              icon=dallasIcon).add_to(m),

folium.Marker([37.773972, -122.431297],
              popup='<strong>San Francisco</strong>',
              tooltip=tooltip,
              icon=sanfranciscoIcon).add_to(m),

folium.Marker([38.889931, -77.009003],
              popup='<strong>Washington DC</strong>',
              tooltip=tooltip,
              icon=washingtondcIcon).add_to(m),

# geojson
folium.GeoJson(newyork, name='New York').add_to(m)

# generate map
m.save('map.html')
