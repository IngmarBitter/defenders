# Prints verbatim NKJV text from Blue Letter Bible, e.g.: python tools/blb.py gen:1:1 exo:20:8-11
import re,sys,html,urllib.request
def chapter(book,ch):
    u=f'https://www.blueletterbible.org/nkjv/{book}/{ch}/1/'
    s=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=60).read().decode('utf8')
    out={}
    for m in re.finditer(r'<div class="EngBibleText scriptureText"[^>]*data-print-verse-prefix="(\d+)">(.*?)</div>',s,re.S):
        t=m.group(2)
        t=re.sub(r'<a[^>]*class="hide-for-tablet">.*?</a>','',t,flags=re.S)
        t=re.sub(r'<span class="hide-for-tablet"> - </span>','',t)
        t=re.sub(r'<sup.*?</sup>','',t,flags=re.S)
        t=re.sub(r'<[^>]+>','',t); t=html.unescape(re.sub(r'\s+',' ',t)).strip()
        out[int(m.group(1))]=t
    return out
for ref in sys.argv[1:]:
    b,c,v=ref.split(':'); a,z=(v.split('-')+[v])[:2]
    d=chapter(b,c); print(ref,'|',' '.join(d[i] for i in range(int(a),int(z)+1)))
