import streamlit

streamlit.title('AR/VR Overview: Predictions and Projects Over the Next 5 Years')

streamlit.header('Compute')
streamlit.text('🥭External🥭')
streamlit.text('🥝Internal🥝')
streamlit.text('🍇Wireless/5g🍇')

streamlit.header('World Building Assets')

import pandas
my_world_building_assets = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_world_building_assets = my_world_building_assets.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
assets_selected = streamlit.multiselect("Pick some fruits:", list(my_world_building_assets.index),['Avocado','Strawberries'])
assets_to_show = my_world_building_assets.loc[assets_selected]

# Display the table on the page.
streamlit.dataframe(assets_to_show)


#New section to display fruityvice api response
import requests
fruitvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(frutivice_response)
