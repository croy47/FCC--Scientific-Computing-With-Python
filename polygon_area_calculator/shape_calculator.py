class Rectangle:
    # 
    def __init__(self, width, height):
        self.width = width
        self.height = height
    # 
    def __repr__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"
    # 
    def set_width(self, new_width):
        self.width = new_width
    # 
    def set_height(self, new_height):
        self.height = new_height
    # 
    def get_area(self):
        return self.width * self.height
    # 
    def get_perimeter(self):
        return 2 * (self.width + self.height)
    # 
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    # 
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            line = "*" * self.width + "\n"
            picture = line * self.height
            return picture
    # 
    def get_amount_inside(self, inner_polygon):
        return (self.width// inner_polygon.width) * (self.height // inner_polygon.height) 
# ==========================================================================
# SQUARE
class Square(Rectangle):
    # 
    def __init__(self, side):
        super().__init__(side, side)
    # 
    def __repr__(self) -> str:
        return f"Square(side={self.width})"
    # 
    def set_side(self, new_side):
        super().set_width(new_side)
        super().set_height(new_side)
    # 
    def set_width(self, new_width):
        super().set_width(new_width)
        super().set_height(new_width)
    # 
    def set_height(self, new_height):
        super().set_width(new_height)
        super().set_height(new_height)
# ===================================================================

# rect = Rectangle(10, 5)
# print(rect.get_area())
# rect.set_height(3)
# print(rect.get_perimeter())
# print(rect)
# print(rect.get_picture())

# sq = Square(9)
# print(sq.get_area())
# sq.set_side(4)
# print(sq.get_diagonal())
# print(sq)
# print(sq.get_picture())

# rect.set_height(8)
# rect.set_width(16)
# print(rect.get_amount_inside(sq))