def get_grade_point(score):
    """Convert numerical score to grade point based on Nigerian polytechnic grading system"""
    if score >= 70:
        return 4.0  # A
    elif score >= 60:
        return 3.5  # AB
    elif score >= 50:
        return 3.0  # B
    elif score >= 45:
        return 2.5  # BC
    elif score >= 40:
        return 2.0  # C
    elif score >= 35:
        return 1.5  # CD
    elif score >= 30:
        return 1.0  # D
    else:
        return 0.0  # F

def get_letter_grade(score):
    """Convert numerical score to letter grade"""
    if score >= 70:
        return 'A'
    elif score >= 60:
        return 'AB'
    elif score >= 50:
        return 'B'
    elif score >= 45:
        return 'BC'
    elif score >= 40:
        return 'C'
    elif score >= 35:
        return 'CD'
    elif score >= 30:
        return 'D'
    else:
        return 'F'

def calculate_semester_gpa():
    """Calculate GPA for a single semester"""
    print("\n=== Semester GPA Calculator ===")
    
    courses = []
    total_credit_units = 0
    total_weighted_points = 0
    
    while True:
        course_code = input("\nEnter course code (or 'done' to finish): ")
        if course_code.lower() == 'done':
            break
            
        try:
            credit_units = float(input("Enter credit units: "))
            score = float(input("Enter score (0-100): "))
            
            if score < 0 or score > 100:
                print("Invalid score! Please enter a score between 0 and 100")
                continue
                
            grade_point = get_grade_point(score)
            letter_grade = get_letter_grade(score)
            weighted_points = grade_point * credit_units
            
            courses.append({
                'code': course_code,
                'units': credit_units,
                'score': score,
                'grade': letter_grade,
                'grade_point': grade_point,
                'weighted_points': weighted_points
            })
            
            total_credit_units += credit_units
            total_weighted_points += weighted_points
            
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue
    
    if total_credit_units == 0:
        print("\nNo courses entered!")
        return None
        
    gpa = total_weighted_points / total_credit_units
    
    # Print semester report
    print("\n=== Semester Report ===")
    print("\nCourse Code | Units | Score | Grade | Grade Point | Weighted Points")
    print("-" * 65)
    
    for course in courses:
        print(f"{course['code']:<11} | {course['units']:<5} | {course['score']:<5} | {course['grade']:<5} | {course['grade_point']:<11} | {course['weighted_points']:.2f}")
    
    print("-" * 65)
    print(f"\nTotal Credit Units: {total_credit_units}")
    print(f"Semester GPA: {gpa:.2f}")
    
    return gpa, total_credit_units

def calculate_cgpa():
    """Calculate CGPA across multiple semesters"""
    print("\n=== CGPA Calculator ===")
    
    semesters = []
    total_credit_units = 0
    total_weighted_points = 0
    
    while True:
        print(f"\nSemester {len(semesters) + 1}")
        result = calculate_semester_gpa()
        
        if result is None:
            continue
            
        semester_gpa, semester_units = result
        semesters.append({
            'gpa': semester_gpa,
            'units': semester_units
        })
        
        total_credit_units += semester_units
        total_weighted_points += semester_gpa * semester_units
        
        another = input("\nCalculate another semester? (yes/no): ")
        if another.lower() != 'yes':
            break
    
    if total_credit_units == 0:
        print("\nNo semesters calculated!")
        return
        
    cgpa = total_weighted_points / total_credit_units
    
    # Print CGPA report
    print("\n=== CGPA Report ===")
    print("\nSemester | GPA    | Credit Units")
    print("-" * 30)
    
    for i, sem in enumerate(semesters, 1):
        print(f"{i:<8} | {sem['gpa']:.2f}   | {sem['units']}")
    
    print("-" * 30)
    print(f"\nTotal Credit Units: {total_credit_units}")
    print(f"CGPA: {cgpa:.2f}")

def main():
    """Main program loop"""
    while True:
        print("\n=== Nigerian Polytechnic GPA Calculator ===")
        print("1. Calculate Semester GPA")
        print("2. Calculate CGPA")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '1':
            calculate_semester_gpa()
        elif choice == '2':
            calculate_cgpa()
        elif choice == '3':
            print("\nThank you for using the GPA Calculator!")
            break
        else:
            print("\nInvalid choice! Please select 1, 2, or 3")

if __name__ == "__main__":
    main()