class_name Player

extends CharacterBody2D

@onready var sprite := $AnimatedSprite2D
@onready var weapon := $Weapon
@onready var atk := $Attack
@onready var timer := $Timer

@export var ACCELERATION:= 25
@export var RESISTANCE := 0.9
@export var SPRINT_POWER := 2
@export var ATTACK_SPEED := 1

var direction

func _physics_process(delta: float) -> void:
	move(delta)
	flip_h()
	atk.attack(sprite, Input.is_action_just_pressed("attack"), func(): sprite.play("attack"))
	animate_movement()

func move(delta):
	direction = Vector2(Input.get_axis("move_left", "move_right"), Input.get_axis("move_up","move_down"))
	direction = direction.normalized() if direction.length() > 1 else direction
	var sprint = SPRINT_POWER if Input.is_action_pressed("sprint") else 1
	velocity += direction * ACCELERATION * sprint
	velocity *= RESISTANCE
	position += velocity * delta

func flip_h():
	if velocity.x < 0:
		sprite.flip_h = true
	elif velocity.x > 0:
		sprite.flip_h = false

func animate_movement():
	if sprite.is_playing() and sprite.animation == "attack":
		return
	elif Input.is_action_pressed("sprint") and direction:
		sprite.play("sprint")
	elif direction:
		sprite.play("walk")
	else:
		sprite.play("idle")
