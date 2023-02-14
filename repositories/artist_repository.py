from db.run_sql import run_sql
from models.artist import Artist


# CREATE AND SAVE ARTIST
def save(artist):
    sql ="""INSERT INTO artists (name, age)
        VALUES (%s, %s)
        RETURNING id """
    values = [artist.name, artist.age]
    results = run_sql(sql,values)
    artist.id = results[0]['id']
    return artist


# FIND ARTISTS
def select_all():  
    artists = [] 
    sql = "SELECT * FROM artists"
    results = run_sql(sql)
    for row in results:
        artist = Artist(row['name'], row['age'], row['id'] )
        artists.append(artist)
    return artists 

def select(id):
    artist = None
    sql = """SELECT * FROM artists WHERE id = %s"""
    values = [id]
    results = run_sql(sql,values)
    if results:
        result = results[0]
        artist = Artist(result['name'], result['age'], result['id'])
    return artist





# DELETE ARTISTS
def delete_all():
    sql = "DELETE  FROM artists"
    run_sql(sql)