class_name Player

extends CharacterBody2D

@onready var animation_tree: AnimationTree = $AnimationTree
@onready var movement: MovementComponent = $"Movement Component"
@onready var atk: Attack = $Attack

func _physics_process(delta: float) -> void:
	movement.move(delta, Vector2(Input.get_axis("move_left","move_right"), Input.get_axis("move_up","move_down")), Input.is_action_pressed("sprint")) 
	attack(Input.is_action_pressed("slash"))

func attack(cond: bool): 
	atk.origin = global_position
	return atk.attack(func (): print()) if cond else null
