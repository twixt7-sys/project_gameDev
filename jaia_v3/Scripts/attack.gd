extends Node2D

class_name Attack

@onready var timer: Timer = $Timer

@export var atk_dmg: float
@export var atk_spd: float
var can_attack := true

func _ready() -> void:
	timer.wait_time = 1.0 / atk_spd
	timer.timeout.connect(_on_timer_timeout)

func _on_timer_timeout() -> void:
	can_attack = true

func attack(sprite: AnimatedSprite2D, cond : bool, callable: Callable):
	if can_attack and cond:
		can_attack = false
		sprite.speed_scale = atk_spd
		callable.call()
		timer.start()
