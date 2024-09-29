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
	

SELECT
	*
FROM
	information_schema.tables
WHERE
	table_schema = 'marts';
	

SELECT * FROM marts.views_per_date;




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


  
  
  
  
  






