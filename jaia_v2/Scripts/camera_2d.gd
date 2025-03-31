extends Camera2D

@export var target: NodePath  # Assign the Player node in the Inspector
@export var smooth_speed: float = 5.0  # Adjust for smoother movement

var player: Node2D

func _ready():
	player = get_node(target)  # Get the player node from the NodePath

func _process(delta):
	if player:
		# Smoothly move the camera towards the player
		position = position.lerp(player.position, smooth_speed * delta)
