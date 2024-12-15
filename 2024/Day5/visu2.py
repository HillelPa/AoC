from manim import *

class VisualizeNums(Scene):
    def construct(self):
        # Liste des nums à visualiser
        nums = [3, 2, 1, 4]
        self.visualize_nums(nums)
        self.check_nums(nums)

    def visualize_nums(self, nums, current=None, p1=None, p2=None, conflict=None, swap=None):
        """
        Affiche l'état actuel de nums.
        """
        # Créez des cercles pour chaque numéro
        positions = [LEFT * 3 + RIGHT * i for i in range(len(nums))]
        circles = [Circle(radius=0.5).move_to(pos) for pos in positions]
        texts = [Text(str(num)).move_to(pos) for num, pos in zip(nums, positions)]

        # Couleurs pour chaque état
        for i, circle in enumerate(circles):
            if i == current:
                circle.set_fill(RED, opacity=0.5)
            elif i == p1:
                circle.set_fill(GREEN, opacity=0.5)
            elif i == p2:
                circle.set_fill(BLUE, opacity=0.5)
            elif conflict and i in conflict:
                circle.set_fill(ORANGE, opacity=0.5)
            elif swap and i in swap:
                circle.set_fill(PURPLE, opacity=0.5)
            else:
                circle.set_fill(GRAY, opacity=0.5)

        # Affiche les cercles et les textes
        group = VGroup(*circles, *texts)
        self.play(Create(group))
        self.wait(1)
        self.play(Uncreate(group))

    def check_nums(self, nums):
        """
        Vérifie les nums et affiche les étapes visuellement.
        """
        for i in range(len(nums)):
            p1 = 0
            p2 = len(nums) - 1

            while p1 < i or p2 > i:
                self.visualize_nums(nums, current=i, p1=p1 if p1 < i else None, p2=p2 if p2 > i else None)

                if p1 < i and nums[p1] > nums[i]:
                    self.visualize_nums(nums, conflict=(i, p1))
                    self.swap(nums, p1, i)
                    return
                if p2 > i and nums[p2] < nums[i]:
                    self.visualize_nums(nums, conflict=(i, p2))
                    self.swap(nums, i, p2)
                    return

                p1 += 1
                p2 -= 1

    def swap(self, nums, i, j):
        """
        Effectue un échange visuel entre deux indices.
        """
        nums[i], nums[j] = nums[j], nums[i]
        self.visualize_nums(nums, swap=(i, j))
