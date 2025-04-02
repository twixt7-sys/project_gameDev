class_name HitboxComponent

extends Area2D

@export var health_comp: HealthComponent

# slime's own damage function that calls the health component's damage function
func damage(atk: Attack):
	if health_comp:
		health_comp.damage(atk)
