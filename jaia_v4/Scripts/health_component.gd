class_name HealthComponent

extends Node2D

@export var MAX_HEALTH := 100

var health: int

func _ready() -> void:
	health = MAX_HEALTH

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass
