### Moving discs fromTower toTower withTower
### withTower moves left along with height -1

def move_tower(height, from_tower, to_tower, with_tower):
	if height >= 1:
		move_tower(height -1, from_tower, with_tower, to_tower)
		move_disc(from_tower, to_tower)
		move_tower(height -1, with_tower, from_tower, to_tower)

def move_disc(from_tower, to_tower):
	print("Move disc from", from_tower, "to", to_tower)

move_tower(3, "A", "B", "C") 