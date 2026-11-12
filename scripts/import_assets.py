#!/usr/bin/env python3
"""Explicit opt-in imports. Never install or execute third-party code automatically."""
import argparse, json, pathlib, subprocess, shutil, os
ROOT=pathlib.Path(__file__).resolve().parents[1]
SOURCES={x['id']:x for x in json.loads((ROOT/'catalog/sources.json').read_text())}
def run(*args):
    print('+', ' '.join(map(str,args)), flush=True)
    subprocess.run(args, check=True)
def clone(s, dest):
    if dest.exists():
        print(f'Skipping existing {dest}; remove it manually to reimport.'); return
    dest.parent.mkdir(parents=True, exist_ok=True)
    temp=dest.with_name(dest.name+'.partial')
    if temp.exists(): raise SystemExit(f'Remove incomplete import {temp} before retrying')
    try:
        if s['mode']=='sparse':
            run('git','clone','--depth','1','--filter=blob:none','--sparse',s['url'],str(temp))
            run('git','-C',str(temp),'sparse-checkout','set',*s['folders'])
        else: run('git','clone','--depth','1',s['url'],str(temp))
        revision=subprocess.check_output(['git','-C',str(temp),'rev-parse','HEAD'],text=True).strip()
        shutil.rmtree(temp/'.git')
        (temp/'IMPORT-PROVENANCE.json').write_text(json.dumps({'source':s['url'],'revision':revision,'license':s['license']},indent=2)+'\n')
        temp.rename(dest)
    except BaseException:
        print(f'Import failed; partial files may remain at {temp}.'); raise
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('ids', nargs='*', choices=None, help='Source IDs (use --list)')
p.add_argument('--list', action='store_true'); p.add_argument('--starter',action='store_true',help='Import Ninja Adventure only')
p.add_argument('--all-free',action='store_true',help='Import three verified-catalog CC0 sources (potentially large)')
p.add_argument('--install-skill',action='store_true',help='Install Pixel Art Studio skill source for review; requires Python/Pillow separately')
a=p.parse_args()
if a.list or not (a.ids or a.starter or a.all_free or a.install_skill):
    for s in SOURCES.values(): print(f"{s['id']:17} {s['mode']:8} {s['name']} | {s['license']}")
    raise SystemExit(0)
ids=list(dict.fromkeys(a.ids+(['ninja-adventure'] if a.starter else [])+(['ninja-adventure','superpowers','tiddybub'] if a.all_free else [])+(['pixel-studio'] if a.install_skill else [])))
for id in ids:
    if id not in SOURCES: raise SystemExit(f'Unknown source: {id}')
    s=SOURCES[id]
    if s['mode']=='manual': print(f'Manual setup: {s["url"]}\n{s["note"]}'); continue
    dest=ROOT/('.claude/skills/pixel-art-studio' if s['mode']=='skill' else 'assets/vendor/'+id)
    clone(s,dest)
print('Done. Review upstream license files and provenance before using assets in a published game.')
