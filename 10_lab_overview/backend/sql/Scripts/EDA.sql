DESC;



/*Det skapar två temporära tabeller: en med data från datum.tabelldata (utan den första raden) och en annan med data från datum.totalt.Det väljer och formaterar datumen, hämtar visningsantal och visningstid*/
/*Det kombinerar dessa data med en LEFT JOIN för att få all information från date_total och eventuell matchande information från date_table, vilket ger en översikt över visningar och visningstid för de olika datumen*/

WITH 
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
   
   
   
   
   
   
   
/*Räknar antalet rader ( total_rows) och sommarvisningarna ( total_visningar) för varje typ av enhet i tabellen enhetstyp.diagramdata */
/*Hämtar resultatet från CTE(Enhetstyp)
och sorterar det baserat på det totala antalet visningar i fallande ordning, vilket visar vilken enhetstyp som har flest visningar överst*/
   
  
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







/*Hämtar alla kolumner utom kolumnen Innehåll från tabtabelldata*/
/*Den sorterar raderna i tabellen baserat påvisningstid (timmar)*/

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


   
/*Skapar två temporära tabeller som sedan hämtas från tittare.tabelldata_kon/tittar.tabelldata_alder*/
/*Visar resultat baserat på tittarnas ålder*/  
   
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





/*Skapar två temporära tabeller som sedan hämtas från tittare.tabelldata_kon/tittar.tabelldata_alder*/
/*Visar resultat baserat på kön*/

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




	
	





/*Kombinerar data från två källor: en som summerar visningar per datum och en som listar visningsinformation per stad, och presenterar detta i en sammanställd vy.*/

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
    
    












