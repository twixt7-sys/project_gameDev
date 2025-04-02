extends Node2D

@export var MOVEMENT_SPEED := 10 #acceleration
@export var RESISTANCE := 1 #deceleration

var accel: Array = [0.0, 0.0]
var vel: Array = [0.0, 0.0]

func _ready() -> void:
	pass

func _process(delta: float) -> void:
	pass
