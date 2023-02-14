import pdb
from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

# delete prior entries of artist in DB - album delete needs to be called 1st as it requires artist!!
album_repository.delete_all()
artist_repository.delete_all()

# add artists using.save()
artist_1 = Artist('Dave', 30)
artist_2 = Artist('Rick', 28)
artist_repository.save(artist_1)
artist_repository.save(artist_2)

# add albums using .save()
album_1 = Album('Dave The Album',10, 'Rock',artist_1)
album_2 = Album('The Sequel of Dave',15, 'Power Ballads',artist_1)
album_3 = Album('Dave no more',5,'Soul', artist_1)

album_4 = Album('The sounds of Rick', 15, 'Country', artist_2)
album_5 = Album("Rick's Pop Experience", 15, 'Pop', artist_2)
album_6 = Album('Rick Returns', 12, 'Country', artist_2)

album_repository.save(album_1)
album_repository.save(album_2)
album_repository.save(album_3)
album_repository.save(album_4)
album_repository.save(album_5)
album_repository.save(album_6)


print('Return results fo select_all() to valiadate')
print('----ARTISTS----')
result = artist_repository.select_all()
for artist in result:
    print(artist.__dict__)
print('----ALBUMS----')
result = album_repository.select_all()
for album in result:
    print(album.__dict__)

print('-------------------------------')
print('Return results for select by ID')
print('-------------------------------')
artist = artist_repository.select(2)
print(artist.__dict__)
   
album =album_repository.select(4)
print(album.__dict__)

print('--------------------------')
print('Return results for update')
print('--------------------------')

artist_1.name ='Tom'
artist_1.age = 35
artist_repository.update(artist_1)
print(artist_1.__dict__)

album_1.name = 'A soundtrack to Tom'
album_1.songs = 5
album_1.genre = 'Motown'
album_1.artist = artist_1

print(album_1.__dict__)

print('----------------------------------------------------------------')
print('Return results for list of songs per artist - requested for Rick')
print('----------------------------------------------------------------')

albums = artist_repository.albums(artist_2)
for album in albums:
    print(album.__dict__)


pdb.set_trace()