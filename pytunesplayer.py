import json
from playsound import playsound as ps

try:
  with open('Library/Library.json') as json_file:
    library = json.load(json_file)
except:
  nolibrary = True


def showsong(id):
  if library["library"][id][0]["song"] == library["library"][id][0]["album"]:
    return library["library"][id][0]["song"] + " - " + library["library"][id][
      0]["artist"]
  else:
    return library["library"][id][0]["song"] + " - " + library["library"][id][
      0]["album"] + " - " + library["library"][id][0]["artist"]


def librarylist():
  print("ID")
  id = 0
  while True:
    try:
      if library["library"][id][0]["song"] == library["library"][id][0][
          "album"]:
        print(
          str(id+1)+" " + library["library"][id][0]["song"] + " - " +
          library["library"][id][0]["artist"])
      else:
        print(
          str(id+1)+" "+ library["library"][id][0]["song"] + " - " +
          library["library"][id][0]["album"] + " - " +
          library["library"][id][0]["artist"])
    except:
      break
    id = id + 1


def playsong(id, repl=False):
  print(id)
  if library["library"][id][0]["song"] == library["library"][id][0]["album"]:
    nowplaying = library["library"][id][0]["song"] + " - " + library[
      "library"][id][0]["artist"]
  else:
    nowplaying = library["library"][id][0]["song"] + " - " + library[
      "library"][id][0]["album"] + " - " + library["library"][id][0]["artist"]
  print("Now Playing: " + nowplaying)
  print(library["library"][id][0]["file"])
  if repl == True:
    from replit import audio
    source = audio.play_file(library["library"][id][0]["file"])
    volume = 1
    loops = 0

    print('type "up" or "down" to change volume')
    print('type "loop" to add another loop')
    print('press enter to play/pause')
    while True:
      print(f'volume is at {source.volume * 100}% with',
            f'{source.loops_remaining} loops remaining.')
      cmd = input('> ').lower()
      if cmd == 'up':
        source.volume += .25
        volume += .25
      elif cmd == 'down':
        source.volume -= .25
        volume -= .25
      elif cmd == 'loop':
        loops += 1
        source.set_loop(source.loops_remaining + 1)
      else:
        source.paused = not source.paused

  if repl == False:
    ps(library["library"][id][0]["file"])
