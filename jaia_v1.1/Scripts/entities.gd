class_name Entity

extends Node2D

signal name_changed(new_name)
signal health_changed(new_health)
signal mana_changed(new_mana)
signal stamina_changed(new_stamina)

@export var entity_name: String:
	get:
		return entity_name
	set(new_name):
		name_changed.emit(new_name)

@export var health: int:
	get:
		return health
	set(value):
		health = clamp(value, 0, 100)
		health_changed.emit(health)

@export var mana: int:
	get:
		return mana
	set(value):
		mana = clamp(value, 0, 100)
		mana_changed.emit(mana)

@export var stamina: int:
	get:
		return stamina
	set(value):
		stamina = clamp(value, 0, 100)
		stamina_changed.emit(stamina)
