class_name HealthComponent

extends Node2D

@export var MAX_HEALTH: float

var health: float

func _ready():
	health = MAX_HEALTH

func damage(atk: Attack):
	print("initial health: ", health)
	health -= atk.damage
	print("remaining health: ", health)
	if health <= 0:
		get_parent().queue_free()
