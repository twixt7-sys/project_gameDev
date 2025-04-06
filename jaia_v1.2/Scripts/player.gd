class_name Player

extends CharacterBody2D

signal damage_dealt(target, atk)

@onready var sprite := $AnimatedSprite2D
@onready var atk:= Attack.new(global_position)
@onready var weapon: Weapon = $Weapon

@export var ACCELERATION: float = 15.0
@export var RESISTANCE: float = 0.9
@export var SPRINT_POWER: float = 1.5
@export var ATTACK_SPEED: float = 1.0
@export var ATTACK_THRUST: float = 2

var direction

func _physics_process(delta: float) -> void:
	move(delta)
	flip_h()
	atk.attack(sprite, Input.is_action_just_pressed("attack"), attack)
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
		weapon.flip_n_offset(false, -12)
	elif velocity.x > 0:
		sprite.flip_h = false
		weapon.flip_n_offset(true, 12)

func animate_movement():
	if sprite.is_playing() and sprite.animation == "attack":
		return
	elif Input.is_action_pressed("sprint") and direction:
		sprite.play("sprint")
	elif direction:
		sprite.play("walk")
	else:
		sprite.play("idle")

func attack():
	sprite.play("attack")
	velocity *= ATTACK_THRUST
	atk.origin = global_position
	weapon.attack()

func _on_weapon_damage_dealt(hitbox: HitboxComponent) -> void:
	print("[weapon to player]: damage dealt!")
	print("value: ", atk.damage)
	var target = hitbox.get_parent()
	print("target: ", target)
	emit_signal("damage_dealt", target, atk)
