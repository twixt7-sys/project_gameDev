class_name Attack

extends Node2D

@onready var timer: Timer = $Timer

@export var damage: float
@export var speed: float
@export var knockback: float

var can_attack := true
var origin: Vector2

func _init(_origin: Vector2):
	origin = _origin

func _ready() -> void:
	timer.wait_time = 1.0 / speed

func _on_timer_timeout() -> void:
	can_attack = true

func attack(sprite: AnimatedSprite2D, cond : bool, callable: Callable):
	if can_attack and cond:
		can_attack = false
		var original_speed = sprite.speed_scale  # Store original speed
		sprite.speed_scale = speed  # Modify speed for attack animation
		callable.call()
		sprite.animation_finished.connect(func():
			sprite.speed_scale = original_speed  # Reset speed after animation ends
		, CONNECT_ONE_SHOT)  # Auto disconnect after execution
		timer.start()
