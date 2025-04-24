class_name Player
extends CharacterBody2D

signal attack_area_entered(enemy, attacker)

#components
@onready var stamina_component: StaminaComponent = $"Components/Stamina Component"
@onready var movement_component: MovementComponent = $"Components/Movement Component"
@onready var attack_component: Attack = $"Components/Attack Component"
@onready var action_component: Action = $"Components/Action Component"
@onready var health_component: HealthComponent = $"Components/Health Component"
@onready var mana_component: ManaComponent = $"Components/Mana Component"

@onready var animation_tree: AnimationTree = $Animation/PlayerAnim
@onready var animation_player: AnimationPlayer = $Animation/PlayerAP

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
	action_component.action("move", 0.00001, true, func():
		dir = Input.get_vector("move_left", "move_right", "move_up", "move_down").normalized()
		movement_component.move(delta, dir, run)
	)

func attack(cond: bool):
	if not cond: return
	var on_start = func():
		print("Player Attacked.")
		attack_component.origin = global_position
		movement_component.dash()
		if stamina_component.stamina > 8:
			stamina_component.stamina -= 8
	action_component.action("attack", 0.5, true, on_start)

func roll(cond: bool):
	if not cond: return
	var on_start = func():
		print("Player Rolled.")
		movement_component.can_flip = false
		movement_component.can_roll = false
		movement_component.dash()
	var on_end = func():
		movement_component.can_flip = true
		movement_component.can_roll = true
	action_component.action("roll", 0.5, true, on_start, on_end)

func backstep(cond: bool):
	if not cond: return
	var on_start = func():
		print("Player Backstepped.")
		movement_component.can_flip = false
		movement_component.backstep()
	var on_end = func():
		movement_component.can_flip = true
	action_component.action("backstep", 0.5, true, on_start, on_end)

func update_animation_parameters():
	var is_attacking = Input.is_action_just_pressed("slash")
	var is_rolling = Input.is_action_just_pressed("roll")
	var backstep = Input.is_action_just_pressed("backstep")

	# Prioritize input
	animation_tree["parameters/conditions/backstep"] = backstep
	animation_tree["parameters/conditions/attack"] = is_attacking and not backstep
	animation_tree["parameters/conditions/is_rolling"] = is_rolling and not is_attacking and not backstep

	if is_attacking or is_rolling or backstep:
		for cond in ["is_running", "is_moving", "idle"]:
			animation_tree["parameters/conditions/%s" % cond] = false
	else:
		var velocity_threshold = 3
		var moving = velocity.length() >= velocity_threshold
		var sprinting = Input.is_action_pressed("sprint") and moving
		animation_tree["parameters/conditions/is_running"] = sprinting
		animation_tree["parameters/conditions/is_moving"] = moving and not sprinting
		animation_tree["parameters/conditions/idle"] = velocity.length() < velocity_threshold
	
	stamina_component.REGEN = 0.75 if velocity.length() < 3 else 0.25
	
	if dir != Vector2.ZERO:
		for x in ["idle", "walk", "run", "roll/BlendSpace2D", "attack/BlendSpace2D", "backstep/BlendSpace2D"]:
			animation_tree["parameters/%s/blend_position" % x] = dir


func _on_attack_area_area_entered(enemy: BlueSlime) -> void:
	emit_signal("attack_area_entered", enemy, self)
