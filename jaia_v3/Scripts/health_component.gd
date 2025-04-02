class_name HealthComponent

extends Node2D

@export var MAX_HEALTH: float

var health: float

func ready():
	health = MAX_HEALTH
	
func damage(atk: Attack):
	health -= atk.atk_dmg
	
	if health <= 0:
		get_parent().queue_free()
