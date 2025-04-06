class_name AttackComponent

extends Node2D

@export var ATTACK_DMG: float
@export var KNOCKBACK_FORCE: float
@export var STUN_TIME: float
@export var ATTACK_POSITION: Vector2

var attack_damage: float
var knockback_force: float
var stun_time: float
var attack_position: Vector2

func _ready() -> void:
	attack_damage = ATTACK_DMG
	knockback_force = KNOCKBACK_FORCE
	stun_time = STUN_TIME
	attack_position = global_position

func attack_triggered():
	print("An entity is being attacked.")
