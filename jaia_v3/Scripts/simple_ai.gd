extends Node2D

#@export var entity: Entity
@export var DETECTION_RANGE: int

var patrol_area: Area2D 

func wander(area):
	# makes the sprite wander at certain points around an area
	pass

func chase():
	#chase the player when it reaches a certain range
	pass
