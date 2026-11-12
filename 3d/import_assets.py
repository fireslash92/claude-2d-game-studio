"""Run in Claude Code cloud: import selected free KayKit repositories."""
import argparse, json, pathlib, subprocess, tempfile, shutil
ROOT = pathlib.Path(__file__).resolve().parent
PACKS = {'adventurers':'KayKit-Character-Pack-Adventures-1.0','dungeon':'KayKit-Dungeon-Remastered-1.0','medieval':'KayKit-Medieval-Hexagon-Pack-1.0','skeletons':'KayKit-Character-Pack-Skeletons-1.0'}
def main():
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('packs',nargs='*',help='Choose '+', '.join(PACKS)+'; default all'); args=p.parse_args()
    selected=args.packs or list(PACKS)
    if any(n not in PACKS for n in selected): p.error('Unknown pack')
    assets=ROOT/'assets'; assets.mkdir(exist_ok=True)
    for name in selected:
        dest=assets/name
        if dest.exists(): print('Preserving existing',dest); continue
        url='https://github.com/KayKit-Game-Assets/'+PACKS[name]+'.git'
        with tempfile.TemporaryDirectory() as tmp:
            clone=pathlib.Path(tmp)/'pack'
            subprocess.run(['git','clone','--depth','1',url,str(clone)],check=True)
            revision=subprocess.check_output(['git','-C',str(clone),'rev-parse','HEAD'],text=True).strip()
            licenses=[x for x in clone.iterdir() if x.is_file() and x.name.lower().startswith(('license','licence','copying'))]
            if not licenses: raise RuntimeError('Review missing license for '+name)
            models=[f for f in clone.rglob('*') if f.is_file() and f.suffix.lower() in ('.glb','.gltf')]
            if not models: raise RuntimeError('No GLB/glTF models in '+name)
            for f in models:
                with f.open('rb') as h:
                    if h.read(80).startswith(b'version https://git-lfs.github.com/spec/v1'): raise RuntimeError('Unresolved Git LFS pointer: '+str(f))
            shutil.copytree(clone,dest,ignore=shutil.ignore_patterns('.git'))
            (dest/'SOURCE.json').write_text(json.dumps({'url':url,'revision':revision,'license_files':[f.name for f in licenses]},indent=2)+'\n')
            print('Imported',name,len(models),'models')
    items=[{'path':f.relative_to(ROOT).as_posix(),'pack':f.relative_to(assets).parts[0],'name':f.stem} for f in sorted(assets.rglob('*')) if f.is_file() and f.suffix.lower() in ('.glb','.gltf')]
    (ROOT/'models.json').write_text(json.dumps(items,indent=2)+'\n'); print('Indexed',len(items),'models. Review licenses before committing.')
if __name__=='__main__': main()
