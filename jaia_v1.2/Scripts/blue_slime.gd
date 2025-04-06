class_name BlueSlime

extends CharacterBody2D

@onready var health_component: HealthComponent = $HealthComponent
@onready var hitbox_component: HitboxComponent = $HitboxComponent

func take_damage(atk: Attack):
	print("[slime] received damage.")
	hitbox_component.take_damage(atk)

func take_knockback(atk: Attack):
	var direction = (global_position - atk.origin).normalized()
	velocity += direction * atk.knockback
	print("Knockback recieved: ", atk.knockback)
