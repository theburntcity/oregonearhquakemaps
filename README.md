# oregonearhquakemaps

<p>The All link opens new page that shows all the earthquakes within Oregon.</p>
<p>The G2 link link opens new page that shows all the earthquakes within Oregon that are magnitude greater than 2 </p>
<p>The 3ghalf link link opens new page that shows all the earthquakes within Oregon that are magnitude greater than 3.5</p>
<p>The G2 link link opens new page that shows all the earthquakes within Oregon that are magnitude greater than 3.5 and depth less than 10 km.</p>
<p>The source for the earthquake data is from <a href="https://earthquake.usgs.gov/earthquakes/search/" target="blank">USGS--Search Earthquake Catalog</a></p>
<p>Python libraries used:
    <ol>
        <li>flask using: Flask, render_template, and url_for.</li>
        <li>Pandas using: DataFrame, IO.io.json--normalize_json</li>
        <li>Geopandas using: GeoDataFrame</li>
        <li>Json using: dump, load</li>
        <li>psycopg2 using it in general.</li>
        <li>Shapely.geometry using the Point.</li>
        <li>Folium using LayerControl, Map, FeatureGroup and the plugin Heatmap.</li>
        <li>os using path</li>

    </ol>
</p>