class BloodDistribution:
    def __init__(self, units_of_blood: list, patients: list) -> None:
        self.units_of_blood = units_of_blood  # amount of blood left in bank
        self.patients = patients # amount of patients still waiting for blood
        self.compatible = {
            0: [0],
            1: [1, 0],
            2: [2, 0],
            3: [3, 2, 1, 0],
            4: [4, 0],
            5: [5, 4, 1, 0],
            6: [0, 2, 4, 6],
            7: list(range(8))
        }

    def check_blood(self):
        donations = 0
        # loop through patients array
        for i in range(len(self.patients)):
            #  loop through possible matches for the blood type
            for blood_type in self.compatible[i]:
                #  blood available for current blood type
                blood_available = self.units_of_blood[blood_type]
                # patients left to serve for current blood type
                patients_left = self.patients[i]

                # no more blood to donate
                if blood_available == 0:
                    continue
                
                # all patients for current blood type served
                if patients_left == 0:
                    
                    break
                
                # more blood than there is patients
                if blood_available > patients_left:
                    # print(f"{patients_left} {i} patients take blood from {blood_type}")
                    donations += patients_left
                    blood_available -= patients_left
                    patients_left = 0
                # less blood than patients
                else:
                    # print(f"{blood_available} {i} patients take blood from {blood_type} ***")
                    donations += blood_available
                    patients_left -= blood_available
                    blood_available = 0

                # update instance variables
                self.units_of_blood[blood_type] = blood_available
                self.patients[i] = patients_left
        
        return donations

if __name__ == "__main__":
    while(True):
        try:
            blood = [x for x in input("Enter units of blood array: ").split()]
            blood = list(map((lambda x: int(x)), blood))
            patients = [x for x in input("Enter patients array: ").split()]
            patients = list(map((lambda x: int(x)), patients))            
        except ValueError:
            print("Invalid input")
            continue
        else:
            break

    donateBlood = BloodDistribution(blood, patients)
    print(donateBlood.check_blood())

# Example:
# --------
# Input:
# 175 265 110 72 276 132 420 149
# 73 381 26 348 360 198 410 20
# Output:
# 1460