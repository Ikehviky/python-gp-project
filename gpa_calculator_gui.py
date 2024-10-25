import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.scrolledtext import ScrolledText

class GPACalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Nigerian Polytechnic GPA Calculator")
        self.root.geometry("800x600")
        
        # Style configuration
        style = ttk.Style()
        style.configure('Header.TLabel', font=('Arial', 14, 'bold'))
        style.configure('Bold.TLabel', font=('Arial', 10, 'bold'))
        
        self.courses = []
        self.create_main_ui()
        
    def create_main_ui(self):
        # Main notebook for tabs
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Semester GPA tab
        semester_frame = ttk.Frame(notebook)
        notebook.add(semester_frame, text='Semester GPA')
        self.create_semester_tab(semester_frame)
        
        # CGPA tab
        cgpa_frame = ttk.Frame(notebook)
        notebook.add(cgpa_frame, text='CGPA')
        self.create_cgpa_tab(cgpa_frame)
        
    def create_semester_tab(self, parent):
        # Course Entry Section
        entry_frame = ttk.LabelFrame(parent, text="Enter Course Details", padding=10)
        entry_frame.pack(fill='x', padx=10, pady=5)
        
        # Course Code
        ttk.Label(entry_frame, text="Course Code:").grid(row=0, column=0, padx=5, pady=5)
        self.course_code = ttk.Entry(entry_frame)
        self.course_code.grid(row=0, column=1, padx=5, pady=5)
        
        # Credit Units
        ttk.Label(entry_frame, text="Credit Units:").grid(row=0, column=2, padx=5, pady=5)
        self.credit_units = ttk.Entry(entry_frame, width=10)
        self.credit_units.grid(row=0, column=3, padx=5, pady=5)
        
        # Score
        ttk.Label(entry_frame, text="Score (0-100):").grid(row=0, column=4, padx=5, pady=5)
        self.score = ttk.Entry(entry_frame, width=10)
        self.score.grid(row=0, column=5, padx=5, pady=5)
        
        # Add Course Button
        add_btn = ttk.Button(entry_frame, text="Add Course", command=self.add_course)
        add_btn.grid(row=0, column=6, padx=5, pady=5)
        
        # Course List Display
        list_frame = ttk.LabelFrame(parent, text="Courses Added", padding=10)
        list_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Treeview for courses
        columns = ('code', 'units', 'score', 'grade', 'points', 'weighted')
        self.course_tree = ttk.Treeview(list_frame, columns=columns, show='headings')
        
        # Define headings
        self.course_tree.heading('code', text='Course Code')
        self.course_tree.heading('units', text='Units')
        self.course_tree.heading('score', text='Score')
        self.course_tree.heading('grade', text='Grade')
        self.course_tree.heading('points', text='Grade Points')
        self.course_tree.heading('weighted', text='Weighted Points')
        
        # Define columns width
        self.course_tree.column('code', width=100)
        self.course_tree.column('units', width=70)
        self.course_tree.column('score', width=70)
        self.course_tree.column('grade', width=70)
        self.course_tree.column('points', width=100)
        self.course_tree.column('weighted', width=120)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(list_frame, orient='vertical', command=self.course_tree.yview)
        self.course_tree.configure(yscrollcommand=scrollbar.set)
        
        # Pack the treeview and scrollbar
        self.course_tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Results Section
        results_frame = ttk.LabelFrame(parent, text="Results", padding=10)
        results_frame.pack(fill='x', padx=10, pady=5)
        
        # GPA Result
        self.gpa_label = ttk.Label(results_frame, text="GPA: 0.00", font=('Arial', 12, 'bold'))
        self.gpa_label.pack(side='left', padx=10)
        
        # Total Units
        self.units_label = ttk.Label(results_frame, text="Total Units: 0", font=('Arial', 12, 'bold'))
        self.units_label.pack(side='left', padx=10)
        
        # Control Buttons
        btn_frame = ttk.Frame(parent)
        btn_frame.pack(fill='x', padx=10, pady=5)
        
        ttk.Button(btn_frame, text="Calculate GPA", command=self.calculate_gpa).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Clear All", command=self.clear_semester).pack(side='left', padx=5)
        
    def create_cgpa_tab(self, parent):
        # Semester Entry Section
        entry_frame = ttk.LabelFrame(parent, text="Enter Semester Details", padding=10)
        entry_frame.pack(fill='x', padx=10, pady=5)
        
        # GPA Entry
        ttk.Label(entry_frame, text="Semester GPA:").grid(row=0, column=0, padx=5, pady=5)
        self.semester_gpa = ttk.Entry(entry_frame)
        self.semester_gpa.grid(row=0, column=1, padx=5, pady=5)
        
        # Units Entry
        ttk.Label(entry_frame, text="Total Units:").grid(row=0, column=2, padx=5, pady=5)
        self.semester_units = ttk.Entry(entry_frame)
        self.semester_units.grid(row=0, column=3, padx=5, pady=5)
        
        # Add Semester Button
        add_btn = ttk.Button(entry_frame, text="Add Semester", command=self.add_semester)
        add_btn.grid(row=0, column=4, padx=5, pady=5)
        
        # Semester List Display
        list_frame = ttk.LabelFrame(parent, text="Semesters Added", padding=10)
        list_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Treeview for semesters
        columns = ('semester', 'gpa', 'units')
        self.semester_tree = ttk.Treeview(list_frame, columns=columns, show='headings')
        
        # Define headings
        self.semester_tree.heading('semester', text='Semester')
        self.semester_tree.heading('gpa', text='GPA')
        self.semester_tree.heading('units', text='Units')
        
        # Define columns width
        self.semester_tree.column('semester', width=100)
        self.semester_tree.column('gpa', width=100)
        self.semester_tree.column('units', width=100)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(list_frame, orient='vertical', command=self.semester_tree.yview)
        self.semester_tree.configure(yscrollcommand=scrollbar.set)
        
        # Pack the treeview and scrollbar
        self.semester_tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Results Section
        results_frame = ttk.LabelFrame(parent, text="Results", padding=10)
        results_frame.pack(fill='x', padx=10, pady=5)
        
        # CGPA Result
        self.cgpa_label = ttk.Label(results_frame, text="CGPA: 0.00", font=('Arial', 12, 'bold'))
        self.cgpa_label.pack(side='left', padx=10)
        
        # Total Units
        self.total_units_label = ttk.Label(results_frame, text="Total Units: 0", font=('Arial', 12, 'bold'))
        self.total_units_label.pack(side='left', padx=10)
        
        # Control Buttons
        btn_frame = ttk.Frame(parent)
        btn_frame.pack(fill='x', padx=10, pady=5)
        
        ttk.Button(btn_frame, text="Calculate CGPA", command=self.calculate_cgpa).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Clear All", command=self.clear_cgpa).pack(side='left', padx=5)
    
    def get_grade_point(self, score):
        if score >= 70:
            return 4.0, 'A'
        elif score >= 60:
            return 3.5, 'AB'
        elif score >= 50:
            return 3.0, 'B'
        elif score >= 45:
            return 2.5, 'BC'
        elif score >= 40:
            return 2.0, 'C'
        elif score >= 35:
            return 1.5, 'CD'
        elif score >= 30:
            return 1.0, 'D'
        else:
            return 0.0, 'F'
    
    def add_course(self):
        try:
            code = self.course_code.get().strip()
            units = float(self.credit_units.get())
            score = float(self.score.get())
            
            if not code:
                raise ValueError("Course code cannot be empty")
            if score < 0 or score > 100:
                raise ValueError("Score must be between 0 and 100")
            if units <= 0:
                raise ValueError("Credit units must be greater than 0")
            
            grade_point, letter_grade = self.get_grade_point(score)
            weighted_points = grade_point * units
            
            # Add to treeview
            self.course_tree.insert('', 'end', values=(
                code, units, score, letter_grade, grade_point, f"{weighted_points:.2f}"
            ))
            
            # Clear entries
            self.course_code.delete(0, 'end')
            self.credit_units.delete(0, 'end')
            self.score.delete(0, 'end')
            
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    
    def calculate_gpa(self):
        total_points = 0
        total_units = 0
        
        for item in self.course_tree.get_children():
            values = self.course_tree.item(item)['values']
            units = float(values[1])
            weighted_points = float(values[5])
            
            total_units += units
            total_points += weighted_points
        
        if total_units == 0:
            messagebox.showwarning("Warning", "No courses added yet!")
            return
        
        gpa = total_points / total_units
        self.gpa_label.config(text=f"GPA: {gpa:.2f}")
        self.units_label.config(text=f"Total Units: {total_units}")
    
    def clear_semester(self):
        self.course_tree.delete(*self.course_tree.get_children())
        self.gpa_label.config(text="GPA: 0.00")
        self.units_label.config(text="Total Units: 0")
    
    def add_semester(self):
        try:
            gpa = float(self.semester_gpa.get())
            units = float(self.semester_units.get())
            
            if gpa < 0 or gpa > 4:
                raise ValueError("GPA must be between 0 and 4")
            if units <= 0:
                raise ValueError("Units must be greater than 0")
            
            # Add to treeview
            semester_num = len(self.semester_tree.get_children()) + 1
            self.semester_tree.insert('', 'end', values=(
                f"Semester {semester_num}", f"{gpa:.2f}", units
            ))
            
            # Clear entries
            self.semester_gpa.delete(0, 'end')
            self.semester_units.delete(0, 'end')
            
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    
    def calculate_cgpa(self):
        total_points = 0
        total_units = 0
        
        for item in self.semester_tree.get_children():
            values = self.semester_tree.item(item)['values']
            gpa = float(values[1])
            units = float(values[2])
            
            total_points += (gpa * units)
            total_units += units
        
        if total_units == 0:
            messagebox.showwarning("Warning", "No semesters added yet!")
            return
        
        cgpa = total_points / total_units
        self.cgpa_label.config(text=f"CGPA: {cgpa:.2f}")
        self.total_units_label.config(text=f"Total Units: {total_units}")
    
    def clear_cgpa(self):
        self.semester_tree.delete(*self.semester_tree.get_children())
        self.cgpa_label.config(text="CGPA: 0.00")
        self.total_units_label.config(text="Total Units: 0")

if __name__ == "__main__":
    root = tk.Tk()
    app = GPACalculator(root)
    root.mainloop()