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
streamlit.multiselect("Pick some fruits:", list(my_world_building_assets.index))

# Display the table on the page.
streamlit.dataframe(my_world_building_assets)
