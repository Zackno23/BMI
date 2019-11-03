# 体重／(身長＊＊2)

class BMI:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def calculate(self):
        BMI = self.weight / (self.height ** 2)
        BMI_round = round(BMI, 2)
        if BMI_round < 10 or BMI_round > 40:
            raise ValueError("入力が間違ってます")
        return [self.name, BMI_round]


chikara = BMI(name="chikara", height=1.7, weight=70)
if __name__ == '__main__':
    print(chikara.calculate())
