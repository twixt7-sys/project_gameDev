class_name HitboxComponent

extends Area2D

@export var healthComponent: HealthComponent
@export var collisionObject: CollisionObject2D

var can_take_damage: bool = true

func _process(delta: float) -> void:
	if collisionObject.modulate.r > 0: collisionObject.modulate.r -= 0.1
	print(collisionObject.modulate.r)

func take_damage(atk: Attack) -> void:
	healthComponent.take_damage(atk.damage)
	collisionObject.modulate.r = 3
	
