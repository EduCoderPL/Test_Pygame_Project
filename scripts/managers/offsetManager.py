from scripts.utils.mathHelper import lerp


class OffsetManager:
    def __init__(self, offset=(0, 0), lerpCoef=0.1):
        self.offset = offset
        self.lerpCoef = lerpCoef

    def get_offset(self):
        return self.offset

    def update_offset(self, targetOffset):
        self.offset = (
            lerp(self.offset[0], targetOffset[0], self.lerpCoef),
            lerp(self.offset[1], targetOffset[1], self.lerpCoef)
        )
