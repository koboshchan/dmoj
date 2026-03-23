o1, o2, a1, a2, b1, b2, ab1, ab2 = map(int, input().split())
ro1, ro2, ra1, ra2, rb1, rb2, rab1, rab2 = map(int, input().split())

# o1 is O negative
# o2 is O positive
# r is receive
# r*o is original for calc at the end

"""
Each Type O patient requires Type O blood.
Each Type A patient may receive blood of Type A or Type O.
Each Type B patient may receive blood of Type B or Type O.
Each Type AB patient may receive blood of any type.

Patients who have Rh-negative blood can accept Rh-negative blood only, but patients with Rh-positive blood can accept either Rh-positive or Rh-negative types of blood.

We want as many patients as possible to receive a unit of blood. What is the maximum number of patients that can receive blood?
"""

# Corrected Algorithm - Maximum Flow approach
def solve():
    # Blood supplies: [O-, O+, A-, A+, B-, B+, AB-, AB+]
    blood = [o1, o2, a1, a2, b1, b2, ab1, ab2]
    
    # Patients needing: [O-, O+, A-, A+, B-, B+, AB-, AB+]
    patients = [ro1, ro2, ra1, ra2, rb1, rb2, rab1, rab2]
    
    treated = 0
    
    # Step 1: O- patients can ONLY receive O- blood
    give = min(patients[0], blood[0])
    treated += give
    patients[0] -= give
    blood[0] -= give
    
    # Step 2: A- patients prefer A- blood first, then O-
    give = min(patients[2], blood[2])
    treated += give
    patients[2] -= give
    blood[2] -= give
    
    # Remaining A- patients get O- blood
    give = min(patients[2], blood[0])
    treated += give
    patients[2] -= give
    blood[0] -= give
    
    # Step 3: B- patients prefer B- blood first, then O-
    give = min(patients[4], blood[4])
    treated += give
    patients[4] -= give
    blood[4] -= give
    
    # Remaining B- patients get O- blood
    give = min(patients[4], blood[0])
    treated += give
    patients[4] -= give
    blood[0] -= give
    
    # Step 4: AB- patients can take AB-, A-, B-, O- (in that order)
    give = min(patients[6], blood[6])  # AB- blood first
    treated += give
    patients[6] -= give
    blood[6] -= give
    
    give = min(patients[6], blood[2])  # A- blood
    treated += give
    patients[6] -= give
    blood[2] -= give
    
    give = min(patients[6], blood[4])  # B- blood
    treated += give
    patients[6] -= give
    blood[4] -= give
    
    give = min(patients[6], blood[0])  # O- blood
    treated += give
    patients[6] -= give
    blood[0] -= give
    
    # Step 5: O+ patients can take O+ or O-
    give = min(patients[1], blood[1])
    treated += give
    patients[1] -= give
    blood[1] -= give
    
    give = min(patients[1], blood[0])
    treated += give
    patients[1] -= give
    blood[0] -= give
    
    # Step 6: A+ patients can take A+, A-, O+, O-
    give = min(patients[3], blood[3])
    treated += give
    patients[3] -= give
    blood[3] -= give
    
    give = min(patients[3], blood[2])
    treated += give
    patients[3] -= give
    blood[2] -= give
    
    give = min(patients[3], blood[1])
    treated += give
    patients[3] -= give
    blood[1] -= give
    
    give = min(patients[3], blood[0])
    treated += give
    patients[3] -= give
    blood[0] -= give
    
    # Step 7: B+ patients can take B+, B-, O+, O-
    give = min(patients[5], blood[5])
    treated += give
    patients[5] -= give
    blood[5] -= give
    
    give = min(patients[5], blood[4])
    treated += give
    patients[5] -= give
    blood[4] -= give
    
    give = min(patients[5], blood[1])
    treated += give
    patients[5] -= give
    blood[1] -= give
    
    give = min(patients[5], blood[0])
    treated += give
    patients[5] -= give
    blood[0] -= give
    
    # Step 8: AB+ patients can take ANY remaining blood
    # But limited by the number of AB+ patients
    total_remaining_blood = sum(blood)
    ab_plus_patients_remaining = patients[7]
    give = min(ab_plus_patients_remaining, total_remaining_blood)
    treated += give
    
    return treated

print(solve())

