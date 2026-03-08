try:
    age = int(input("Ievadi vecumu: "))

    if age < 0:
        print("Vecums nevar būt negatīvs!")
    else:
        license_input = input("Vai ir autovadītāja apliecība? (j/n): ")
        student_input = input("Vai ir students? (j/n): ")
        veteran_input = input("Vai ir veterāns? (j/n): ")

        # pārvērš j/n uz True/False
        has_license = license_input == "j"
        is_student = student_input == "j"
        is_veteran = veteran_input == "j"

        print("\n---")

        # Balsošana
        if age >= 18:
            print(f"Balsošana: Jā ✓")
        else:
            print(f"Balsošana: Nē ✗")

        # Auto īre
        if age >= 21 and has_license:
            print(f"Auto īre: Jā ✓")
        elif age >= 21 and not has_license:
            print(f"Auto īre: Nē ✗ (nav apliecības)")
        else:
            print(f"Auto īre: Nē ✗ (par jaunu)")

        # Veterānu atlaide
        if age >= 65 or is_veteran:
            print(f"Veterānu atlaide: Jā ✓")
        else:
            print(f"Veterānu atlaide: Nē ✗")

        # Studentu atlaide
        if 16 <= age <= 26 and is_student:
            print(f"Studentu atlaide: Jā ✓")
        else:
            print(f"Studentu atlaide: Nē ✗")

except ValueError:
    print("Kļūda: jāievada skaitlis!")