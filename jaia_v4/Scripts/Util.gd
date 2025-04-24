class_name Util

extends Node

static func wait(n: float) -> void:
	var timer := Timer.new()
	add_child(timer)
	timer.start(n)
	await timer.timeout
	timer.queue_free()
