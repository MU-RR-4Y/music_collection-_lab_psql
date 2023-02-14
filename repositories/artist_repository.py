from db.run_sql import run_sql
from models.artist import Artist
from models.album import Album


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
    results = run_sql(sql,values)[0]
    if results:
        artist = Artist(results['name'], results['age'], results['id'])
    return artist





# DELETE ARTISTS
def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM artists WHERE id = %s" 
    values = [id]
    run_sql(sql, values)



# EDIT ARTISTS

def update(artist):
    sql = """UPDATE artists SET (name, age) = (%s, %s) WHERE id = %s"""
    values =[artist.name, artist.age, artist.id]
    run_sql(sql,values)


# LIST OF ALBUMS PER USER
def albums(artist):
    albums=[]
    sql ='SELECT * FROM albums WHERE artist_id = %s'
    values =[artist.id]    
    results = run_sql(sql,values)
    for row in results:
        album = Album(row['name'], row['songs'], row['genre'], artist, row['id'] )
        albums.append(album)
    return albums 


