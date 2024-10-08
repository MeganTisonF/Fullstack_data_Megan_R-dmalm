SELECT
	*
FROM
	information_schema.schemata
WHERE
	catalog_name = 'youtube_data';

CREATE SCHEMA IF NOT EXISTS marts;

CREATE TABLE IF NOT EXISTS marts.content_view_time AS
(
SELECT
	Videotitel,
	"Publiceringstid för video" AS Publiceringstid,
	Visningar,
	"Visningstid (timmar)" AS Visningstid_timmar,
	Exponeringar,
	Prenumeranter,
	"Klickfrekvens för exponeringar (%)" AS "Klickfrekvens_exponering_%"
FROM
	innehall.tabelldata
ORDER BY
	"Visningstid (timmar)" DESC OFFSET 1
);


SELECT * FROM marts.content_view_time;


CREATE TABLE IF NOT EXISTS marts.views_per_date AS (
SELECT
	STRFTIME('%Y-%m-%d',
	Datum) AS Datum,
	Visningar
FROM
	innehall.totalt);



SELECT * FROM marts.views_per_date;



SELECT
	*
FROM
	information_schema.tables
WHERE
	table_schema = 'marts';
	




CREATE TABLE IF NOT EXISTS marts.content_screens AS
WITH diagram_data AS (
    SELECT 
        Enhetstyp, 
        COUNT(*) AS total_rows,  
        SUM(Visningar) AS total_visningar  
    FROM enhetstyp.diagramdata
    GROUP BY Enhetstyp
)
SELECT 
    Enhetstyp,
    total_rows,
    total_visningar
FROM diagram_data
ORDER BY total_visningar DESC;

  
SELECT * FROM marts.content_screens;






	




CREATE TABLE IF NOT EXISTS marts.content_stader_viewers AS (
    SELECT
        COALESCE("Ort", 'Okänd ort') AS "Ort",
        "Visningar",
        "Visningstid (timmar)"
        
    FROM
        stader.tabelldata
);




SELECT * FROM marts.content_stader_viewers;








CREATE TABLE IF NOT EXISTS marts.content_gender_viewers AS (
SELECT 
    "Tittarnas ålder" AS "Kön",
    "Visningar (%)" AS "Visningar_%",
    "Genomsnittlig visningslängd",
    "Genomsnittlig procent som har visats (%)" AS "Genomsnittlig_%_visat",
    "Visningstid (timmar) (%)" AS "Visningstid_timmar_%"
FROM 
    tittare.tabelldata_kon
ORDER BY
    "Kön");
   
 
   
   SELECT * FROM marts.content_gender_viewers;

  

  
  
  
  
  

CREATE TABLE IF NOT EXISTS marts.content_age_viewers AS (
SELECT 
    "Tittarnas kön" AS "Ålder",
    "Visningar (%)" AS "Visningar_%",
    "Genomsnittlig visningslängd",
    "Genomsnittlig procent som har visats (%)" AS "Genomsnittlig_%_visat",
    "Visningstid (timmar) (%)" AS "Visningstid_timmar_%"
FROM 
    tittare.tabelldata_alder);
   
   
   SELECT * FROM marts.content_age_viewers;


  
  
  

  







