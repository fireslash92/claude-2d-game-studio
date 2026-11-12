from PIL import Image, ImageDraw
from pathlib import Path
import random, json
out=Path(__file__).resolve().parents[1]/'assets/starter';out.mkdir(exist_ok=True)
r=random.Random(42)
def tile(base,marks):
 im=Image.new('RGBA',(16,16),base);d=ImageDraw.Draw(im)
 for _ in range(14):
  x,y=r.randrange(16),r.randrange(16);d.point((x,y),fill=r.choice(marks))
 return im
atlas=Image.new('RGBA',(96,16));
for i,(base,marks) in enumerate([('#52784f',['#648b58','#426b47','#70965d']),('#b59a70',['#c9b58c','#a98b60']),('#366a7b',['#448a99','#599ca7']),('#40594a',['#526a50','#2c493e']),('#c6ae87',['#a88b66','#d8c6a5']),('#786c64',['#95867a','#504f4d'])]):
 im=tile(base,marks);d=ImageDraw.Draw(im)
 if i==2:
  for y in [3,9,14]: d.line((2,y,9,y),fill='#5394a3')
 if i==4:
  d.line((0,0,15,0),fill='#8c7459');d.line((0,8,15,8),fill='#9b8262');d.line((7,0,7,8),fill='#a88b66')
 if i==5:
  d.line((0,7,15,7),fill='#514c47');d.line((6,0,6,7),fill='#514c47');d.line((11,8,11,15),fill='#514c47')
 atlas.paste(im,(i*16,0))
atlas.save(out/'tiles.png')
# Four 16x24 directional character rows, four steps each.
sheet=Image.new('RGBA',(64,96));
for row in range(4):
 for f in range(4):
  im=Image.new('RGBA',(16,24));d=ImageDraw.Draw(im);dy=[0,0,-1,0][f];a=[0,1,0,-1][f]
  def rect(b,c): d.rectangle((b[0],b[1]+dy,b[2],b[3]+dy),fill=c)
  rect((4,3,11,10),'#39313b');rect((5,4,10,10),'#b87950');rect((4,2,11,5),'#694c39');rect((5,2,9,3),'#a8794c')
  rect((3,11,12,18),'#263c49');rect((4,11,11,17),'#418d86');rect((5,12,8,15),'#70b8a0');rect((4,17,11,18),'#b99a56');rect((5,19,7,22+a),'#3d3945');rect((9,19,11,22-a),'#3d3945')
  if row==0: rect((6,7,6,7),'#302e35');rect((9,7,9,7),'#302e35')
  elif row==1: rect((5,4,10,9),'#694c39');rect((5,11,10,15),'#326c72')
  elif row==2: rect((4,6,4,7),'#332d35');rect((10,5,12,9),'#694c39')
  else: rect((11,6,11,7),'#332d35');rect((3,5,5,9),'#694c39')
  sheet.paste(im,(f*16,row*24))
sheet.save(out/'hero.png')
# Props atlas 4x32 square.
props=Image.new('RGBA',(128,32));
for i in range(4):
 im=Image.new('RGBA',(32,32));d=ImageDraw.Draw(im)
 if i==0:
  d.rectangle((14,19,18,30),fill='#76563d');d.rectangle((15,21,16,29),fill='#ac8052')
  for b,c in [((2,5,29,25),'#284c40'),((4,3,27,21),'#396a48'),((8,1,23,16),'#52845a'),((10,3,18,10),'#79a36a')]:d.ellipse(b,fill=c)
 elif i==1:
  d.rectangle((4,14,27,30),fill='#c8ad80');d.rectangle((6,17,25,29),fill='#ddc39a');d.polygon([(1,15),(16,2),(30,15)],fill='#704c45');d.polygon([(4,14),(16,5),(27,14)],fill='#a66751');d.rectangle((13,21,19,30),fill='#765b48');d.rectangle((7,20,10,23),fill='#4d7482');d.rectangle((22,20,25,23),fill='#4d7482')
 elif i==2:
  d.ellipse((3,17,27,28),fill='#435748');d.ellipse((5,9,25,25),fill='#68826f');d.ellipse((9,11,20,17),fill='#8eaa8a')
 else:
  d.rectangle((6,17,25,27),fill='#45372e');d.rectangle((7,15,24,25),fill='#a6753d');d.rectangle((7,19,24,21),fill='#e0b95f');d.rectangle((14,19,17,24),fill='#e8cd81')
 props.paste(im,(i*32,0))
props.save(out/'props.png')
(out/'manifest.json').write_text(json.dumps({'license':'MIT','tiles':{'file':'tiles.png','frame':[16,16],'names':['grass','path','water','forest','floor','stone']},'hero':{'file':'hero.png','frame':[16,24],'columns':4,'rows':['down','up','left','right'],'fps':8,'anchor':'bottom-center'},'props':{'file':'props.png','frame':[32,32],'names':['tree','house','rock','chest']}},indent=2)+'\n')
