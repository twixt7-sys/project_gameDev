class_name Attack

extends Node2D

@onready var timer: Timer = $Timer

@export var damage: float
@export var speed: float
@export var knockback: float

var can_attack = true
var origin: Vector2

static func create(atk_origin: Vector2) -> Attack:
	var atk: Attack = preload("res://Scenes/attack.tscn").instantiate()
	atk.origin = atk_origin
	return atk

func attack(callable: Callable):
	if can_attack:
		can_attack = false
		callable.call()
		print("Entity attacked.")
		timer.start()

func _on_timer_timeout() -> void:
	can_attack = true
