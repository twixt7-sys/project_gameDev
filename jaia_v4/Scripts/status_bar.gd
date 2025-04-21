class_name StatusBar
extends Node

@export var entity: Node2D
@onready var sprite: Sprite2D = $"../Animation/Player"

@export var healthComponent : HealthComponent
@export var manaComponent : ManaComponent
@export var staminaComponent : StaminaComponent

@onready var health_bar: ColorRect = $HealthBar
@onready var mana_bar: ColorRect = $ManaBar
@onready var stamina_bar: ColorRect = $StaminaBar

const BAR_HEIGHT = 2.0

func _process(delta: float) -> void:
	var BAR_WIDTH = sprite.texture.get_size().x * sprite.scale.x / 9 
	if healthComponent:
		health_bar.size = Vector2((healthComponent.health / healthComponent.MAX_HEALTH) * BAR_WIDTH, BAR_HEIGHT)
	if manaComponent:
		mana_bar.size = Vector2((manaComponent.mana / manaComponent.MAX_MANA) * BAR_WIDTH, BAR_HEIGHT)
	if staminaComponent:
		stamina_bar.size = Vector2((staminaComponent.stamina / staminaComponent.MAX_STAMINA) * BAR_WIDTH, BAR_HEIGHT)
	
