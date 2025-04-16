class_name StaminaComponent

extends Node2D

@export var MAX_STAMINA := 100.0
@export var REGEN := 0.25

var stamina: float


func _ready() -> void:
	stamina = MAX_STAMINA

func _physics_process(delta: float) -> void:
	if stamina < MAX_STAMINA:
		stamina += REGEN

func consume(amount: float):
	if stamina > 0:
		stamina -= amount
