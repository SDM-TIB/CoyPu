prefixes = """PREFIX coy: <https://schema.coypu.org/global#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX time: <http://www.w3.org/2006/time#> 
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wds: <http://www.wikidata.org/entity/statement/>
PREFIX wdv: <http://www.wikidata.org/value/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX wikibase: <http://wikiba.se/ontology#>
PREFIX p: <http://www.wikidata.org/prop/>
PREFIX ps: <http://www.wikidata.org/prop/statement/>
PREFIX pq: <http://www.wikidata.org/prop/qualifier/>
PREFIX bd: <http://www.bigdata.com/rdf#>
PREFIX wb: <http://worldbank.org/>
"""

query_0_desc = "Query0: Test query"
query_0 = prefixes + """
SELECT * WHERE{
    ?subject ?predicate ?object
}LIMIT 10
"""

query_test = prefixes + """
SELECT * WHERE{ 
    ?subject ?predicate ?object
}
LIMIT 10
"""

query_test_public_service = prefixes +"""
SELECT * WHERE { 
SERVICE <https://query.wikidata.org/sparql> {
    ?subject ?predicate ?object
}LIMIT 10
}"""

query_test_private_service = prefixes +"""
SELECT * WHERE 
{ SERVICE <https://implisense.coypu.org/dataplatform/proxy/default/sparql> 
 {<https://schema.coypu.org/acled/8909747> a ?o
}
}"""

query_test_private_service_2 = prefixes +"""
SELECT Distinct * WHERE{ 
SERVICE <https://implisense.coypu.org/dataplatform/proxy/default/sparql> {
    <https://schema.coypu.org/acled/8909747> a ?o
}
SERVICE <http://coypu-fuseki.aksw.org/country/sparql> {
    <https://data.coypu.org/country/MAR> a ?o1
}
}"""

query_test_private_public = prefixes +"""
SELECT Distinct * WHERE{ 
SERVICE <https://implisense.coypu.org/dataplatform/proxy/default/sparql> {
    <https://schema.coypu.org/acled/8909747> a ?o
}

SERVICE <https://labs.tib.eu/sdm/worldbank_endpoint/sparql> {
     <http://worldbank.org/Country/DEU> a ?o1
}
}"""


 
query_1_desc = "Query1: percentage of fatalities with respect to country population in a year"
query_1 = prefixes + """
SELECT ?isoCode ?year ((sum(?fatalities_int)/avg(?population))*100 as ?per_fatalities) (count(?iri) as ?no_of_acled_events) 
WHERE {
    ?iri a coy:AcledEvent ;
    coy:hasIsoCode ?isoCode ;
    coy:hasTimestamp ?timestamp;
    coy:hasFatalities ?fatalities.
    bind(year(?timestamp) as ?year)
    bind (xsd:integer(?fatalities) as ?fatalities_int)
    
    SERVICE <https://query.wikidata.org/sparql>
    {
        ?country_wiki wdt:P31 wd:Q3624078; 
                      wdt:P298 ?country_code_wiki;
                     p:P1082 ?p.

        ?p pq:P585 ?time;
               ps:P1082 ?population.
        bind(year(?time) as ?year_w)
        SERVICE wikibase:label {bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en".}  
    }
    filter(?year_w=?year && ?country_code_wiki=?isoCode)  
    

}group by ?isoCode ?year 
order by desc (?total_fatalities)
LIMIT 10
"""

query_1_fdq = prefixes + """
SELECT ?isoCode ?timestamp ?fatalities ?population
WHERE {
    SERVICE <https://implisense.coypu.org/dataplatform/proxy/default/sparql>{
    <https://schema.coypu.org/acled/8823191> a coy:AcledEvent ;
    coy:hasIsoCode ?isoCode ;
    coy:hasTimestamp ?timestamp;
    coy:hasFatalities ?fatalities.
    }
    SERVICE <https://query.wikidata.org/sparql>
    {
        ?country_wiki wdt:P31 wd:Q3624078; 
                      wdt:P298 'IND';
                     p:P1082 ?p.
        ?p pq:P585 ?time;
               ps:P1082 ?population.
        SERVICE wikibase:label {bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en".}
    }
    
}
"""

query_2_desc = "Query 2: Germany WB indicators for year 2021"
query_2 = prefixes + """
select ?country ?isoCode ?year ?topic ?indicator ?indicator_label ?indicator_note ?value
where {
?country a wb:AnnualIndicatorEntry;
         wb:hasTopic ?topic;
         wb:hasIndicator ?indicator;
         wb:hasCountry ?country;
         owl:hasValue ?value;        
         time:year ?year.
optional {?indicator rdfs:label ?indicator_label}
optional {?indicator skos:note  ?indicator_note }

bind(replace(str(?country),"http://worldbank.org/Country/", "") as ?isoCode )
         
filter(?year=2021 && ?country=<http://worldbank.org/Country/DEU>)
}
group by ?country ?year ?isoCode ?topic ?indicator ?indicator_label ?indicator_note
order by ?country ?isoCode ?year
limit 2000
"""



