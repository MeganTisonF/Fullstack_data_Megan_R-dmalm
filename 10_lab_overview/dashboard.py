import streamlit as st
from frontend.kpi import ContentKPI, AgeGenderKPI, StaderKPI
from frontend.graphs import ViewsTrend, ViewGender, ViewAge
from pathlib import Path

# Instansiera klasserna
content_kpi = ContentKPI()
views_graph = ViewsTrend()
age_kpi = AgeGenderKPI()
stad_kpi = StaderKPI()
gender_graph = ViewGender()
age_graph = ViewAge()



def layout():
    
    sida1, sida2, sida3, sida4 = st.tabs(["Översikt", "Publik", "Videoinnehåll", "Orter"])

    with sida1:        
         st.header("The data driven youtuber")
         st.markdown("Denna dashboard syftar till att utforska och analysera datan från min YouTube-kanal. Genom att använda olika visualiseringar och KPI (Key Performance Indicators) kan jag få en djupare förståelse för hur mina videor presterar, vilka målgrupper som engagerar sig mest, och vilka typer av innehåll som resonerar bäst med mina tittare.")


    with sida2:
         st.header("Publikens KPier baserat på kön och ålder")
         age_kpi.display_gender_age()
         gender_graph.display_gender_pie()
         age_graph.display_age_pie()
         
        
        
    with sida3:
        st.header("KPIer för videor")
        st.markdown("Nedan visas sammanfattning för totala antal")
        content_kpi.display_content()
        views_graph.display_plot()

    with sida4:
        st.header("KPIer för orter")
        stad_kpi.display_stad()
    

if __name__ == "__main__":
    layout()


