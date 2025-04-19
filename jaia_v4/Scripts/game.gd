extends Node

@onready var player: Player = $Entities/Player
@onready var slimes: Array = []
@onready var camera: Camera2D = $Entities/Camera2D2
@onready var gui: Control = $ControlParent/GUI

func _ready() -> void:
	for entity in $Entities.get_children():
		if entity is BlueSlime:
			slimes.append(entity)
			entity.connect("patrol_area_exited", _on_patrol_area_exited)

func _process(delta: float) -> void:
	camera.position = player.position

func _physics_process(delta: float) -> void:
	for slime in slimes:
		slime = slime as BlueSlime
		slime.chase(delta, player)

func _on_blue_slime_patrol_area_entered(player: Player, slime: BlueSlime) -> void:
	player = player
	slime = slime

func _on_patrol_area_exited(player: Player, slime: BlueSlime):
	slime.patrol()
