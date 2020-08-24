# -*- coding: utf-8 -*-
import re
import json

films = {}
with open('newdata.txt') as filmdata:
    newdata = filmdata.read()
    films = json.loads(newdata)

def esc(x):
    if x:
        return "'" + x.replace("'", "''") + "'"
    else:
        return 'NULL'

def cls(f, x):
    if x in f: return f[x]
    else: return None


for filmName in films:
    INSERT_FILM = "INSERT INTO film (director, rdate, runtime, country, mid) VALUES (%s, %s, %s, %s, %s);"
    
    film = films[filmName]

    print(
        INSERT_FILM % (
            esc(cls(film, 'director')),
            esc(cls(film, 'releaseDate')),
            esc(cls(film, 'Work/runtime')),
            esc(cls(film, 'country')),
            esc(filmName)
        )
    )

    if 'subject' not in film: continue

    INSERT_SUBJECT = "INSERT INTO filmsubject (mid, subject) VALUES (%s, %s);"
    for subject in film['subject']:
        print(
            INSERT_SUBJECT % (
                esc(filmName.encode('utf-8', 'ignore')),
                esc(subject.encode('utf-8', 'ignore'))
            )
        )

