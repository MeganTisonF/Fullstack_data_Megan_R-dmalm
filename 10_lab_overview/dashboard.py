import streamlit as st
from frontend.kpi import ContentKPI, AgeGenderKPI, StaderKPI
from frontend.graphs import ViewsTrend, ViewGender, ViewAge, ScreenView
from pathlib import Path

# Instansiera klasserna
content_kpi = ContentKPI()
views_graph = ViewsTrend()
age_kpi = AgeGenderKPI()
stad_kpi = StaderKPI()
gender_graph = ViewGender()
age_graph = ViewAge()
screen_view=ScreenView()



def layout():
    
    sida1, sida2, sida3, sida4 = st.tabs(["Översikt", "Publik", "Videoinnehåll", "Orter"])

    with sida1:        
         st.markdown(
            """
            <div class="custom-tab-1">
            <h1 class="custom-header">The data driven youtuber</h1>
            <p class="p-h">Denna dashboard syftar till att utforska och analysera datan från min YouTube-kanal. Genom att använda olika visualiseringar och KPI (Key Performance Indicators) kan jag få en djupare förståelse för hur mina videor presterar, vilka målgrupper som engagerar sig mest, och vilka typer av innehåll som resonerar bäst med mina tittare.</p>
            </div>
            """, unsafe_allow_html=True
            )
         st.image("10_lab_overview/images/KPI.jpg", use_column_width=True)
         
         
         
         
    with sida2:
         st.header("Publikens KPier baserat på kön och ålder")
         age_kpi.display_gender_age()
         gender_graph.display_gender_pie()
         age_graph.display_age_pie()
         
        
        
    with sida3:
        content_kpi.display_content()
        views_graph.display_plot()
        screen_view.display_screenview_pie()

    with sida4:
        st.header("KPIer för orter")
        stad_kpi.display_stad()
    
   
    read_css()

def read_css():
    css_path = Path(__file__).parent / "style.css"

    with open(css_path) as css:
        st.markdown(f"<style> {css.read()}</style>", unsafe_allow_html=True)




if __name__ == "__main__":
    layout()




