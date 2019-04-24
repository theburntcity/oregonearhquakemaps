import geopandas as gpd 
from  datawrangling.misc.config import config
# from misc.config import config
import psycopg2
import json
import pandas as pd 
from pandas.io.json import json_normalize
import os
from  pprint import pprint
from shapely.geometry import Point

# find the file and open it 
file1 = os.path.join(r'datawrangling\usgsdata', 'newusgs.json')
with open(file1, 'r') as f1:
    data = json.load(f1)
df = json_normalize(data['features'])
df[['lon','lat', 'depth']] = pd.DataFrame(df['geometry.coordinates'].values.tolist())
df['Coordinates'] = list(zip(df.lon, df.lat))
df['Coordinates'] = df['Coordinates'].apply(Point)

# create connection 
conn = None
try:
    # read config parameters
    params = config()
    # connect to the PostgreSQL server
    # print('Connecting to the PostgreSQL database...')
    conn = psycopg2.connect(**params)
    # create query for oregon shapefile
    sql ="""
    select * 
    from oregon 
    """
    # procces sql from the database
    oregon = gpd.read_postgis(sql, conn, geom_col='geom')
    # create the geodataframe
    geodf = gpd.GeoDataFrame(df, geometry='Coordinates')
    # add the projection
    geodf.crs = {'init' :'epsg:4326'}
    oqh = gpd.sjoin(geodf, oregon, how="inner", op='intersects')
    g2 =  oqh[oqh['properties.mag'] > 2]
    g3half = oqh[oqh['properties.mag'] > 3.5]
    depthm3half = oqh[(oqh['properties.mag'] > 3.5) & (oqh['depth'] < 10)]

# error with the database
except (Exception, psycopg2.DatabaseError) as error:
        print(error)
# closing time for the database
finally:
        if conn is not None:
                conn.close()
                # print('Database connection closed.')

