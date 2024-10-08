import streamlit as st
from utils.query_database import QueryDatabase


class ContentKPI:
    def __init__(self) -> None:
        self._content = QueryDatabase("SELECT * FROM marts.content_view_time").df

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
       
        stad_df = self.stader_content

        
        stad_options = ["Alternativ"] + list(stad_df["Ort"].unique())

        selected_stad = st.selectbox("Välj en ortkatergori:", stad_options)

        if selected_stad:
            filtered_stad_df = stad_df[stad_df["Ort"] == selected_stad]

            
            if not filtered_stad_df.empty:
              st.markdown(f"### Data för ortskategori: {selected_stad}")
              st.write(f"- Antal visningar: {filtered_stad_df['Visningar'].values[0]}")
              st.write(f"- Visningstid: {filtered_stad_df['Visningstid (timmar)'].values[0]}")







class AgeGenderKPI:
    def __init__(self) -> None:
        self._gender_content = QueryDatabase("SELECT * FROM marts.content_gender_viewers").df
        self._age_content = QueryDatabase("SELECT * FROM marts.content_age_viewers").df

    def display_gender_age(self):
        gender_df = self._gender_content
        age_df = self._age_content

        
        st.markdown("##### (KPI) analys baserat på kön:")

        
        gender_options = ["Alternativ"] + list(gender_df["Kön"].unique())
        selected_gender = st.selectbox("Välj en könskategori:", gender_options)

        
        if selected_gender:
            filtered_gender_df = gender_df[gender_df["Kön"] == selected_gender]

            if not filtered_gender_df.empty:
                st.markdown(f"##### Data baserat på könskategori: {selected_gender}")
                st.write(f"- Visningar i procent: {filtered_gender_df ['Visningar_%'].values[0]}")
                st.write(f"- Genomsnittlig visningslängd: {filtered_gender_df['Genomsnittlig visningslängd'].values[0]}")
                st.write(f"- Genomsnittlig procent som har visats: {filtered_gender_df['Genomsnittlig_%_visat'].values[0]}")
                st.write(f"- Visningstid i timmar i procent: {filtered_gender_df['Visningstid_timmar_%'].values[0]}")

        st.markdown("##### (KPI) analys baserat på ålder:")

        
        age_options = ["Alternativ"] + list(age_df["Ålder"].unique())
        selected_age = st.selectbox("Välj en ålderskategori:", age_options)

        
        if selected_age:
            filtered_age_df = age_df[age_df["Ålder"] == selected_age]

           
            if not filtered_age_df.empty:
                st.markdown(f"##### Data baserat på ålderskategori: {selected_age}")
                st.write(f"- Visningar i procent: {filtered_age_df ['Visningar_%'].values[0]}")
                st.write(f"- Genomsnittlig visningslängd: {filtered_age_df['Genomsnittlig visningslängd'].values[0]}")
                st.write(f"- Genomsnittlig procent som har visats: {filtered_age_df['Genomsnittlig_%_visat'].values[0]}")
                st.write(f"- Visningstid i timmar i procent: {filtered_age_df['Visningstid_timmar_%'].values[0]}")



        

   
    
    
        
        


                                
