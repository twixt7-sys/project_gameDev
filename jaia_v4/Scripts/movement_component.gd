class_name MovementComponent

extends Node2D

@export var STAMINA: StaminaComponent

@export var BODY : CharacterBody2D
@export var MOVEMENT_SPEED := 10.0
@export var SPRINT_POWER := 1.8
@export var BACKSTEP_POWER := 2
@export var FRICTION := 0.9

var can_flip = true
var can_roll = true
var is_dashing = false
var run_on_cooldown = false

const V_zero = Vector2.ZERO

func move(delta: float, direction: Vector2, run: bool) -> void:
	direction = direction.normalized() if direction.length() > 1 else direction
	var sprint = SPRINT_POWER if run and STAMINA.stamina >= 5 and not run_on_cooldown else 1
	BODY.velocity += direction * MOVEMENT_SPEED * sprint
	BODY.velocity *= FRICTION
	BODY.position += BODY.velocity * delta
	BODY.move_and_slide()
	
	if STAMINA and run and direction != V_zero:
		if not run_on_cooldown:
			STAMINA.consume(0.35)

func dash():
	if STAMINA.stamina > 4:
		STAMINA.stamina -= 4
		BODY.velocity *= (Vector2(1, 1) * BACKSTEP_POWER)
	
func backstep():
	if STAMINA.stamina > 4:
		STAMINA.stamina -= 4
		BODY.velocity *= -(Vector2(1, 1) * BACKSTEP_POWER)
