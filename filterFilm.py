import re
import json

films = {}
with open('film.dbpedia.graph') as dbpedia:
  for linha in dbpedia:
    tokens = linha.split()
    tokens[0]= tokens[0].replace('<','').replace('>','')
    tokens[1]= tokens[1].replace('<','').replace('>','')
    values = ' '.join(tokens[2:])
    if tokens[1] == 'director' or tokens[1] == 'country':
      values = values.replace('<','').replace('>','')
    elif tokens[1] == 'releaseDate':
      regexresult = re.search(r'"([^"]+)"', values).groups(1)[0]
      values = regexresult
    elif tokens[1] == 'subject':
      values = values.replace('<','').replace('>','').replace('Category:','')
    elif tokens[1] =='Work/runtime':
      regexresult = re.search(r'"([^"]+)"', values).groups(1)[0]
      values = regexresult

    if tokens[1] in ['director','releaseDate','subject','Work/runtime','country',]:
      if tokens[0] not in films:
        films[tokens[0]] = {}

      if tokens[1] == 'subject':
        if 'subject' not in films[tokens[0]]:
            films[tokens[0]]['subject'] = []
        films[tokens[0]]['subject'].append(values)
      else:
        films[tokens[0]][tokens[1]] = values

print(json.dumps(films))
