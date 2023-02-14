import pdb
from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

# delete prior entries of artist in DB
artist_repository.delete_all()
album_repository.delete_all()

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






# Return results in terminal to valiadate
result = artist_repository.select_all()
for artist in result:
    print(artist.__dict__)

result = album_repository.select_all()
for album in result:
    print(album.__dict__)

pdb.set_trace()