import socket


class Song:
    def __init__(self,s):
        self.songName = s.split('::')[0]
        self.songWriter = s.split('::')[1]
        self.duration = s.split('::')[2]
        self.lyrics = s.split('::')[3]

    def __str__(self):
        return f"{self.songName} by {self.songWriter} - {self.duration}:\n{self.lyrics}"


class Album:
    def __init__(self, s):
        self.albumName = s.split('\n')[0]
        self.songs = []

    def appendSong(self,song_class):
        self.songs.append(song_class)

    def __str__(self):
        return self.albumName


def parsing(albums_lst):
    file = open('pink_floyd_db.txt', 'r').read()

    albums = file.split('#')
    for album in albums:
        if album == ' ' or album == '':
            continue
        currAlbumClass = Album(album)
        songs = album.split('*')[1:]
        for song in songs:
            currSongClass = Song(song)
            currAlbumClass.appendSong(currSongClass)

        albums_lst.append(currAlbumClass)

    return albums_lst


def debug_parsing(albums_lst):
    for album in albums_lst:
        print(album.albumName)
        print('############################')
        for song in album.songs:
            print(song)
            print('-------------------------------')


def song_name_by_lyrics(st, albums_lst):

    for album in albums_lst:
        for song in album.songs:
            if st in song.lyrics.lower():
                return song.songName

    return '404 - Not Found'


def songs_by_album(st, albums_lst):

    songs_res = []

    for album in albums_lst:
        if st == album.albumName.lower():
            for song in album.songs:
                songs_res.append(song.songName)

    if len(songs_res) > 0:
        songs_res = ', '.join(songs_res)
        return songs_res

    return '404 - Not Found'


def duration_by_song(st, albums_lst):

    for album in albums_lst:

        for song in album.songs:
            if st == song.songName.lower():
                return song.duration

    return '404 - Not Found'


def lyrics_by_song(st, albums_lst):

    for album in albums_lst:

        for song in album.songs:
            if st == song.songName.lower():
                return song.lyrics

    return '404 - Not Found'


def songWriter_by_song(st, albums_lst):

    for album in albums_lst:

        for song in album.songs:
            if st == song.songName.lower():
                return song.songWriter

    return '404 - Not Found'


def server_program():

    albums_lst = []
    albums_lst = parsing(albums_lst)

    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))

    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break

        choice = data[:3]
        param = data[3:]
        print("from connected user: " + str(data))

        if choice == 'SNG':
            data = song_name_by_lyrics(param, albums_lst)

        elif choice == 'ALM':
            data = songs_by_album(param, albums_lst)

        elif choice == 'DUR':
            data = duration_by_song(param, albums_lst)

        elif choice == 'LYR':
            data = lyrics_by_song(param, albums_lst)

        elif choice == 'WRT':
            data = songWriter_by_song(param, albums_lst)

        conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()