import json
import os
import shutil
songsdict = {"library": []}

def save(data,file="Library/Library.json"):
  with open(file, 'w') as f:
    json.dump(data, f)
    f.close()

libdir = "Library/"
isExist = os.path.exists(libdir)
if isExist == False:
  os.makedirs("Library/Artists")

if os.path.exists(libdir + "Library.json") == False:
  libraryjson = open(libdir + "Library.json", "w")
  songsdict = {"library": []}
  save(songsdict)

def addsong(song, album, artist, location):
  os.makedirs("Library/Artists/" + artist + "/" + album)
  if os.path.exists(location):
    shutil.move(location, "Library/Artists/" + artist + "/" + album)
    songsdict["library"].append([{
      "song": song,
      "album": album,
      "artist": artist,
      "file": "Library/Artists/"+"/"+artist+"/"+album+"/"+location
    }])
    save(songsdict)

if os.path.exists(libdir + "Library.json") == False:
  libraryjson = open(libdir + "Library.json", "w")
  songsdict = {"library": []}
  save(songsdict)

def addsongmenu():
  print("Adding Song. Fill Out These!")
  print("Your Song WILL Be Moved")
  songname = input("Song Name: ")
  albumname = input("Album Name: ")
  artistname = input("Artist Name: ")
  filelocation = input("File Location: ")
  addsong(songname,albumname,artistname,filelocation)

