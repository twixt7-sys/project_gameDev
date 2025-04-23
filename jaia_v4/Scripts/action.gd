class_name Action
extends Node2D

@export var player: Player
@export var sprite: AnimatedSprite2D

var cooldowns = {}

func action(action_name: String, cooldown: float,	cond: bool, logic: Callable, at_end = func(): null):
	if is_on_cooldown(action_name) or not cond: return func(): print(action_name, " failed.")
	logic.call()
	start_cooldown(action_name, cooldown, at_end)

func is_on_cooldown(action_name: String) -> bool:
	return cooldowns.has(action_name)

func start_cooldown(action_name: String, duration: float, at_end: Callable) -> void:
	var timer = Timer.new()
	timer.wait_time = duration
	timer.one_shot = true
	timer.autostart = true
	timer.name = action_name + "_cooldown"
	timer.timeout.connect(func():
		cooldowns.erase(action_name)
		timer.queue_free()
	)
	add_child(timer)
	cooldowns[action_name] = timer
	at_end.call()
