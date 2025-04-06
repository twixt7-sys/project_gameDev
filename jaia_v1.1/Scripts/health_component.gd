class_name HealthComponent

extends Node2D

@export var MAX_HEALTH := 100

var health: float

func _ready() -> void:
	health = MAX_HEALTH

func damage(attack: AttackComponent):
	health -= attack.attack_damage
	attack.attack_triggered()
	if health <= 0:
		get_parent().queue_free()
