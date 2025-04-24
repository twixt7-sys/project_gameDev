class_name HealthComponent

extends Node2D

@export var MAX_HEALTH := 100

var health: int

func _ready() -> void:
	health = MAX_HEALTH

func _process(delta: float) -> void:
	pass

func take_damage(dmg: int) -> void:
	if health - dmg >= 0:
		health -= dmg
	else:
		health = 0
