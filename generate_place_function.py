blocks = []
id_map = {}
offset_x = 1
offset_y = 1

# build id map 
with open('blocks.map', 'r') as f:
  with open('blocks.map2', 'r') as f2:
    line = f.readline()
    line2 = f2.readline()
    while line != '' and line2 != '':
      line = line.replace("\n", '')
      line2 = line2.replace("\n", '')
      id_map[line] = f'minecraft:{line2}'
      line = f.readline()
      line2 = f2.readline()

with open('blocks.data', 'r') as f:
  line = f.readline()
  while line != '':
    blocks.append(line.replace("\n", ""))
    line = f.readline()

blocks = [id_map[x] for x in blocks]

i = 0
for x in range(0, 36*2, 2 * offset_x):
  for y in range(0, 20*2, 2 * offset_y):
    coords = f"setblock ~{x} ~ ~{y} "
    if (i < len(blocks)):
        blocks[i] = coords + blocks[i]
    i += 1

with open('./data/all_blocks/function/place.mcfunction', 'w') as f:
  first = True
  for line in blocks:
    if not first: f.write("\n")
    f.write(line)
    first = False


