extends CharacterBody2D

@onready var animated_sprite_2d: AnimatedSprite2D = $"AnimatedSprite2D"
@onready var dash_particles: GPUParticles2D = $DashParticles

#player attributes
const acceleration = 25

#environment attributes
const friction = 0.85

#variables
var dir = [1, 1]
var accel = [0, 0]
var accel_multiplier = 0
var vel_sum = 0

func _physics_process(delta: float) -> void:
	dir = [Input.get_axis("move_left", "move_right"), Input.get_axis("move_up", "move_down")]
	
	if Input.is_action_pressed("sprint"):
		accel_multiplier = 2
		dash_particles.emitting = true
	else:
		accel_multiplier = 1
		dash_particles.emitting = false
	
	accel = [dir[0] * acceleration, dir[1] * acceleration]
	
	velocity.x += accel[0] * accel_multiplier 
	velocity.y += accel[1] * accel_multiplier
	velocity.x *= friction
	velocity.y *= friction
	position.x += velocity.x * delta
	position.y += velocity.y * delta
	
	if dir[0] > 0:
		animated_sprite_2d.flip_h = false
		dash_particles.scale.x = 1
	elif dir[0] < 0:
		animated_sprite_2d.flip_h = true
		dash_particles.scale.x = -1
	
	vel_sum = abs(velocity.x) + abs(velocity.y)
	
	if Input.is_action_pressed("sprint") and vel_sum > 100:
		animated_sprite_2d.play("sprint")
	elif vel_sum > 100:
		animated_sprite_2d.play("walk")
	elif vel_sum > 0:
		animated_sprite_2d.play("idle")
		
	print(vel_sum)
