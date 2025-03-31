class_name Game

extends Node2D

func _ready() -> void:
	pass

func _process(delta: float) -> void:
	pass

func _on_entities_name_changed(new_name: Variant) -> void:
	print("An entity changed its name to: " + new_name)

func _on_entities_health_changed(new_health: Variant) -> void:
	print("An entity changed its health to: " + new_health)

func _on_entities_mana_changed(new_mana: Variant) -> void:
	print("An entity changed its mana to: " + new_mana)

func _on_entities_stamina_changed(new_stamina: Variant) -> void:
	print("An entity changed its stamina to: " + new_stamina)
