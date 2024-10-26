import json, re
import requests
from urlextract import URLExtract
import sys


utid = 'audris'
base= { 'model':'https://huggingface.co/', 'data': 'https://huggingface.co/datasets/' }
post = '/raw/main/README.md'

extU = URLExtract()
DOIpattern = r'\b(10[.][0-9]{4,}(?:[.][0-9]+)*/(?:(?!["&\'<>])[[:graph:]])+)\b';

def extractURLs (c):
 res = extU.find_urls (c)
 return res

def extractDOIs (c):
 res = re.findall (DOIpattern, c)
 return res

def run (tp):
 with open(f"input/{utid}_{tp}", 'r') as f:
  for line in f:
   line = line.strip ()
   print(line)
   url = base[tp] + f"{line}{post}"
   r = requests.get (url)
   content = r.text;
   urls = extractURLs(content)
   dois = extractDOIs(content)
   res = { 'ID': line, 'type': tp, 'url': url, 'content': content, 'links': urls, 'dois': dois }
   out = json.dumps(res, ensure_ascii=False)
   print (out)

run('model')