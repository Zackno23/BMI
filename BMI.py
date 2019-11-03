class BMI_Calculation:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
        self.BMI = round(self.weight / (self.height ** 2))

    def dangerousity(self):
        if self.BMI > 30:
            return "死にますよ"
        else:
            return "正常です"


chikara_BMI = BMI_Calculation(name="chikara", height=1.7, weight=70)

noriya_BMI = BMI_Calculation(name="chikara", height=1.7, weight=70)
if __name__ == '__main__':
    print(chikara_BMI.dangerousity())
