extends Node

@onready var player: Player = $Entities/Player
@onready var slimes: Array = []
@onready var gui: Control = $ControlParent/GUI
@onready var camera: Camera2D = $Entities/Player/Camera2D

@onready var blueslime: BlueSlime = $"Entities/Blue Slime"

func _ready() -> void:
	for entity in $Entities.get_children():
		if entity is BlueSlime:
			slimes.append(entity)
			entity.connect("patrol_area_exited", _on_patrol_area_exited)

func _process(delta: float) -> void:
	pass
		
func _physics_process(delta: float) -> void:
	for slime in slimes:
		slime = slime as BlueSlime
		slime.chase(delta, player)

func _on_blue_slime_patrol_area_entered(player: Player, slime: BlueSlime) -> void:
	player = player
	slime = slime

func _on_patrol_area_exited(player: Player, slime: BlueSlime):
	slime.patrol()


func _on_blue_slime_body_attacked(attacker: Variant, entity: Variant) -> void:
	blueslime.take_damage(player.attack_component)


func _on_player_attack_area_entered(enemy: BlueSlime, attacker: Player) -> void:
	enemy.take_damage(attacker.attack_component)
