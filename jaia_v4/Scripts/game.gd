extends Node

@onready var player: Player = $Entities/Player
@onready var slimes: Array = []
@onready var gui: Control = $ControlParent/GUI
@onready var camera: Camera2D = $Entities/Player/Camera2D

# temps
@onready var bd_cake: Node2D = $"../../bd_cake"
@onready var cakee: AnimationPlayer = $Cakee

var i = 0
var event2 = false

func _ready() -> void:
	for entity in $Entities.get_children():
		if entity is BlueSlime:
			slimes.append(entity)
			entity.connect("patrol_area_exited", _on_patrol_area_exited)

func _process(delta: float) -> void:
	#event1
	if Input.is_action_just_pressed("act1"):
		player.movement_component.FRICTION = 0.80

	if Input.is_action_just_pressed("act2"):
		event2 = true
	if event2:
		player.text.visible = true
		player.action_component.action("print1", 0.5, true, func():
			if i == 0:
				player.content.text = "."
				i = i + 1
			elif i == 1:
				player.content.text = ". ."
				i = i + 1
			elif i == 2:
				player.content.text = ". . ."
				i = i + 1
			elif i == 3:
				player.content.text = ""
				i = i + 1
			else:
				i = 0)
	if Input.is_action_just_pressed("act3"):
		event2 = false
		player.content.scale = Vector2(0.4, 0.4)
		player.content.text = "sorry"
		
		var timer := Timer.new()
		add_child(timer)
		timer.start(3)
		await timer.timeout
		
		player.content.text = "I lied."
		
		timer.start(3)
		await timer.timeout
		
		player.text.scale = Vector2(2, 2)
		player.text.position += Vector2(5, -5)
		player.content.scale = Vector2(0.35, 0.35)
		player.textbox.size *= 2
		player.textbox.position -= Vector2(3, 1)
		player.content.text = "This ain't actually about the game."
		
		timer.start(3)
		await timer.timeout
		
		player.content.text = "This is actually for your birthday."
		
		timer.start(3)
		await timer.timeout
		
		player.content.text = "Sorry for being late dude."
		
		timer.start(3)
		await timer.timeout
		
		player.content.text = "Happy Birthday."
		
		timer.start(3)
		await timer.timeout

	if Input.is_action_just_pressed("act4"):
		
		cakee.play("spawn")
		
		var timer := Timer.new()
		add_child(timer)
		timer.start(3)
		await timer.timeout

		player.content.text = "Sorry it took a while"
		
		timer.start(8)
		await timer.timeout
		
		player.content.text = "Wishing you all the best. Always. ^ - ^"

func _physics_process(delta: float) -> void:
	for slime in slimes:
		slime = slime as BlueSlime
		slime.chase(delta, player)

func _on_blue_slime_patrol_area_entered(player: Player, slime: BlueSlime) -> void:
	player = player
	slime = slime

func _on_patrol_area_exited(player: Player, slime: BlueSlime):
	slime.patrol()
