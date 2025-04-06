extends Node

@onready var player: Player = $Entities/Player
@onready var blue_slime: BlueSlime = $"Blue Slime"
@onready var blue_slime_2: BlueSlime = $"Blue Slime2"
@onready var blue_slime_3: BlueSlime = $"Blue Slime3"

func _on_player_damage_dealt(target: BlueSlime, atk: Attack) -> void:
	print("player dealt damage!")
	target.take_damage(atk)
	target.take_knockback(atk)
