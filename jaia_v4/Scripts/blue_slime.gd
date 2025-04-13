class_name BlueSlime

extends CharacterBody2D

signal patrol_area_entered(area, entity)
signal patrol_area_exited(area, entity)

@onready var patrol_area: Area2D = $PatrolArea
@onready var movement_component: MovementComponent = $"Movement Component"

var is_chasing = false
var is_patrolling = true

func _physics_process(delta: float) -> void:
	pass

func patrol():
	print("slime is patrolling.")
	
func chase(delta, player: Player):
	if is_patrolling:
			is_patrolling = false
			print("slime is chasing.")
	if is_chasing:
		var direction = (player.global_position - global_position).normalized()
		movement_component.move(delta, direction, false)

func _on_patrol_area_body_entered(body: Player) -> void:
	if body:
		is_chasing = true
		emit_signal("patrol_area_entered", body, self)

func _on_patrol_area_body_exited(body: Node2D) -> void:
	is_chasing = false
	is_patrolling = true
	print(self.name, " stopped chase.")
	emit_signal("patrol_area_exited", body, self)
