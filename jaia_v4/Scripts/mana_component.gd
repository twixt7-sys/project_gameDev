class_name ManaComponent

extends Node2D

@export var MAX_MANA := 100

var mana: int

func _ready() -> void:
	mana = MAX_MANA

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass
