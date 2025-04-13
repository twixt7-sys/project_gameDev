class_name MovementComponent

extends Node2D

@export var STAMINA: StaminaComponent

@export var BODY : CharacterBody2D
@export var SPRITE : AnimatedSprite2D
@export var MOVEMENT_SPEED := 10.0
@export var SPRINT_POWER := 1.8
@export var FRICTION := 0.9

func move(delta: float, direction: Vector2, run: bool) -> void:
	direction = direction.normalized() if direction.length() > 1 else direction
	var sprint = SPRINT_POWER if run and STAMINA.stamina >= 1 else 1
	BODY.velocity += direction * MOVEMENT_SPEED * sprint
	BODY.velocity *= FRICTION
	BODY.position += BODY.velocity * delta
	BODY.move_and_slide()

	if STAMINA and run and direction != Vector2.ZERO:
		STAMINA.consume(2)

	flip_h()
	animate(run, direction)

func flip_h():
	if BODY.velocity.x < 0:
		SPRITE.flip_h = true
	elif BODY.velocity.x > 0:
		SPRITE.flip_h = false
		
func animate(run_animation: bool, direction: Vector2):
	if run_animation and direction:
		SPRITE.play("run")
	elif direction:
		SPRITE.play("walk")
	else:
		SPRITE.play("idle")

func dash(dash_power):
	pass
	
