class_name Player
extends CharacterBody2D

@onready var animation_tree: AnimationTree = $AnimationTree
@onready var movement: MovementComponent = $"Movement Component"
@onready var atk: Attack = $Attack
@onready var sprite: AnimatedSprite2D = $AnimatedSprite2D
@onready var action: Action = $Action
@onready var animation_player: AnimationPlayer = $AnimationPlayer

var dir: Vector2 = Vector2.ZERO

func _ready() -> void:
	#animation_machine.add_state("roll", "is_rolling", func(): return movement.can_roll, func(): print("Roll done."))
	animation_tree.active = true

func _process(delta: float) -> void:
	update_animation_parameters()

func _physics_process(delta: float) -> void:
	move(delta, Input.is_action_pressed("sprint")) 
	attack(Input.is_action_just_pressed("slash"))
	backstep(Input.is_action_just_pressed("backstep"))
	roll(Input.is_action_just_pressed("roll"))
	#animation_machine.update()

func move(delta: float, run: bool) -> void:
	action.action("move", 0.00001, true, func():
		dir = Input.get_vector("move_left", "move_right", "move_up", "move_down").normalized()
		movement.move(delta, dir, run)
	)

func attack(cond: bool):
	if not cond: return
	var on_start = func():
		print("Player Attacked.")
		atk.origin = global_position
	action.action("attack", get_anim_length("attack"), true, on_start)

func roll(cond: bool):
	if not cond: return
	var on_start = func():
		print("Player Rolled.")
		movement.can_flip = false
		movement.can_roll = false
		movement.dash()
	var on_end = func():
		movement.can_flip = true
		movement.can_roll = true
	action.action("roll", get_anim_length("roll"), true, on_start, on_end)

func backstep(cond: bool):
	if not cond: return
	var on_start = func():
		print("Player Backstepped.")
		movement.can_flip = false
		sprite.play("roll")
		movement.backstep()
	var on_end = func():
		movement.can_flip = true
	action.action("backstep", get_anim_length("roll"), true, on_start, on_end)

func get_anim_length(anim_name: String) -> float:
	if animation_tree and animation_tree.has_animation(anim_name):
		return animation_tree.get_animation(anim_name).length
	elif animation_player and animation_player.has_animation(anim_name):
		return animation_player.get_animation(anim_name).length
	else:
		return 0.5  # fallback default

func update_animation_parameters():
	if (velocity == Vector2.ZERO):
		animation_tree["parameters/conditions/idle"] = true
		animation_tree["parameters/conditions/is_moving"] = false
	else:
		animation_tree["parameters/conditions/idle"] = false
		animation_tree["parameters/conditions/is_moving"] = true

	animation_tree["parameters/conditions/attack"] = true if Input.is_action_just_pressed("slash") else false
	
	if (dir != Vector2.ZERO):
		animation_tree["parameters/idle/blend_position"] = dir
		animation_tree["parameters/walk/blend_position"] = dir
