class_name Player

extends CharacterBody2D
@onready var sprite: AnimatedSprite2D = $AnimatedSprite2D
@onready var weapon: Area2D = $Weapon

@export var entity: Entity
@export var movement_speed := 0.5
@export var sprint_power := 2

const RESISTANCE := 0.80
const slash_cooldown = 0.5
const slash_thrust = 2
var can_slash = true

func _physics_process(delta: float) -> void:
	
	var sprint = sprint_power if Input.is_action_pressed("run") else 1
	if Input.is_action_just_pressed("attack") and can_slash:
		can_slash = false
		weapon.get_node("AnimatedSprite2D").play("slash", true)
		sprite.play("action1")
		velocity.x += velocity.x * slash_thrust
		velocity.y += velocity.y * slash_thrust
		await get_tree().create_timer(slash_cooldown).timeout
		can_slash = true
	
	var direction := Vector2(Input.get_axis("move_left","move_right"), Input.get_axis("move_up", "move_down"))
	if direction.length() > 1:
		direction = direction.normalized()  # Apply Pythagorean theorem (normalize diagonal movement)
	velocity.x += direction.x * movement_speed * sprint
	velocity.y += direction.y * movement_speed * sprint
	velocity.x = move_toward(velocity.x, 0, delta) * RESISTANCE
	velocity.y = move_toward(velocity.y, 0, delta) * RESISTANCE
	position += velocity
	
	if velocity.x < 0 and sprite.is_playing() and sprite.animation != "slash":
		sprite.flip_h = true
		weapon.get_node("AnimatedSprite2D").flip_h = false
		weapon.position.x = -10
	elif velocity.x > 0 and sprite.is_playing() and sprite.animation != "slash":
		sprite.flip_h = false
		weapon.get_node("AnimatedSprite2D").flip_h = true
		weapon.position.x = 10
	if sprite.is_playing() and sprite.animation == "action1":
		return 
	
	if Input.is_action_pressed("run") and velocity.x + velocity.y != 0:
		sprite.play("run")
	elif velocity.x + velocity.y != 0:
		sprite.play("walk")
	else:
		sprite.play("idle")
