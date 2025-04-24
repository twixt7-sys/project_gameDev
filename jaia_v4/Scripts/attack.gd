class_name Attack

extends Node2D

@onready var timer: Timer = $AttackTimer
@onready var animation_timer: Timer = $AnimationTimer

@export var damage: float
@export var speed: float
@export var knockback: float

var can_attack = true
var animation_flag = true
var origin: Vector2

static func create(atk_origin: Vector2) -> Attack:
	var atk: Attack = preload("res://Scenes/Components/attack.tscn").instantiate()
	atk.origin = atk_origin
	return atk

func attack(callable: Callable):
	if can_attack:
		can_attack = false
		callable.call()
		timer.start()

func _on_timer_timeout() -> void:
	can_attack = true

func play_animation(sprite: AnimatedSprite2D, action: String):
	if animation_flag:
		animation_flag = false
		sprite.play(action)
		animation_timer.start()

func _on_animation_timer_timeout() -> void:
	animation_flag = true
