import pdb
from models.artist import Artist
# from models.album import Album
import repositories.artist_repository as artist_repository
# import repositories.album_repository as album_repository

# delete prior entries of artist in DB
artist_repository.delete_all()

# add artists using.save()
artist_1 = Artist('Dave', 30)
artist_2 = Artist('Rick', 28)
artist_repository.save(artist_1)
artist_repository.save(artist_2)





# Return results in terminal to valiadate
result = artist_repository.select_all()
for artist in result:
    print(artist.__dict__)

pdb.set_trace()