extends Node2D

var attack_damage := 10.0
var knockback_force := 100.0
var stun_time := 1.5

func _on_hitbox_area_entered(area):
	if area is HitboxComponent:
		var hitbox: HitboxComponent = area
		var attack = AttackComponent.new()
		attack.attack_damage = attack_damage
		attack.knockback_force = knockback_force
		attack.attack_position = global_position
		attack.stun_time = stun_time
		
		hitbox.damage(attack)
