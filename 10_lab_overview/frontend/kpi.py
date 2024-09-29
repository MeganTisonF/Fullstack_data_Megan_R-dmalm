import streamlit as st
from utils.query_database import QueryDatabase


class ContentKPI:
    def __init__(self) -> None:
        self._content = QueryDatabase("SELECT * FROM marts.content_view_time;").df

    def display_content(self):
        df = self._content
        st.markdown("## KPIer för videor")
        st.markdown("Nedan visas KPIer för totalt antal")


        kpis = {
            "videor": len(df),
            "visade timmar": df["Visningstid_timmar"].sum(),
            "prenumeranter": df["Prenumeranter"].sum(),
            "exponeringar": df["Exponeringar"].sum(),
        }

        for col, kpi in zip(st.columns(len(kpis)), kpis):
            with col: 
                st.metric(kpi, round(kpis[kpi]))

        st.dataframe(df)


class StaderKPI:
    def __init__(self) -> None:
        # Använd COALESCE för att ersätta NULL-värden med "Okänd Ort"
        query = """
        SELECT
            COALESCE("Ort", 'Okänd ort') AS "Ort",
            "Visningar",
            "Visningstid (timmar)"
        FROM
            marts.content_stader_viewers;
        """
        self.stader_content = QueryDatabase(query).df
    
    def display_stad(self):
        # Visa innehållet endast när sidan "Stad" är vald
        st.write(self.stader_content)

        stad_df = self.stader_content

        # Välj en ort, inklusive "Okänd Ort"
        selected_stad = st.selectbox("Välj en stadskategori:", stad_df["Ort"].unique())

        # Filtrera datan baserat på användarens val
        filtered_stad_df = stad_df[stad_df["Ort"] == selected_stad]  

        # Visa data för den valda staden
        if not filtered_stad_df.empty:
            st.markdown(f"### Data för stadskategori: {selected_stad}")
            st.write(f"- Antal visningar: {filtered_stad_df['Visningar'].values[0]}")
            st.write(f"- Visningstid: {filtered_stad_df['Visningstid (timmar)'].values[0]}")



      
               
class AgeGenderKPI:
    def __init__(self) -> None:
        self._gender_content = QueryDatabase("SELECT * FROM marts.content_gender_viewers").df
        self._age_content = QueryDatabase("SELECT * FROM marts.content_age_viewers").df

    def display_gender_age(self):
        gender_df = self._gender_content
        age_df = self._age_content

        # st.dataframe(gender_df)
        # st.dataframe(age_df)

        age_kpis = {
            "Tittarnas kön": age_df["Ålder"],
            "Genomsnittlig visningslängd": age_df["Genomsnittlig visningslängd"],
            "Genomsnittlig procent som har visats": age_df["Genomsnittlig_%_visat"],
        }

        gender_kpis = {
            "Tittarnas ålder": gender_df["Kön"],
            "Genomsnittlig visningslängd": gender_df["Genomsnittlig visningslängd"],
            "Genomsnittlig procent som har visats": gender_df["Genomsnittlig_%_visat"],
        }



        # Låter användaren välja en viss könskategori från selectbox
        st.markdown("##### (KPI) analys baserat på kön:")
        selected_age = st.selectbox("Välj en könskategori:", age_df["Ålder"].unique())

        # Filtrera datan baserat på användarens val
        filtered_age_df = age_df[age_df["Ålder"] == selected_age]

        # Visa data för den valda könskategorin
        if not filtered_age_df.empty:
            st.markdown(f"##### Data baserat på kön: {selected_age}")
            st.write(f"- Genomsnittlig visningslängd: {filtered_age_df['Genomsnittlig visningslängd'].values[0]}")
            st.write(f"- Genomsnittlig procent som har visats: {filtered_age_df['Genomsnittlig_%_visat'].values[0]}")

        

        st.markdown("##### (KPI) analys baserat på ålder:")
        selected_gender = st.selectbox("Välj en ålderskategori:", gender_df["Kön"].unique())

        # Filtrera datan baserat på användarens val
        filtered_gender_df = gender_df[gender_df["Kön"] == selected_gender]

        # Visa data för den valda ålderskategorin
        if not filtered_gender_df.empty:
            st.markdown(f"##### Data baserat på ålderskategori: {selected_gender}")
            st.write(f"- Genomsnittlig visningslängd: {filtered_gender_df['Genomsnittlig visningslängd'].values[0]}")
            st.write(f"- Genomsnittlig procent som har visats: {filtered_gender_df['Genomsnittlig_%_visat'].values[0]}")

        

   
    
    
        
        


                                
