from pathlib import Path
import shutil
root=Path(__file__).resolve().parent
site=Path.cwd()
index=site/'index.html'
css=site/'styles.css'
if not index.exists() or not css.exists():
    raise SystemExit('Run this script from the website repository root (where index.html and styles.css live).')
for p in (index,css):
    shutil.copy2(p,p.with_suffix(p.suffix+'.before-brand-repair'))
for p in (root/'assets').rglob('*'):
    if p.is_file():
        dest=site/'assets'/p.relative_to(root/'assets');dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dest)
s=index.read_text()
s=s.replace('assets/brand/lee-logo-horizontal.svg','assets/brand/lee-logo-dark.jpg')
s=s.replace('assets/brand/lee-logo-symbol.svg','assets/brand/lee-logo-symbol.png')
index.write_text(s)
with css.open('a') as f:
    f.write('''\n/* Brand asset restoration – preserve original layout */\n.brand-master{object-fit:contain;max-width:100%;height:auto}\n.hero-photo{background-image:linear-gradient(90deg,rgba(0,0,0,.78),rgba(0,0,0,.28)),url("assets/hero-brand.jpg")!important;background-position:center;background-size:cover}\n''')
print('Logo and hero restored. Other missing service and comparison photographs still need original assets. No production deployment performed.')
