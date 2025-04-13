class_name StatusBar
extends Node

@export var player: Player
@export var sprite: AnimatedSprite2D

@export var healthComponent: HealthComponent
@export var manaComponent: ManaComponent
@export var staminaComponent: StaminaComponent

@onready var health_bar: ColorRect = $HealthBar
@onready var mana_bar: ColorRect = $ManaBar
@onready var stamina_bar: ColorRect = $StaminaBar

const MAX_VALUE = 30.0
const BAR_HEIGHT = 2.0



func _process(delta: float) -> void:
	var BAR_WIDTH = sprite.sprite_frames.get_frame_texture("idle", 0).get_size().x * sprite.scale.x / 3.5
	if healthComponent and manaComponent and staminaComponent:
		health_bar.size = Vector2((healthComponent.health / MAX_VALUE) * BAR_WIDTH, BAR_HEIGHT)
		mana_bar.size = Vector2((manaComponent.mana / MAX_VALUE) * BAR_WIDTH, BAR_HEIGHT)
		stamina_bar.size = Vector2((staminaComponent.stamina / MAX_VALUE) * BAR_WIDTH, BAR_HEIGHT)
		health_bar.position = player.position + Vector2(-15, -24)
		mana_bar.position = player.position + Vector2(-15, -22)
		stamina_bar.position = player.position + Vector2(-15, -20)
