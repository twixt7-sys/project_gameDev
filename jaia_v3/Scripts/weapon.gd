extends Node2D

var attack_damage := 10

func _on_hitbox_component_area_entered(area) -> void:
	if area is HitboxComponent:
		var hitbox: HitboxComponent = area
		var atk = Attack.new
		atk.atk_dmg = attack_damage
		
		hitbox.damage(atk)
