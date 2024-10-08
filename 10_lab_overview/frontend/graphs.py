from utils.query_database import QueryDatabase
import plotly.express as px
import streamlit as st 
from backend.constants import Color 

class ViewsTrend:
    def __init__(self) -> None:
        self.df = QueryDatabase("SELECT * FROM marts.views_per_date").df
        print(self.df)

    def display_plot(self):
        fig = px.line(self.df, x="Datum", y="Visningar")
        st.markdown("## Antal visningar under senaste månaden")
        st.plotly_chart(fig)

        fig.update_traces(
        line=dict(
            width=4,
            color=Color.PRIMARY)) 

class ScreenView:
     def __init__(self) -> None:
        self._content_view_screen = QueryDatabase("SELECT * FROM marts.content_screens").df
        print(self._content_view_screen)

     def display_screenview_pie(self):
        
        fig_screenview_pie = px.pie(self._content_view_screen, 
                                 names="Enhetstyp", 
                                 values="total_visningar") 
        st.markdown("### Fördelning av visningar baserat på enhetstypen som användes av tittarna")
        st.plotly_chart(fig_screenview_pie)





class ViewGender:
    def __init__(self) -> None:
        self._gender_content = QueryDatabase("SELECT * FROM marts.content_gender_viewers").df
        print(self._gender_content)

    def display_gender_pie(self):
        
        fig_gender_pie = px.pie(self._gender_content, 
                                 names="Kön", 
                                 values="Visningar_%") 
        st.markdown("### Visningsandelar baserat på åldersgrupp")
        st.plotly_chart(fig_gender_pie)

class ViewAge:
    def __init__(self) -> None:
        self._age_content = QueryDatabase("SELECT * FROM marts.content_age_viewers").df
        print(self._age_content)

    def display_age_pie(self):
        
        fig_age_pie = px.pie(self._age_content, 
                             names="Ålder", 
                             values="Visningar_%") 
        st.markdown("### Visningsandelar baserat på åldersgrupper")
        st.plotly_chart(fig_age_pie)

    




# create more graphs here

