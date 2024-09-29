from utils.query_database import QueryDatabase
import plotly.express as px
import streamlit as st 
from backend.constants import Color 

class ViewsTrend:
    def __init__(self) -> None:
        self.df = QueryDatabase("SELECT * FROM marts.views_per_date").df
        self.stader_content = QueryDatabase("SELECT * FROM marts.content_stader_viewers").df
        print(self.df)

    def display_plot(self):
        fig = px.line(self.df, x="Datum", y="Visningar")
        st.markdown("## Antal visningar under senaste månaden")
        st.plotly_chart(fig)

        fig.update_traces(
        line=dict(
            width=4,
            color=Color.PRIMARY)) 




class ViewGender:
    def __init__(self) -> None:
        self._gender_content = QueryDatabase("SELECT * FROM marts.content_gender_viewers").df
        print(self._gender_content)

    def display_gender_pie(self):
        # Cirkeldiagram för visningsandelar baserat på kön
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
        # Cirkeldiagram för visningsandelar baserat på åldersgrupper
        fig_age_pie = px.pie(self._age_content, 
                             names="Ålder", 
                             values="Visningar_%") 
        st.markdown("### Visningsandelar baserat på åldersgrupper")
        st.plotly_chart(fig_age_pie)

    




# create more graphs here

