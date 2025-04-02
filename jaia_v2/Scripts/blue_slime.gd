class_name BlueSlime

extends CharacterBody2D

@export var health: HealthComponent

func _on_hitbox_component_body_entered(area) -> void:
	health.damage(AttackComponent.new())
