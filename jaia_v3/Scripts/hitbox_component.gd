class_name HitboxComponent

extends Area2D

@export var health_comp: HealthComponent
@export var hit_interval: float

var flag = true

func _ready() -> void:
	$Timer.wait_time = hit_interval
	$Timer.start()

# slime's own damage function that calls the health component's damage function
func take_damage(atk: Attack):
	if flag:
		flag = false
		if health_comp:
			health_comp.damage(atk)
			print("[hitbox]This entity is taking", atk.damage, " damage.")

func _on_timer_timeout() -> void:
	flag = true
