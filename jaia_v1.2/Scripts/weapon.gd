class_name Weapon

extends Node2D

signal damage_dealt(area, atk)

@onready var sprite: AnimatedSprite2D = $AnimatedSprite2D
@onready var hitbox_component: HitboxComponent = $HitboxComponent

@export var atk:= Attack.new(global_position)

var attack_damage := 10

var flag = false
var hitbox: HitboxComponent

func _physics_process(delta: float) -> void:
	if flag:
		emit_signal("damage_dealt", hitbox, atk)
		var atk = Attack.new(global_position)
		hitbox.take_damage(atk)

func _on_hitbox_component_area_entered(hb: HitboxComponent) -> void:
	flag = true
	hitbox = hb
	
func _on_hitbox_component_area_exited(area: Area2D) -> void:
	flag = false

func attack():
	hitbox_component.disable_mode = CollisionObject2D.DISABLE_MODE_REMOVE
	sprite.play("default")
	sprite.speed_scale = atk.speed
	hitbox_component.disable_mode = CollisionObject2D.DISABLE_MODE_KEEP_ACTIVE

func flip_n_offset(bool_val: bool, x_offset: int):
	sprite.flip_h = bool_val
	sprite.position.x = x_offset
	hitbox_component.position.x = x_offset
