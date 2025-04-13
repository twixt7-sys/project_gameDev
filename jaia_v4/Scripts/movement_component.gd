class_name MovementComponent

extends Node2D

@export var STAMINA: StaminaComponent

@export var BODY : CharacterBody2D
@export var SPRITE : AnimatedSprite2D
@export var MOVEMENT_SPEED := 10.0
@export var SPRINT_POWER := 1.8
@export var BACKSTEP_POWER := 2
@export var FRICTION := 0.9

@onready var timer: Timer = $DashCD
@onready var stamina_cd: Timer = $StaminaCD

var can_dash: bool = true
var flip_active = true
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

	if STAMINA and STAMINA.stamina < 5:
		run_on_cooldown = true
		stamina_cd.start()
	
	if STAMINA and run and direction != V_zero:
		if not run_on_cooldown:
			STAMINA.consume(1.2)

	flip_h()
	animate(run, direction)

func flip_h():
	if flip_active:
		if BODY.velocity.x < 0:
			SPRITE.flip_h = true
		elif BODY.velocity.x > 0:
			SPRITE.flip_h = false

func animate(run_animation: bool, direction: Vector2):
	if is_dashing:
		SPRITE.play("roll")
	elif run_animation and direction and not run_on_cooldown:
		SPRITE.play("run")
	elif direction:
		SPRITE.play("walk")
	else:
		SPRITE.play("idle")

func dash(callable: Callable):
	if STAMINA.stamina > 15 and can_dash:
		is_dashing = true
		STAMINA.stamina -= 15
		can_dash = false
		flip_active = false
		BODY.velocity *= (Vector2(1, 1) * BACKSTEP_POWER)
		callable.call()
		timer.start()
	
func backstep(callable: Callable):
	if STAMINA.stamina > 15 and can_dash:
		STAMINA.stamina -= 15
		can_dash = false
		flip_active = false
		BODY.velocity *= -(Vector2(1, 1) * BACKSTEP_POWER)
		callable.call()
		timer.start()

func _on_timer_timeout() -> void:
	can_dash = true
	flip_active = true
	is_dashing = false


func _on_stamina_cd_timeout() -> void:
	run_on_cooldown = false
