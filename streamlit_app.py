import streamlit

streamlit.title('AR/VR Overview: Predictions and Projects Over the Next 5 Years')

streamlit.header('Compute')
streamlit.text('🥭External🥭')
streamlit.text('🥝Internal🥝')
streamlit.text('🍇Wireless/5g🍇')

streamlit.header('World Building')

import pandas
my_world_building_assets = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt)

streamlit.dataframe(my_world_building_assets)
