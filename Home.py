import streamlit as st
from PIL import Image 

st.set_page_config(
    page_title="Home",
    page_icon="🎯"
)

#image_path = 'C:/Users/Ian/OneDrive/Área de Trabalho/PROJETO_PRATICO_01_MANUAL_ENG_DADOS/images/'
image = Image.open( 'cury.png' )
st.sidebar.image( image, width=120 )

st.sidebar.markdown('### Cury company')
st.sidebar.markdown ('## Fastest Delivery in Town')
st.sidebar.markdown ("""---""")

st.write( "# Cury Company Growth Dashboard" )

st.markdown(
    """
    Growth dashboard was built to monitor the growth metrics of delivery drivers and restaurants.

    How to use this growth dashboard?
    
    -Company view:
    
        -Management view: Overall behavioral metrics. 
        
        -Tatical view: Weekly growth metrics.
        
        -Geographical view: Geolocation insights.
        
    -Delivery driver view:
    
        -Monitor the weekly growth metrics.
        
    -Restaurant view:
    
        -Weekly growth metrics.
        
    ### Ask for Help
    
    -discord:
    
    @iannfava
    
""" )        




