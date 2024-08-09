class Action(object):
    def oscillate(self, pos, speed, direction, osc_range):
        range1 = pos - osc_range
        range2 = pos + osc_range
        if pos <= range1 or pos >= range2:
            direction *= -1
        new_pos = pos + speed * direction
        return new_pos, direction