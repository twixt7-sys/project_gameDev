class_name Player
extends CharacterBody2D

@onready var animation_tree: AnimationTree = $AnimationTree
@onready var movement: MovementComponent = $"Movement Component"
@onready var atk: Attack = $Attack
@onready var action: Action = $Action
@onready var animation_player: AnimationPlayer = $AnimationPlayer

var dir: Vector2 = Vector2.ZERO

func _ready() -> void:
	animation_tree.active = true

func _process(delta: float) -> void:
	update_animation_parameters()

func _physics_process(delta: float) -> void:
	move(delta, Input.is_action_pressed("sprint")) 
	attack(Input.is_action_just_pressed("slash"))
	backstep(Input.is_action_just_pressed("backstep"))
	roll(Input.is_action_just_pressed("roll"))

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
	action.action("attack", 0.5, true, on_start)

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
	action.action("roll", 0.5, true, on_start, on_end)

func backstep(cond: bool):
	if not cond: return
	var on_start = func():
		print("Player Backstepped.")
		movement.can_flip = false
		movement.backstep()
	var on_end = func():
		movement.can_flip = true
	action.action("backstep", 0.5, true, on_start, on_end)

func update_animation_parameters():

	animation_tree["parameters/conditions/attack"] = true if Input.is_action_just_pressed("slash") else false
	animation_tree["parameters/conditions/is_rolling"] = true if Input.is_action_pressed("roll") else false

	if animation_tree["parameters/conditions/is_rolling"]:
		return

	if Input.is_action_pressed("sprint") and velocity != Vector2.ZERO:
		animation_tree["parameters/conditions/is_running"] = true
		animation_tree["parameters/conditions/is_moving"] = false
		animation_tree["parameters/conditions/idle"] = false
	elif velocity != Vector2.ZERO:
		animation_tree["parameters/conditions/is_running"] = false
		animation_tree["parameters/conditions/is_moving"] = true
		animation_tree["parameters/conditions/idle"] = false
	else:
		animation_tree["parameters/conditions/is_running"] = false
		animation_tree["parameters/conditions/is_moving"] = false
		animation_tree["parameters/conditions/idle"] = true

	if dir != Vector2.ZERO: for x in ["idle", "walk", "run", "roll/BlendSpace2D"]:
		animation_tree["parameters/%s/blend_position" % x] = dir
