extends Area2D


func _on_body_entered(body: Node2D) -> void:
	print("+1 coin")
	queue_free()


func _on_killzone_body_entered(body: Node2D) -> void:
	pass # Replace with function body.
