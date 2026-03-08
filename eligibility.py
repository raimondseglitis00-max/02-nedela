try:
    age = int(input("Ievadi vecumu: "))

    if age < 0:
        print("Kļūda: vecums nevar būt negatīvs!")
    else:
        license_input = input("Vai ir autovadītāja apliecība? (j/n): ")
        student_input = input("Vai ir students? (j/n): ")
        veteran_input = input("Vai ir veterāns? (j/n): ")

        # pārvērš j/n uz bool
        has_license = license_input.lower() == "j"
        is_student = student_input.lower() == "j"
        is_veteran = veteran_input.lower() == "j"

        # kompleksas loģiskās izteiksmes
        can_vote = age >= 18
        can_rent_car = age >= 21 and has_license
        senior_discount = age >= 65 or is_veteran
        student_discount = 16 <= age <= 26 and is_student

        print("\n---")

        # rezultāti ar f-string
        print(f"Balsošana: {'Jā ✓' if can_vote else 'Nē ✗'}")

        if age >= 21 and not has_license:
            print(f"Auto īre: Nē ✗ (nav apliecības)")
        else:
            print(f"Auto īre: {'Jā ✓' if can_rent_car else 'Nē ✗'}")

        print(f"Senioru atlaide: {'Jā ✓' if senior_discount else 'Nē ✗'}")
        print(f"Studentu atlaide: {'Jā ✓' if student_discount else 'Nē ✗'}")

except ValueError:
    print("Kļūda: jāievada skaitlis!")