class_name GameInterface

extends Control

@onready var player: Player = $Node2D/Player

@onready var health_bar: ColorRect = $HealthBar
@onready var mana_bar: ColorRect = $ManaBar
@onready var stamina_bar: ColorRect = $StaminaBar

const BAR_HEIGHT = 2.0

var mana_width := 402.0
var health_width := 400.0
var stamina_width := 408.0

func _ready() -> void:
	visible = true


func _process(delta: float) -> void:
	health_bar.size = Vector2((player.health_component.health / player.health_component.MAX_HEALTH) * mana_width, mana_bar.size.y)
	mana_bar.size = Vector2((player.mana_component.mana / player.mana_component.MAX_MANA) * health_width, health_bar.size.y)
	stamina_bar.size = Vector2((player.stamina_component.stamina / player.stamina_component.MAX_STAMINA) * stamina_width, stamina_bar.size.y)
