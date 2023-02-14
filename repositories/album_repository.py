from db.run_sql import run_sql
from models.album import Album
import repositories.artist_repository as artist_repository


# CREATE AND SAVE AlBUM

def save(album):
    sql ="""INSERT INTO albums (name, songs, genre, artist_id)
        VALUES (%s, %s, %s,%s)
        RETURNING * """
    values = [album.name, album.songs, album.genre, album.artist.id]
    results = run_sql(sql,values)
    album.id = results[0]['id']
    return album






# FIND ALBUMS
def select_all():  
    albums = []
    sql = "SELECT * FROM albums"
    results = run_sql(sql)
    for row in results:
        artist = artist_repository.select(row['artist_id'])
        album = Album(row['name'], row['songs'],row['genre'], artist, row['id'] )
        albums.append(album)
    return albums 

def select(id):
    album= None
    sql ="SELECT * FROM albums WHERE id = %s"
    values =[id]
    results = run_sql(sql,values)
    if results:
        result = results[0]
        artist = artist_repository.select(result['artist_id'])
        album = Album(result['name'], result['songs'], result['genre'], artist, id)
    return album







# DELETE ALBUMS
def delete_all():
    sql = "DELETE  FROM albums"
    run_sql(sql)