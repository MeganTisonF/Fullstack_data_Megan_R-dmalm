DESC;


WITH 
/*Det skapar två temporära tabeller: en med data från datum.tabelldata (utan den första raden) och en annan med data från datum.totalt.Det väljer och formaterar datumen, hämtar visningsantal och visningstid*/
/*Det kombinerar dessa data med en LEFT JOIN för att få all information från date_total och eventuell matchande information från date_table, vilket ger en översikt över visningar och visningstid för de olika datumen*/
date_table AS (
    SELECT * FROM datum.tabelldata OFFSET 1
),
date_total AS (
    SELECT * FROM datum.totalt
)
SELECT
    STRFTIME('%Y-%m-%d', tot.datum) AS formaterat_datum,
    tot.visningar AS total_visningar,
    tab.visningar AS tabell_visningar,
    tab."visningstid (timmar)"
FROM
    date_total AS tot
LEFT JOIN
    date_table AS tab  
ON
    tot.datum = tab.datum;
   

   
  
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






   SELECT
	* EXCLUDE (Innehåll)
FROM
	innehall.tabelldata
ORDER BY "visningstid (timmar)" DESC;



-- Datum och visningar
SELECT 
    STRFTIME('%Y-%m-%d', Datum) AS formaterat_datum,
    Visningar
FROM
    innehall.totalt;


   
WITH age_table AS (
SELECT
	*
FROM
	tittare.tabelldata_alder),
	gender_table AS (
SELECT
	*
FROM
	tittare.tabelldata_kon) -- schema.name
SELECT
	*
FROM
	gender_table;


WITH gender_table AS (
SELECT
	*
FROM
	tittare.tabelldata_kon),
age_table AS (
SELECT
	*
FROM
	tittare.tabelldata_alder)
SELECT
	*
FROM
	age_table;




WITH cities_table AS (
SELECT
	*
FROM
	stader.tabelldata),
date_table AS (
SELECT
	*
FROM
	stader.totalt)
SELECT
	*
FROM
	date_table
	
	
	
SELECT * FROM stader.tabelldata LIMIT 1;



WITH 
cities_table AS (
    SELECT 
        "Ort",                                 
        "Visningar",                         
        "Visningstid (timmar)",                  
    FROM
        stader.tabelldata
),
dates_cities_table AS (
    SELECT 
        datum,
        SUM(visningar) AS totalt_visningar  
    FROM
        stader.totalt
    GROUP BY
        datum
)
SELECT
    STRFTIME('%Y-%m-%d', dt.datum) AS formaterat_datum,
    dt.totalt_visningar,
    cities.Ort,                                  
    cities.Visningar,
    cities."Visningstid (timmar)",                       
FROM
    dates_cities_table AS dt,
    cities_table AS cities; 
    
    












