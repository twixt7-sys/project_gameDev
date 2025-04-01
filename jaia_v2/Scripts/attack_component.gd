class_name AttackComponent

extends Node2D

@export var ATTACK_DMG := 10.0
@export var KNOCKBACK_FORCE := 5.0
@export var STUN_TIME := 1.5
@export var ATTACK_POSITION := Vector2(50, 0)

var attack_damage: float
var knockback_force: float
var stun_time: float

func _ready() -> void:
	attack_damage = ATTACK_DMG
	knockback_force = KNOCKBACK_FORCE
	stun_time = STUN_TIME
