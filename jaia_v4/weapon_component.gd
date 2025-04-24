class_name WeaponComponent

extends Node2D

@export var attack_area: Area2D
@export var interval: float

var can_attack: bool = true

func attack(atk: Attack) -> void:
	if can_attack: pass
		
	
	await Util.wait(interval)
	
