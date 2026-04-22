import os
import csv
import json

# ==============================
# FUNCTIONS
# ==============================

def check_files():
    print("Checking file...")
    if not os.path.exists("students.csv"):
        print("Error: students.csv not found. Please download the file from LMS.")
        return False
    print("File found: students.csv")

    print("Checking output folder...")
    if not os.path.exists("output"):
        os.makedirs("output")
        print("Output folder created: output/")
    else:
        print("Output folder already exists: output/")

    return True


def load_data(filename):
    print("Loading data...")
    students = []
    try:
        with open(filename, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                students.append(row)
        print(f"Data loaded successfully: {len(students)} students")
        return students
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found. Please check the filename.")
        return []
    except Exception as e:
        print(f"Error while reading file: {e}")
        return []


def preview_data(students, n=5):
    print("First 5 rows:")
    print("------------------------------")
    for row in students[:n]:
        print(f"{row.get('student_id')} | {row.get('age')} | {row.get('gender')} | {row.get('country')} | GPA: {row.get('GPA')}")
    print("------------------------------")


def analyse_sleep_vs_gpa(students):
    low_sleep_gpas = []
    high_sleep_gpas = []

    for s in students:
        try:
            sleep = float(s.get('sleep_hours', 0))
            gpa = float(s.get('GPA', 0))

            if sleep < 6:
                low_sleep_gpas.append(gpa)
            else:
                high_sleep_gpas.append(gpa)

        except ValueError:
            print(f"Warning: bad data for student {s.get('student_id', 'UNKNOWN')}")
            continue

    low_count = len(low_sleep_gpas)
    high_count = len(high_sleep_gpas)

    low_avg = round(sum(low_sleep_gpas) / low_count, 2) if low_count else 0
    high_avg = round(sum(high_sleep_gpas) / high_count, 2) if high_count else 0
    diff = round(high_avg - low_avg, 2)

    print("------------------------------")
    print("Sleep vs GPA Analysis")
    print("------------------------------")
    print(f"Students sleeping < 6 hours : {low_count}")
    print(f"Average GPA (< 6 hours) : {low_avg}")
    print(f"Students sleeping >= 6 hours : {high_count}")
    print(f"Average GPA (>= 6 hours) : {high_avg}")
    print(f"Difference in avg GPA : {diff}")
    print("------------------------------")

    return {
        "analysis": "Sleep vs GPA",
        "total_students": len(students),
        "low_sleep": {"students": low_count, "avg_gpa": low_avg},
        "high_sleep": {"students": high_count, "avg_gpa": high_avg},
        "gpa_difference": diff
    }


def lambda_operations(students):
    print("------------------------------")
    print("Lambda / Map / Filter")
    print("------------------------------")

    low_sleep = list(filter(lambda s: float(s.get('sleep_hours', 0)) < 6, students))
    print(f"Students with sleep < 6 hrs : {len(low_sleep)}")

    gpa_values = list(map(lambda s: float(s.get('GPA', 0)), students))
    print(f"GPA values (first 5) : {gpa_values[:5]}")

    stressed = list(filter(lambda s: float(s.get('mental_stress_level', 0)) > 7, students))
    print(f"Students with stress > 7 : {len(stressed)}")

    print("------------------------------")


# ==============================
# CLASSES
# ==============================

class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def check_file(self):
        print("Checking file...")
        if os.path.exists(self.filename):
            print(f"File found: {self.filename}")
            return True
        else:
            print(f"Error: {self.filename} not found.")
            return False

    def create_output_folder(self, folder='output'):
        print("Checking output folder...")
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Output folder created: {folder}/")
        else:
            print(f"Output folder already exists: {folder}/")


class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load(self):
        print("Loading data...")
        try:
            with open(self.filename, encoding='utf-8') as f:
                reader = csv.DictReader(f)
                self.students = list(reader)
            print(f"Data loaded successfully: {len(self.students)} students")
        except FileNotFoundError:
            print("File not found.")
        return self.students

    def preview(self, n=5):
        print("First 5 rows:")
        print("------------------------------")
        for row in self.students[:n]:
            print(f"{row.get('student_id')} | {row.get('age')} | {row.get('gender')} | {row.get('country')} | GPA: {row.get('GPA')}")
        print("------------------------------")


class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        self.result = analyse_sleep_vs_gpa(self.students)
        return self.result

    def print_results(self):
        r = self.result
        print("==============================")
        print("ANALYSIS RESULT")
        print("==============================")
        print("Analysis : Sleep vs GPA")
        print(f"Total students : {r['total_students']}")
        print("------------------------------")
        print("Sleep < 6 hours:")
        print(f"Students : {r['low_sleep']['students']}")
        print(f"Average GPA : {r['low_sleep']['avg_gpa']}")
        print("Sleep >= 6 hours:")
        print(f"Students : {r['high_sleep']['students']}")
        print(f"Average GPA : {r['high_sleep']['avg_gpa']}")
        print("------------------------------")
        print(f"GPA difference : {r['gpa_difference']}")
        print("==============================")


class ResultSaver:
    def __init__(self, result, output_path):
        self.result = result
        self.output_path = output_path

    def save_json(self):
        try:
            with open(self.output_path, 'w', encoding='utf-8') as f:
                json.dump(self.result, f, indent=4)
            print(f"Result saved to {self.output_path}")
        except Exception as e:
            print(f"Error saving file: {e}")


# ==============================
# MAIN
# ==============================

if __name__ == "__main__":

    # FUNCTIONS PART
    if not check_files():
        exit()

    students = load_data("students.csv")
    preview_data(students)
    analyse_sleep_vs_gpa(students)
    lambda_operations(students)

    # TEST ERROR HANDLING
    load_data("wrong_file.csv")

    # OOP PART
    fm = FileManager('students.csv')
    if not fm.check_file():
        print("Stopping program.")
        exit()

    fm.create_output_folder()

    dl = DataLoader('students.csv')
    dl.load()
    dl.preview()

    analyser = DataAnalyser(dl.students)
    analyser.analyse()
    analyser.print_results()

    saver = ResultSaver(analyser.result, 'output/result.json')
    saver.save_json()